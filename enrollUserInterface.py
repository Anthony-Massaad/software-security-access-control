import sys
from src.implementation.RBAC import Roles
from src.implementation.passwordFileManager import PasswordFileManager
import re

class EnrollUserInterface:
    """Enroll user interface
    """
    
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
    
    def __get_input(self, prompt: str, is_role: bool = False) -> str:
        """get the input of the user

        Args:
            prompt (str): The prompt for the input
            is_role (bool, optional): True if the prompt is for Role. Defaults to False.

        Returns:
            str: the input of the user
        """
        while True: 
            s = ""
            s = input(f"{prompt} (or 'exit' to quit): ")

            if s.lower() == "exit": 
                # exit the enroll user system if the user wants by typing 'exit'
                print("Exiting Enrolling user")
                sys.exit(1)
                
            if not is_role:
                # if it's not the role selection, we don't want whitespace
                if re.search(r"\s", s):
                    print("Cannot have spaces")
                    continue
            break
         
        return s

    def run_interface(self) -> None:
        """The user interface for the enroll user
        """
        while True:
            print("Enrolling User")
            print("-------------------")
            while True:
                username = self.__get_input("Username")
                if not PasswordFileManager.is_unique_username(username):
                    # username is not unique
                    print("Username already in use, try again.")
                    continue
                break
            
            name = self.__get_input("Name")
            email = self.__get_input("Email")
            phone = self.__get_input("Phone number")
            
            while True: 
                role = self.__get_input(f"Available Roles: {Roles.to_string()}\nRole chosen:", is_role=True)
                if not Roles.role_exists(role):
                    # role selected is invalid
                    print("Invalid Role, please type again based on the selection.")
                    continue
                break
                
            while True:
                password = self.__get_input(f"{self.__password_rules()}\nInput Password:")
                if not PasswordFileManager.add_record(username, role, name, email, phone, password):
                    # password provided was invalid, adding user to the record was unsuccessful
                    print("Bad password, please try again")
                    continue
                # valid password input, break out
                break
            
            print(f"Successfully enrolled user with username {username}")

if __name__ == "__main__":
    enroll = EnrollUserInterface()
    enroll.run_interface()