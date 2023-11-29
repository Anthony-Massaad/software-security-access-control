from src.implementation.rbac.roles import Roles
from src.implementation.rbac.permissions import permission_type, Permissions
from src.implementation.rbac.actions import Actions
from typing import Dict
from datetime import datetime

class AccessControl:
    """ Access Control of the system
    """
    
    def __init__(self):
        """Default constructor for AccessControl
        """
        self.__access_control_matrix:  Dict[Roles, permission_type] = {
            Roles.REGULAR_CLIENT: {
                Permissions.ACCOUNT_BALANCE: [Actions.VIEW],
                Permissions.INVESTMENT_PORTFOLIO: [Actions.VIEW],
                Permissions.FINANCIAL_ADVISOR_CONTACT: [Actions.VIEW],
                Permissions.CLIENT_INFORMATION: [Actions.MODIFY]
            },
            Roles.PREMIUM_CLIENT: {
                Permissions.ACCOUNT_BALANCE: [Actions.VIEW],
                Permissions.INVESTMENT_PORTFOLIO: [Actions.VIEW, Actions.MODIFY],
                Permissions.FINANCIAL_ADVISOR_CONTACT: [Actions.VIEW],
                Permissions.FINANCIAL_PLANNER_CONTACT: [Actions.VIEW],
                Permissions.INVESTMENT_ANALYST_CONTACT: [Actions.VIEW]
            },
            Roles.FINANCIAL_ADVISOR: {
                Permissions.ACCOUNT_BALANCE: [Actions.VIEW],
                Permissions.INVESTMENT_PORTFOLIO: [Actions.VIEW, Actions.MODIFY],
                Permissions.FINANCIAL_ADVISOR_CONTACT: [Actions.VIEW, Actions.MODIFY],
                Permissions.FINANCIAL_PLANNER_CONTACT: [Actions.VIEW],
                Permissions.INVESTMENT_ANALYST_CONTACT: [Actions.VIEW],
                Permissions.PRIVATE_CONSUMER_INSTRUMENT: [Actions.VIEW]
            },
            Roles.FINANCIAL_PLANNER: {
                Permissions.ACCOUNT_BALANCE: [Actions.VIEW],
                Permissions.INVESTMENT_PORTFOLIO: [Actions.VIEW, Actions.MODIFY],
                Permissions.FINANCIAL_ADVISOR_CONTACT: [Actions.VIEW],
                Permissions.FINANCIAL_PLANNER_CONTACT: [Actions.VIEW, Actions.MODIFY],
                Permissions.INVESTMENT_ANALYST_CONTACT: [Actions.VIEW],
                Permissions.PRIVATE_CONSUMER_INSTRUMENT: [Actions.VIEW],
                Permissions.MONEY_MARKET_INSTRUMENT: [Actions.MODIFY]
            },
            Roles.INVESTMENT_ANALYST: {
                Permissions.ACCOUNT_BALANCE: [Actions.VIEW],
                Permissions.INVESTMENT_PORTFOLIO: [Actions.VIEW, Actions.MODIFY],
                Permissions.FINANCIAL_ADVISOR_CONTACT: [Actions.VIEW],
                Permissions.FINANCIAL_PLANNER_CONTACT: [Actions.VIEW],
                Permissions.INVESTMENT_ANALYST_CONTACT: [Actions.VIEW, Actions.MODIFY],
                Permissions.PRIVATE_CONSUMER_INSTRUMENT: [Actions.VIEW],
                Permissions.MONEY_MARKET_INSTRUMENT: [Actions.VIEW],
                Permissions.INTEREST_INSTRUMENT: [Actions.VIEW],
                Permissions.DERIVATIVES_TRADING: [Actions.MODIFY]
            },
            Roles.TELLER: {
                Permissions.ACCOUNT_BALANCE: [Actions.VIEW],
                Permissions.INVESTMENT_PORTFOLIO: [Actions.VIEW],
                Permissions.FINANCIAL_ADVISOR_CONTACT: [Actions.VIEW],
                Permissions.FINANCIAL_PLANNER_CONTACT: [Actions.VIEW],
                Permissions.INVESTMENT_ANALYST_CONTACT: [Actions.VIEW]
            },
            Roles.TECHNICAL_SUPPORT: {
                Permissions.CLIENT_INFORMATION: [Actions.VIEW],
                Permissions.REVIEW_SUPPORT_TICKETS: [Actions.SPECIAL]
            },
            Roles.COMPLIANCE_OFFICER: {
                Permissions.INVESTMENT_PORTFOLIO: [Actions.VIEW],
                Permissions.ACCOUNT_BALANCE: [Actions.VIEW],
                Permissions.VALIDATE_MODIFICATIONS: [Actions.SPECIAL]
            }
        }
    
    def get_permissions(self, role: Roles) -> permission_type:
        """Get the permissions dictionary based on role

        Args:
            role (Roles): the role 

        Returns:
            permission_type: the columns of permissions and their associates actions
        """
        return self.__access_control_matrix.get(role, {})
        
    def enforce_ABAC(self, role: Roles, initial: bool = False) -> bool:
        """Enforce the ABAC policy on a given role

        Args:
            role (Roles): the role
            initial (bool, optional): True if the ABAC enforcement is on intial login. Defaults to False.

        Returns:
            _type_: True if ABAC passed, otherwise False
        """
        if initial:
            # on sign in, enforce abac
            if role == Roles.TELLER:
                curr_time = datetime.now()
                curr_hour = curr_time.hour
                # enforce time restriction to the teller between 9am-5pm
                if curr_hour < 9 or curr_hour > 16:
                    print("Hello fellow Teller, System hours is between 9am-5pm only. Thank you.")
                    return False
        return True

    def perform_access_control_policy(self, role: Roles, action: Actions, permission: Permissions) -> bool:
        """Peform access control policy for a specific action and permission of a role

        Args:
            role (Rles): the Role
            action (Actions): the specified Action
            permission (Permissions): the specified Permission

        Returns:
            bool: True if access control was performed, otherwise False
        """
        if not self.enforce_ABAC(role):
            # enforce abac on every access control performance
            # not needed but if more ABAC policies were added that are not on intiial sign in, 
            # this would be necessary
            return False
        
        if action in self.__access_control_matrix.get(role, {}).get(permission, []):
            print(f"Access granted for {action.value} action on {permission.value} permission")
            if role == Roles.TECHNICAL_SUPPORT:
                if permission == Permissions.REVIEW_SUPPORT_TICKETS:
                    print(f"reviewing support tickets. Role Elevated")
                    # elevate the tech_support permissions
                    self.__access_control_matrix[role][Permissions.ACCOUNT_BALANCE] = [Actions.VIEW]
                    self.__access_control_matrix[role][Permissions.INVESTMENT_PORTFOLIO] = [Actions.VIEW]
            return True        
        print(f"Access denied for {action.value} action on {permission.value} permission")
        return False