
from constants.roles import Roles
from constants.permisions import Permissions
from constants.actions import Actions

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