from src.implementation.rbac.roles import Roles

class User:
    """The System User
    """
    def __init__(self, username: str, name: str, email: str, phone: str, role: Roles) -> None:
        """User Constructor

        Args:
            username (str): the username/user_id
            name (str): the name of the user
            email (str): the email of the user
            phone (str): the number of the user
            role (Roles): the specified Role for the user
        """
        self.username = username
        self.name = name 
        self.email = email
        self.phone = phone
        self.role = role

    def __repr__(self) -> str:
        """To string method to print the user

        Returns:
            str: to string of User
        """
        return f"username: {self.username}, name: {self.name}, email: {self.email}, phone: {self.phone}, role: {self.role.value}"