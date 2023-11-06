import sys
from src.implementation.constants.roles import Roles
from src.implementation.passwordManager import PasswordManager
import re

class EnrollUserInterface:

    def __init__(self) -> None: 
        self.username = ""
        self.name = ""
        self.email = ""
        self.password = ""
        self.phone = ""
        self.role = ""
    
    def __password_rules(self) -> str:
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
        while True: 
            s = ""
            s = input(f"{prompt} (or 'exit' to quit): ")

            if s.lower() == "exit": 
                print("Exiting Enrolling user")
                sys.exit(1)
                
            if not is_role:
                if re.search(r"\s", s):
                    print("Cannot have spaces")
                    continue
            break
         
        return s

    def run_interface(self):
        print("Enrolling User")
        print("-------------------")
        self.username = self.__get_input("Username")
        self.name = self.__get_input("Name")
        self.email = self.__get_input("Email")
        self.phone = self.__get_input("Phone number")
        
        while True: 
            self.role = self.__get_input(f"Available Roles: {Roles.to_string()}\nRole chosen:", is_role=True)
            if not Roles.role_exists(self.role):
                print("Invalid Role, please type again based on the selection.")
                continue
            break
            
        while True:
            self.password = self.__get_input(f"{self.__password_rules()}\nInput Password:")
            if not PasswordManager.add_record(self.username, self.role, self.name, self.email, self.phone, self.password):
                # password provided was invalid, adding user to the record was unsuccessful
                print("Invalid Password, please try again")
                continue
            # valid password input, break out
            break
        
        print(f"Successfully enroled user with username {self.username}")

if __name__ == "__main__":
    enroll = EnrollUserInterface()
    enroll.run_interface()