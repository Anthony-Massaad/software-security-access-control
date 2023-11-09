import sys
from src.implementation.passwordManager import PasswordManager
from src.implementation.accessControl import AccessControl
from src.implementation.constants.actions import Actions
from src.implementation.constants.permisions import Permissions

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
                    continue
                # is a valid user, system accessed
                print("Successful Log in\n")
            else:
                print("Incorrect username or password. Try again")
                continue
        
            print(f"Welcome {user.username}")
            print("Note: all inputs from here are not case sensitive")
            # User can perform some actions
            while True: 
                # while logged in
                print("Actions Available:")
                print("---------------------")
                print(user.role.get_available_actions())

                val = input("Type an action (examples: view 0, modify 1) or 'exit' to quit ('sign out' to log out): ")
                if val.lower() == "exit":
                    print("Logging out and exiting!")
                    sys.exit(0)

                if val.lower() == "sign out":
                    break
                
                # validate the input
                split_input = val.split(" ")
                
                # validate number of inputs
                if len(split_input) >= 3:
                    print("Too many inputs")
                    continue
                
                # validate action selection
                action = split_input[0]
                enum_action = Actions.get_action_by_string(action)
                if not enum_action:
                    print("invalid action selected")
                    continue

                if not user.role.has_action(enum_action):
                    print(f"You don't have action {enum_action.value} rights")
                    continue
                
                permission = split_input[1]
                try:
                    permission = int(permission)
                except:
                    print("Invalid permission, has to be a number")
                    continue
                
                if not user.role.verify_permission_index(enum_action, permission - 1):
                    print("invalid permision selected")
                    continue

                print()                                    
                AccessControl.perform_access_control_policy(user, enum_action, user.role.get_permission_by_index(enum_action, permission - 1))
                print()
            




if __name__ == "__main__":
    interface = LoginUserInterface()
    interface.run_interface()