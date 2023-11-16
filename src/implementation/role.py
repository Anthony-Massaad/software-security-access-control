from src.implementation.rbac.roles import Roles
from src.implementation.rbac.permissions import Permissions, permission_type
from src.implementation.rbac.actions import Actions
from typing import List

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

    def verify_permission_index(self, action: Actions, perm_index: int) -> bool:
        """Ensure no index out of bounds given an index

        Args:
            action (Actions): The Action to perform
            perm_index (int): the index of the desired permission

        Returns:
            bool: True if valid index, otherwise False
        """
        perm_lst = self.permissions[action]
        if perm_index < 0 or perm_index >= len(perm_lst): return False
        return True
    
    def get_available_actions(self) -> str:
        """Get a string reperesentation of the available action and respective permissions

        Returns:
            str: the string rerpesentation of the available action and respective permission
        """
        s = ""
        for action, permissions in self.permissions.items():
            action_text = action.value
            permissions_text = ", ".join([f"({index + 1}) {perm.value}" for index, perm in enumerate(permissions)])
            s+=f"{action_text}: {permissions_text}\n"
        return s

    def get_permission_by_index(self, action: Actions, perm_index: int) -> Permissions:
        """Retrieve a permission based on the index

        Args:
            action (Actions): the Action performed
            perm_index (int): the permission index

        Returns:
            Permissions: the Permission of an action
        """
        return self.permissions[action][perm_index]

    def has_action(self, action: Actions) -> bool:
        """the role has the Action provided

        Args:
            action (Actions): the Action

        Returns:
            bool: True if the Role has the desired Action, otherwise False
        """
        return bool(self.permissions.get(action))

    def get_action(self, action: Actions) -> Actions:
        """Retrieve the set of permissions associated with the specified Action

        Args:
            action (Actions): The desired Action

        Returns:
            Actions: the set of permissions
        """
        return self.permissions[action]

    def elevate_permission(self, action: Actions, elevated_permissions: List[Permissions]) -> None:
        """Elevate a Role's Action permissions

        Args:
            action (Actions): The Action to elevate
            elevated_permissions (List[Permissions]): a list of permissions to add
        """
        if not self.has_action(action):
            # action does not exist yet, make it
            self.permissions[action] = elevated_permissions
            return
        # append new permissions to the current list of permissions for the action
        self.permissions[action] = self.permissions[action] + elevated_permissions

    def __repr__(self) -> str:
        """To string method for the print of Role

        Returns:
            str: the string to show
        """
        return f"Role: {self.role.value} \n Permisions: {self.permissions}"