from src.implementation.rbac.roles import Roles
from src.implementation.rbac.permissions import Permissions, permission_type
from src.implementation.rbac.actions import Actions
from typing import List, Union

class Role:
    """Role class for RBAC (has a set of permissions)
    """

    def __init__(self, role: Roles, permisions: permission_type = {}) -> None:
        """Constructor

        Args:
            role (Roles): the Role
            permisions (permission_type, optional): The set of permissions for the Role. Defaults to {}.
        """
        self.role = role
        self.permissions = permisions

    def has_access(self, permission: Permissions, action: Actions) -> bool:
        """Verify the permission and action is within the role's access

        Args:
            permission (Permissions): the permission to access
            action (Actions): the action for the permissions

        Returns:
            bool: true if granted, otherwise false 
        """
        if self.permissions.get(permission):
            for action_granted in self.permissions[permission]:
                if action == action_granted:
                    return True
        return False
    
    def get_available_access(self) -> str:
        s = ""
        for perm, lst_actions in self.permissions.items():
            perm_text = perm.value
            action_text = ", ".join([f"({index}) {action.value}" for index, action in enumerate(lst_actions)])
            s += f"{perm_text}: {action_text}\n"
        return s