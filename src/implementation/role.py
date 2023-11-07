
from src.implementation.constants.roles import Roles
from src.implementation.constants.permisions import Permissions
from src.implementation.constants.actions import Actions

class Role:

    def __init__(self, role: Roles, permisions = {}) -> None:
        self.role = role
        self.permissions = permisions

    def verify_permission_index(self, action: Actions, perm_index: int) -> bool:
        perm_lst = self.permissions[action]
        if perm_index < 0 or perm_index >= len(perm_lst): return False
        return True
    
    def get_available_actions(self) -> str:
        s = ""
        for action, permissions in self.permissions.items():
            action_text = action.value
            permissions_text = ", ".join([f"({index + 1}) {perm.value}" for index, perm in enumerate(permissions)])
            s+=f"{action_text}: {permissions_text}\n"
        return s

    def get_permission_by_index(self, action:Actions, perm_index: int) -> Permissions:
        return self.permissions[action][perm_index]

    def has_action(self, action: Actions) -> bool:
        return bool(self.permissions.get(action))

    def get_action(self, action: Actions) -> Actions:
        return self.permissions[action]

    def __repr__(self) -> str:
        return f"Role: {self.role.value} \n Permisions: {self.permissions}"