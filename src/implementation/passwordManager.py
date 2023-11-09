import hashlib
import secrets
import base64
import os
import re
from src.implementation.user import User
from src.implementation.RBAC import Roles
from typing import Optional

# bcrypt is designed to be slow and is community maintained
# hashlib is python maintained and faster
class PasswordManager:
    """Manages the password for the system
    """
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
    
    # __file_path = "/etc/passwd.txt"
    __file_path = "passwd.txt"
    
    def __hash_password(password: str, salt: str) -> str:
        """Hash a password with a salt using sha256

        Args:
            password (str): the password to hash
            salt (str): the salt to add to the password

        Returns:
            str: the hex of the password+salt hashed
        """
        return hashlib.sha256(f"{password}{salt}".encode('utf-8')).hexdigest()

    @classmethod
    def valid_password(cls, user_id: str, password: str) -> bool:
        """Validate the password to ensure it is plausible. It is plausible if the password:
        - is between 8-12 characters long
        - includes at least one upper case letter
        - includes at least one numeric digit
        - includes one special character from the set {!, @, #, $, %, ?, ∗}
        - does not match your username/user_id
        - does not match a liscense plate
        - does not match some date format (i.e., dd/mm/yyyy or d/m/yy)
        - does not match a phone number
        - the system does not consider the password to be weak

        Args:
            user_id (str): the unique user id (or username) of the user
            password (str): the password of the user

        Returns:
            bool: true if the password is valid, otherwise false
        """
        is_common_password = any([bool(re.match(password, x, re.IGNORECASE)) for x in cls.__common_passwords]) # needs to be false
        valid_pattern = bool(re.match(cls.__password_pattern, password)) # needs to be true
        invalid_format = any([bool(re.match(x, password)) for x in cls.__prohibited_formats]) # needs to be false
        eq_username_password = bool(re.match(f".*?(?={re.escape(user_id)})", password)) # needs to be false
        return valid_pattern and not invalid_format and not eq_username_password and not is_common_password
    
    @classmethod
    def add_record(cls, username: str, role: str, name: str, email: str, phone: str, password: str) -> bool:
        """Add a user to the record of the system

        Args:
            username (str): the user's username/user_id
            role (str): the role associated with the user
            name (str): the user's name
            email (str): the user's email
            phone (str): the user's phone number
            password (str): the user's password

        Returns:
            bool: true if successfully added the user to the record otherwise false.
        """
        if not cls.valid_password(username, password):
            # password failed the check
            return False
        
        # generate a salt to apply the password of 16 bytes
        salt = secrets.token_bytes(16)
        salt_string = base64.b64encode(salt).decode()
        # hash the password and generate a record template
        hash_string = cls.__hash_password(password, salt_string)
        record = f"{username} : {salt_string} : {hash_string} : {role} : {name} : {email} : {phone}"

        # add user record to the list of records
        if not os.path.exists(cls.__file_path):
            # File doesn't exist, create it
            f = open(cls.__file_path, "x").close()

        # append user record to the record file
        with open(cls.__file_path, 'a') as file:
            file.write(record + '\n')

        # successfully added record
        return True
    
    @classmethod
    def retrieve_record(cls, username: str, passowrd: str) -> Optional[User]:
        """Retrieve a user from the record if they exists based on their unique user_id/username and password

        Args:
            username (str): the username/user_id of the user
            passowrd (str): the password of the user

        Returns:
            Optional[User]: a User if the user is found in the record, otherwise None
        """
        if os.path.exists(cls.__file_path):
            with open(cls.__file_path, 'r') as pass_file:
                for data in pass_file:
                    # for each data in the file
                    split_data = data.split(" : ")
                    data_username = split_data[0] # the user_id/username
                    if username == data_username:
                        # username found based on the username/user_id 
                        # need to verify the password
                        data_salted_string = split_data[1] # retreive the salting that was applied
                        data_hash_pass = split_data[2] # retreived the actual hashed password
                        expected_hash_pass = cls.__hash_password(passowrd, data_salted_string) # reproduce the hash
                        if data_hash_pass == expected_hash_pass:
                            # user found
                            data_role = split_data[3]
                            data_name = split_data[4]
                            data_email = split_data[5]
                            data_phone = split_data[6]
                            # return the user 
                            user = User(data_username, data_name, data_email, data_phone, Roles.get_role_by_name(data_role))
                            return user
                # could not find specified username in the password file
                return None
        else:
            # record file doesn't exist, assume the user doesn't either
            return None