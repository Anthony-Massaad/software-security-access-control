from src.implementation.rbac.roles import Roles
from src.implementation.rbac.permissions import permission_type, Permissions
from src.implementation.rbac.actions import Actions
from typing import Dict
from datetime import datetime

class AccessControl:
    """ Access Control of the system
    """
    
    def __init__(self):
        self.__access_control_matrix:  Dict[Roles, permission_type] = {
            Roles.REGULAR_CLIENT: {
                Permissions.ACCOUNT_BALANCE: [Actions.VIEW],
                Permissions.INVESTMENT_PORTFOLIO: [Actions.VIEW],
                Permissions.FINANCIAL_ADVISOR_CONTACT: [Actions.VIEW],
                Permissions.CLIENT_INFORMATION: [Actions.MODIFY],
                Permissions.REQUEST_SUPPORT: [Actions.SPECIAL]
            },
            Roles.PREMIUM_CLIENT: {
                Permissions.ACCOUNT_BALANCE: [Actions.VIEW],
                Permissions.INVESTMENT_PORTFOLIO: [Actions.VIEW, Actions.MODIFY],
                Permissions.FINANCIAL_ADVISOR_CONTACT: [Actions.VIEW],
                Permissions.FINANCIAL_PLANNER_CONTACT: [Actions.VIEW],
                Permissions.INVESTMENT_ANALYST_CONTACT: [Actions.VIEW],
                Permissions.REQUEST_SUPPORT: [Actions.SPECIAL]
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
        return self.__access_control_matrix.get(role, {})
        
    def enforce_ABAC(self, role: Roles, initial: bool = False):
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
        """Peform access control policy for a specific action and permission of a User

        Args:
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
                    self.__access_control_matrix[role].get(Permissions.ACCOUNT_BALANCE, []).append(Actions.VIEW)
                    self.__access_control_matrix[role].get(Permissions.INVESTMENT_PORTFOLIO, []).append(Actions.VIEW)
            return True        
        print(f"Access denied for {action.value} action on {permission.value} permission")
        return False