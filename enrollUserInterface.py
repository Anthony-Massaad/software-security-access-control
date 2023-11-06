import sys
from src.implementation.constants.roles import Roles
from src.implementation.passwordManager import PasswordManager

class EnrollUserInterface:

    def __init__(self) -> None: 
        self.username = ""
        self.name = ""
        self.email = ""
        self.password = ""
        self.phone = ""
        self.role = ""
    
    def __get_input(self, prompt: str, is_role: bool = False) -> str:
        while True: 
            s = ""
            s = input(f"{prompt} (or 'exit' to quit): ")

            if s.lower() == "exit": 
                print("Exiting Enrolling user")
                sys.exit(1)

            if is_role and not Roles.role_exists(s):
                print("Invalid Role, please type again based on the selection.")
                continue

            if s.strip():
                # final check, there is no whitespace in the input
                break

        return s

    def run_interface(self):
        print("Enrolling User")
        print("-------------------")
        self.username = self.__get_input("Username")
        self.name = self.__get_input("Name")
        self.email = self.__get_input("Email")
        self.phone = self.__get_input("Phone number")
        self.role = self.__get_input("Role", True)

        while True:
            self.password = self.__get_input("Password")
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