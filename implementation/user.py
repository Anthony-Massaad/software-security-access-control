from constants.roles import Roles
from implementation.accessControl import AccessControl

class User:
    
    def __init__(self, username: str, name: str, email: str, phone: str, role: Roles):
        self.username = username
        self.name = name 
        self.email = email
        self.phone = phone
        self.grantAccess = False
        self.role = AccessControl.grantRole(role)

    def __repr__(self) -> str:
        return 'User:\n username: ' + self.username + " | name: " + self.name + "\n" + "email: " + self.email + " | phone: " + self.phone