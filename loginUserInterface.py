import sys
from src.implementation.passwordFileManager import PasswordFileManager
from src.implementation.accessControl import AccessControl
from src.implementation.RBAC import Actions

class LoginUserInterface:
    """The login interface
    """
    def __get_input(self, prompt: str) -> str:
        """Get the input from the user

        Args:
            prompt (str): The prompt to display to the user

        Returns:
            str: the user input
        """
        while True: 
            s = ""
            s = input(f"{prompt} (or 'exit' to quit): ")

            if s.lower() == "exit": 
                print("Exiting Enrolling user")
                sys.exit(1)
                
            break
         
        return s

    def run_interface(self) -> None:
        """User interface for login and other actions in the system
        """
        print("Log In")
        print("-----------")
        user = None
        while True:
            # handle sign in
            username = self.__get_input("Enter Username")
            password = self.__get_input("Enter Password")
            user = PasswordFileManager.retrieve_record(username, password)

            if user:
                if not AccessControl.enforce_ABAC(user):
                    # enforce the abac rule on the user to determine if they can access the system
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