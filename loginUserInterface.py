import sys
from src.implementation.passwordManager import PasswordManager
from src.implementation.accessControl import AccessControl
from src.implementation.constants.actions import Actions

class LoginUserInterface:

    def __get_input(self, prompt: str) -> str:
        while True: 
            s = ""
            s = input(f"{prompt} (or 'exit' to quit): ")

            if s.lower() == "exit": 
                print("Exiting Enrolling user")
                sys.exit(1)
                
            break
         
        return s

    def run_interface(self) -> None:
        print("Log In")
        print("-----------")
        user = None
        while True:
            # handle sign in
            username = self.__get_input("Enter Username")
            password = self.__get_input("Enter Password")
            user = PasswordManager.retrieve_record(username, password)

            if user:
                if not AccessControl.enforce_ABAC(user):
                    # enforce the abac rule on the user to determine if they can access the system
                    # use case, the user is a teller and the system is only accessed between 9-5 for tellers
                    print("Hello fellow Teller, System hours is between 9am-5pm only. Thank you.")
                    sys.exit(0)
                # is a valid user, system accessed
                print("Successful Log in\n")
                break
            else:
                print("Incorrect username or password. Try again")
        
        print(f"Welcome {user.username}")
        print("Note: all inputs from here are not case sensitive")
        # User can perform some actions
        while True: 
            # while logged in
            print("Actions Available:")
            print("---------------------")
            print(user.role.get_available_actions())

            val = input("Type an action (examples: view 0, modify 1) or exit to log out: ")
            if val.lower() == "exit":
                print("Logging out!")
                break

            split_input = val.split(" ")
            
            if len(split_input) >= 3:
                print("Too many inputs")
                continue



if __name__ == "__main__":
    interface = LoginUserInterface()
    interface.run_interface()