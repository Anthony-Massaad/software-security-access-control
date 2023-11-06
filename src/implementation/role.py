
from src.implementation.constants.roles import Roles
from src.implementation.constants.permisions import Permissions
from src.implementation.constants.actions import Actions

class Role:

    def __init__(self, role: Roles, permisions = {}) -> None:
        self.role = role
        self.permissions = permisions

    def has_permision(self, action: Actions, permision: Permissions) -> bool:
        if (self.permissions.get(action)):
            for perm in self.permissions.get(action):
                if perm == permision:
                    return True
        return False
    
    def print_permisions_of_action(self, action: Actions) -> str:
        s = ""
        for perm in self.permissions[action]:
            s += f"{perm.value}, "
        return s

    def __repr__(self) -> str:
        return f"Role: {self.role.value} \n Permisions: {self.permissions}"