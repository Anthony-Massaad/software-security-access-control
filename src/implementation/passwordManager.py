import hashlib
import secrets
import base64
import os
import re
from src.implementation.user import User
from src.implementation.constants.roles import Roles

# bcrypt is designed to be slow and is community maintained
# hashlib is python maintained and faster
class PasswordManager:
# in regex, \d is any digit from 0 to 9, so match any numeric digit
    # .*? indicates match any character before the specified statement
    # Initial pattern for the password complexity requirements
    # (?=.*[A-Z]) specifies at least 1 upper case letter
    # (?=.*[a-z]) specifies at least 1 lower case letter
    # (?=.*\d) specifies at least 1 numerical digit
    # (?=.*[!@#$%?∗]) specifies at least one special character defined in the [...]
    # (?!.*\s) indicates no white space included
    # {8,12} indicates the password must be 8-12 length long inclusive
    __password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%?∗])(?!.*\s).{8,12}$"
    # List of prohibited formats (e.g., calendar dates, license plate numbers, phone numbers)
    # .*?(?=\d{1,2}/\d{1,2}/\d{2,4}): This pattern matches dates in the format of "dd/mm/yyyy" or "d/m/yy." ignores anything before and after
    # (?:[A-Z]{3,4}(?:-|)?[0-9]{3,4})|(?:[0-9]{3,4}(?:-|)?[A-Z]{3,4}): This pattern matches sequences that start with one to three uppercase letters followed by one to six digits.
    # .*?(?=\d{10,11}): This pattern matches sequences of 10 or 11 consecutive digits
    __prohibited_formats = [r".*?(?=\d{1,2}/\d{1,2}/\d{2,4})", r".*?(?=([A-Z]{3,4}[0-9]{3,4})|([0-9]{3,4}[A-Z]{3,4}))", r".*?(?=\d{10,11})"]
    __common_passwords = ["PaASsword@1", "Qwerty#@123", "Qaz12!3wsx"]
    
    __file_path = "/etc/passwd.txt"
    
    def __hash_password(password: str, salt: str):
        return hashlib.sha256(f"{password}{salt}".encode('utf-8')).hexdigest()

    @classmethod
    def valid_password(cls, user_id: str, password: str) -> bool:
        is_common_password = any([bool(re.match(password, x, re.IGNORECASE)) for x in cls.__common_passwords]) # needs to be false
        valid_pattern = bool(re.match(cls.__password_pattern, password)) # needs to be true
        invalid_format = any([bool(re.match(x, password)) for x in cls.__prohibited_formats]) # needs to be false
        eq_username_password = bool(re.match(f".*?(?={re.escape(user_id)})", password)) # needs to be false
        return valid_pattern and not invalid_format and not eq_username_password and not is_common_password
    
    @classmethod
    def add_record(cls, username: str, role: str, name: str, email: str, phone: str, password: str) -> bool:
        if not cls.valid_password(username, password):
            # password failed the check
            return False
        salt = secrets.token_bytes(16)
        salt_string = base64.b64encode(salt).decode()
        hash_string = cls.__hash_password(password, salt_string)
        record = f"{username} : {salt_string} : {hash_string} : {role} : {name} : {email} : {phone}"

        if not os.path.isfile(cls.__file_path):
            # File doesn't exist, create it and append the record
            with open(cls.__file_path, 'w') as file:
                file.write(record + '\n')
        else:
            # file already exists, append the new record
            with open(cls.__file_path, 'a') as file:
                file.write(record + '\n')

        # successfully added record
        return True
    
    @classmethod
    def retrieve_record(cls, username: str, passowrd: str) -> User:
        if os.path.isfile(cls.__file_path):
            with open(cls.__file_path, 'r') as pass_file:
                for data in pass_file:
                    split_data = data.split(" : ")
                    data_username = split_data[0]
                    if username == data_username:
                        data_salted_string = split_data[1]
                        data_hash_pass = split_data[2]
                        expected_hash_pass = cls.__hash_password(passowrd, data_salted_string)
                        if data_hash_pass == expected_hash_pass:
                            # user found
                            data_role = split_data[3]
                            data_name = split_data[4]
                            data_email = split_data[5]
                            data_phone = split_data[6]
                            user = User(data_username, data_name, data_email, data_phone, Roles.get_role_by_name(data_role))
                            return user
                # could not find specified username in the password file
                return None
        else:
            # record file doesn't exist, assume the user doesn't either
            return None