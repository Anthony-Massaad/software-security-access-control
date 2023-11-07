
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
    
    def get_available_actions(self) -> str:
        s = ""
        for action, permissions in self.permissions.items():
            action_text = action.value
            permissions_text = ", ".join([f"{index + 1}: {perm.value}" for index, perm in enumerate(permissions)])
            s+=f"{action_text}: {permissions_text}\n"
        return s

    def __repr__(self) -> str:
        return f"Role: {self.role.value} \n Permisions: {self.permissions}"