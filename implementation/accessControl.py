from implementation.role import Role
from implementation.user import User
from constants.roles import Roles
from constants.permisions import user_permissions, Permissions
from constants.actions import Actions
from datetime import datetime
from sys import exit

# we will be using RBAC to handle role accessing 
# we will also be using ABAC to handle operational control handling for the Teller
class AccessControl:

    __regular_client_role = Role(Roles.REGULAR_CLIENT, user_permissions[Roles.REGULAR_CLIENT])
    __premium_client_role = Role(Roles.PREMIUM_CLIENT, user_permissions[Roles.PREMIUM_CLIENT])
    __financial_advisor_role = Role(Roles.FINANCIAL_ADVISOR, user_permissions[Roles.FINANCIAL_ADVISOR])
    __financial_planner_role = Role(Roles.FINANCIAL_PLANNER, user_permissions[Roles.FINANCIAL_PLANNER])
    __investment_analyst_role = Role(Roles.INVESTMENT_ANALYST, user_permissions[Roles.INVESTMENT_ANALYST])
    __teller_role = Role(Roles.TELLER, user_permissions[Roles.TELLER])
    __technical_support_role = Role(Roles.TECHNICAL_SUPPORT, user_permissions[Roles.TECHNICAL_SUPPORT])
    __compliance_officer_role = Role(Roles.COMPLIANCE_OFFICER, user_permissions[Roles.COMPLIANCE_OFFICER])

    __modifications = []
    __accountAccessGranted = []
    
    @classmethod
    def grantRole(cls, role: Roles) -> Role:
        if role == Roles.REGULAR_CLIENT: return cls.__regular_client_role
        elif role == Roles.PREMIUM_CLIENT: return cls.__premium_client_role
        elif role == Roles.FINANCIAL_ADVISOR: return cls.__financial_advisor_role
        elif role == Roles.FINANCIAL_PLANNER: return cls.__financial_planner_role
        elif role == Roles.INVESTMENT_ANALYST: return cls.__investment_analyst_role
        elif role == Roles.TELLER: return cls.__teller_role
        elif role == Roles.TECHNICAL_SUPPORT: return cls.__technical_support_role
        elif role == Roles.COMPLIANCE_OFFICER: return cls.__compliance_officer_role
        
        print("[ERROR] Could not determine Role")
        exit(1)

    @classmethod
    def enforce_ABAC(cls, user: User) -> bool:
        curr_time = datetime.now()
        curr_hour = curr_time.hour
        if user.role.role == Roles.TELLER:
            # enforce time restriction to the teller between 9am-5pm
            if curr_hour < 9 or curr_hour > 16:
                print("Hello fellow Teller, System hours is between 9am-5pm only.")
                return False
        return True

    @classmethod
    def perform_access_control_policy(cls, user: User, action: Actions, permission: Permissions) -> bool: 
        if (user.role.has_permision(action, permission)):
            print("ACCCESS GRANTED")
            return True
        print("No Access")
        return False