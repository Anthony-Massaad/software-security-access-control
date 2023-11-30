import hashlib
import secrets
import base64
import os
import re
from src.implementation.user import User
from src.implementation.rbac.roles import Roles
from typing import Optional

# bcrypt is designed to be slow and is community maintained
# hashlib is python maintained and faster
class PasswordFileManager:
    """Manages the password for the system
    """
    def __init__(self, password_file_ref: str):
        """default constructor
        """
        # __file_path = "/etc/passwd.txt"
        self.__file_path = password_file_ref
    
    def __hash_password(self, password: str, salt: str) -> str:
        """Hash a password with a salt using sha256

        Args:
            password (str): the password to hash
            salt (str): the salt to add to the password

        Returns:
            str: the hex of the password+salt hashed
        """
        return hashlib.sha256(f"{password}{salt}".encode('utf-8')).hexdigest()
    
    def is_unique_username(self, username: str) -> bool:
        """Handler to ensure the username selected is unique

        Args:
            username (str): the User's username

        Returns:
            bool: True if username is uniuque, otherwise False
        """
        if os.path.exists(self.__file_path):
            # check to see if the username/user_id already exists
            with open(self.__file_path, 'r') as pass_file:
                for data in pass_file:
                    split_data = data.split(" : ")
                    data_username = split_data[0] # the user_id/username
                    if username == data_username:
                        # username already exists meaning it cannot be used
                        return False
        # username passed
        return True
    
    def add_record(self, username: str, role: str, name: str, email: str, phone: str, password: str) -> bool:
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
        
        if not os.path.exists(self.__file_path):
            # password File doesn't exist, create it
            f = open(self.__file_path, "x").close()

        if not self.is_unique_username(username):
            print("Username is already in use")
            return False
        
        # generate a salt to apply the password of 16 bytes
        salt = secrets.token_bytes(16)
        salt_string = base64.b64encode(salt).decode()
        # hash the password and generate a record template
        hash_string = self.__hash_password(password, salt_string)
        record = f"{username} : {salt_string} : {hash_string} : {role} : {name} : {email} : {phone}"

        # add user record to the list of records
        # append user record to the record file
        with open(self.__file_path, 'a') as file:
            file.write(record + '\n')

        # successfully added record
        return True
    
    def retrieve_record(self, username: str, passowrd: str) -> Optional[User]:
        """Retrieve a user from the record if they exists based on their unique user_id/username and password

        Args:
            username (str): the username/user_id of the user
            passowrd (str): the password of the user

        Returns:
            Optional[User]: a User if the user is found in the record, otherwise None
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as pass_file:
                for data in pass_file:
                    # for each data in the file
                    split_data = data.split(" : ")
                    data_username = split_data[0] # the user_id/username
                    if username == data_username:
                        # username found based on the username/user_id 
                        # need to verify the password
                        data_salted_string = split_data[1] # retreive the salting that was applied
                        data_hash_pass = split_data[2] # retreived the actual hashed password
                        expected_hash_pass = self.__hash_password(passowrd, data_salted_string) # reproduce the hash
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