import re
import sys
from src.implementation.accessControl import AccessControl
from src.implementation.passwordFileManager import PasswordFileManager
from src.implementation.rbac.roles import Roles
from src.implementation.rbac.permissions import Permissions
from src.implementation.rbac.actions import Actions
from src.implementation.user import User
from typing import Union


class UserInterface:
    
    def __init__(self):
        self.access_control = AccessControl()
        self.password_file_manager = PasswordFileManager("passwd.txt")
        self.user: Union[User, None] = None
        # in regex, \d is any digit from 0 to 9, so match any numeric digit
        # .*? indicates match any character before the specified statement
        # Initial pattern for the password complexity requirements
        # (?=.*[A-Z]) specifies at least 1 upper case letter
        # (?=.*[a-z]) specifies at least 1 lower case letter
        # (?=.*\d) specifies at least 1 numerical digit
        # (?=.*[!@#$%?∗]) specifies at least one special character defined in the [...]
        # (?!.*\s) indicates no white space included
        # {8,12} indicates the password must be 8-12 length long inclusive
        self.__password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%?∗])(?!.*\s).{8,12}$"
        # List of prohibited formats (e.g., calendar dates, license plate numbers, phone numbers)
        # .*?(?=\d{1,2}/\d{1,2}/\d{2,4}): This pattern matches dates in the format of "dd/mm/yyyy" or "d/m/yy." ignores anything before and after
        # (?:[A-Z]{3,4}(?:-|)?[0-9]{3,4})|(?:[0-9]{3,4}(?:-|)?[A-Z]{3,4}): This pattern matches sequences that start with one to three uppercase letters followed by one to six digits.
        # .*?(?=\d{10,11}): This pattern matches sequences of 10 or 11 consecutive digits
        self.__prohibited_formats = [r".*?(?=\d{1,2}/\d{1,2}/\d{2,4})", r".*?(?=([A-Z]{3,4}[0-9]{3,4})|([0-9]{3,4}[A-Z]{3,4}))", r".*?(?=\d{10,11})"]
        self.__common_passwords = ["PaASsword@1", "Qwerty#@123", "Qaz12!3wsx"]
        
    
    def valid_password(self, user_id: str, password: str) -> bool:
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
        is_common_password = any([bool(re.match(password, x, re.IGNORECASE)) for x in self.__common_passwords]) # needs to be false
        valid_pattern = bool(re.match(self.__password_pattern, password)) # needs to be true
        invalid_format = any([bool(re.match(x, password)) for x in self.__prohibited_formats]) # needs to be false
        eq_username_password = bool(re.match(f".*?(?={re.escape(user_id)})", password)) # needs to be false
        return valid_pattern and not invalid_format and not eq_username_password and not is_common_password

    def __password_rules(self) -> str:
        """Display the password rules to the client

        Returns:
            str: the password rules
        """
        s = "Password Rules:\n"
        s += "-----------------\n"
        s += "- Must be at leat 8-12 characters in length\n"
        s += "- Include one upper case letter\n"
        s += "- Include one numeric digit\n"
        s += "- include one special character from the set {!, @, #, $, %, ?, ∗}\n"
        s += "- cannot match your username\n"
        s += "Note: if the password is considered weak by the system, it will also not pass"
        return s
        
    def __get_input(self, prompt: str, spaces=False) -> str:
        """get the input of the user

        Args:
            prompt (str): The prompt for the input

        Returns:
            str: the input of the user
        """
        s = ""
        while True: 
            s = input(f"{prompt} (or 'exit' to quit): ")

            if s.lower() == "exit": 
                # exit the enroll user system if the user wants by typing 'exit'
                print("Exiting...")
                sys.exit(1)
                
            if re.search(r"\s", s) and not spaces:
                print("Cannot have spaces")
                continue
            
            if not s:
                print("Input needed")
                continue
            
            break
         
        return s
    
    def login_user(self):
        """login interface
        """
        while True:
            username = self.__get_input("Enter Username")
            password = self.__get_input("Enter Password")
            self.user = self.password_file_manager.retrieve_record(username, password)
            
            if self.user:
                if not self.access_control.enforce_ABAC(self.user.role):
                    # enforce initial abac on user
                    continue
                print("Successful Log in\n")
            else: 
                print("Incorrect username or password. Try again")
                continue
            
            break
        
    def enroll_user(self): 
        """enroll user interface
        """
        while True:
            print("Enrolling User")
            print("-------------------")
            while True:
                username = self.__get_input("Username")
                if not self.password_file_manager.is_unique_username(username):
                    # username is not unique
                    print("Username already in use, try again.")
                    continue
                break
            name = self.__get_input("Name")
            email = self.__get_input("Email")
            phone = self.__get_input("Phone number")
            
            while True: 
                role = self.__get_input(f"Available Roles: {Roles.to_string()}\nRole Chosen:")
                if not Roles.role_exists(role):
                    # role selected is invalid
                    print("Invalid Role, please type again based on the selection.")
                    continue
                break
            
            while True:
                password = self.__get_input(f"{self.__password_rules()}\nInput Password:")
                if not self.valid_password(username, password):
                     # password provided was invalid, adding user to the record was unsuccessful
                    print("Bad password, please try again")
                    continue

                self.password_file_manager.add_record(username, role, name, email, phone, password)
                # valid password input, break out
                break
            
            print(f"Successfully enrolled user with username {username}")
    
    def perform_actions(self):
        """Action performed when the user is signed in
        """
        if not self.user:
            return
        
        print("---------------------------")
        print(f"Welcome {self.user.username}")
        print(f"Your current role is {self.user.role.value}")            
        print("-----------------------------")
        print()
        while True:
            print("What would like to do?")
            print("------------------------")
            
            for perm, lst_actions in self.access_control.get_permissions(self.user.role).items():
                perm_text = perm.value
                action_text = ", ".join([f"{action.value}" for action in lst_actions])
                print(f"{perm_text}: {action_text}")
            
            print()
            val = self.__get_input("Perform action (ex: perm action)", spaces=True)
            
            # validate the input
            split_input = val.split(" ")
            
            # validate number of inputs
            if len(split_input) != 2:
                print("Expected inputs is 2")
                continue
            
            #get the perm
            perm = split_input[0]
            enum_perm = Permissions.get_permission_by_string(perm)
            if not enum_perm:
                print("invalid permission input")
                continue

            # action type
            action = split_input[1]
            enum_action = Actions.get_action_by_string(action)
            if not enum_action:
                print("invalid action input")
                continue
            
            print()
            self.access_control.perform_access_control_policy(self.user.role, enum_action, enum_perm)
            print()
            
    def run(self):
        """run method
        """
        while True:
            s = self.__get_input("Would you like to Login (l) or Enroll (e)")

            if s.lower() == "l":
                self.login_user()
            elif s.lower() == "e": 
                self.enroll_user()
            else:
                print("Invalid option")
            
            # signed in
            self.perform_actions()

if __name__ == "__main__":
    UserInterface().run()