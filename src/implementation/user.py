from src.implementation.accessControl import AccessControl
from src.implementation.RBAC import Roles

class User:
    
    def __init__(self, username: str, name: str, email: str, phone: str, role: Roles) -> None:
        self.username = username
        self.name = name 
        self.email = email
        self.phone = phone
        self.role = AccessControl.grant_role(role)

    def __repr__(self) -> str:
        s = 'User:\n username: ' + self.username + " | name: " + self.name + "\n" + "email: " + self.email + " | phone: " + self.phone
        return s