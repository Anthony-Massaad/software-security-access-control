from __future__ import annotations # necessary to use TYPE_CHECKING with annotations and not strings
from src.implementation.role import Role
from src.implementation.RBAC import Roles, Permissions, user_permissions, Actions
from typing import TYPE_CHECKING, List, Optional
from datetime import datetime

if TYPE_CHECKING:
    # required for typing without circular imports
    # A special constant that is assumed to be True by 3rd party static type checkers. It is False at runtime.
    from src.implementation.user import User

class AccessControl:
    """ Access Control of the system
    """
    __roles: List[Role] = [
        Role(Roles.REGULAR_CLIENT, user_permissions[Roles.REGULAR_CLIENT]),
        Role(Roles.PREMIUM_CLIENT, user_permissions[Roles.PREMIUM_CLIENT]),
        Role(Roles.FINANCIAL_ADVISOR, user_permissions[Roles.FINANCIAL_ADVISOR]),
        Role(Roles.FINANCIAL_PLANNER, user_permissions[Roles.FINANCIAL_PLANNER]),
        Role(Roles.INVESTMENT_ANALYST, user_permissions[Roles.INVESTMENT_ANALYST]),
        Role(Roles.TELLER, user_permissions[Roles.TELLER]),
        Role(Roles.TECHNICAL_SUPPORT, user_permissions[Roles.TECHNICAL_SUPPORT]),
        Role(Roles.COMPLIANCE_OFFICER, user_permissions[Roles.COMPLIANCE_OFFICER])
    ]

    __modifications: List[User] = []
    __support_tickets: List[User] = []
    
    @classmethod
    def grant_role(cls, role: Roles) -> Optional[Role]:
        """Grant a role based on the role input provided

        Args:
            role (Roles): the role desired

        Returns:
            Optional[Role]: the Role is found, otherwise None
        """
        for defined_role in cls.__roles:
            if role == defined_role.role:
                # Role found
                return defined_role
        # Role not found      
        print("[ERROR] Could not determine Role")
        return None

    @classmethod
    def enforce_ABAC(cls, user: User) -> bool:
        """Enforce ABAC policy on the system to define authorization and restrictions.

        Args:
            user (User): the User to enforce ABAC policy on

        Returns:
            bool: True if the User passed the ABAC policy, otherwise False
        """
        curr_time = datetime.now()
        curr_hour = curr_time.hour
        if user.role.role == Roles.TELLER:
            # enforce time restriction to the teller between 9am-5pm
            if curr_hour < 9 or curr_hour > 16:
                print("Hello fellow Teller, System hours is between 9am-5pm only. Thank you.")
                return False
        return True

    @classmethod
    def perform_access_control_policy(cls, user: User, action: Actions, permission: Permissions) -> bool:
        """Peform access control policy for a specific action and permission of a User

        Args:
            user (User): the User
            action (Actions): the specified Action
            permission (Permissions): the specified Permission

        Returns:
            bool: True if access control was performed, otherwise False
        """
        if not user.role.get_action(action):
            # deny user access if they don't have action permission
            print(f"ACCESS DENIED FOR ACTIONS {action.value}")
            return False

        if action == Actions.VIEW:
            for perm in user.role.get_action(action):
                if perm == permission:
                    print(f"ACCESS GRANTED FOR VIEWING {permission.value}")
                    return True
            print(f"ACCESS DENIED FOR VIEWING {permission.value}")
        elif action == Actions.MODIFY:
            for perm in user.role.get_action(action):
                if perm == permission:
                    print(f"ACCESS GRANTED FOR MODIFYING {permission.value}")
                    if perm == Permissions.INVESTMENT_PORTFOLIO:
                        # investment portfolio's modification CAN be verified by compliance officer's
                        print(f"MODIFYING {permission.value} CAN BE VERIFIED BY A COMPIANCE OFFICER")
                        cls.__modifications.append(user)
                        return True
            print(f"ACCESS DENIED FOR MODIFYING {permission.value}")
        elif action == Actions.SPECIAL:
            if permission == Permissions.REQUEST_SUPPORT:
                # request support can only be done by clients and premium clients
                if user.role.role == Roles.PREMIUM_CLIENT or user.role.role == Roles.REGULAR_CLIENT:
                    print("Permissions granted to request support")
                    cls.__support_tickets.append(user)
                    return True
                print(f"ACCESS DENIED FOR SPECIAL PERMISSION {permission.value}")
            elif permission == Permissions.VALIDATE_MODIFICATIONS:
                # modifications to invest portfolios can only be validated by compliance officer's
                if user.role.role == Roles.COMPLIANCE_OFFICER:
                    if not cls.__modifications:
                        # no modifications done yet
                        print("NO MODIFICATIONS TO INVESTMENT PORTFOLIO'S TO VERIFY")
                        return True
                    
                    while cls.__modifications:
                        # while there are modifications to be verified, continue to verify 
                        mod_user = cls.__modifications.pop()
                        print(f"Changes made by {mod_user.name} to portfolio verified")

                    return True
            elif permission == Permissions.REVIEW_SUPPORT_TICKETS:
                if user.role.role == Roles.TECHNICAL_SUPPORT:
                    if not cls.__support_tickets:
                        # no support requests done yet
                        print("NO SUPPORT TICKETS TO REIVEW")
                        return True
                    # assuming the client will agree to the request for their information 
                    while cls.__support_tickets:
                        supp_user = cls.__support_tickets.pop()
                        print(f"REVIEWING SUPPORT REQUESTED BY {supp_user.username}")
                    
                    # elevate the tech_support permissions
                    user.role.elevate_permission(Actions.VIEW, [Permissions.ACCOUNT_BALANCE, Permissions.INVESTMENT_PORTFOLIO])
                    return True
        return False