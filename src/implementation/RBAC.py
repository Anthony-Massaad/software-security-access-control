from enum import Enum
from typing import Optional
from typing import Dict, List


class Roles(Enum):
    """The Roles of the system
    """
    REGULAR_CLIENT = "Regular Client"
    PREMIUM_CLIENT = "Premium Client"
    FINANCIAL_ADVISOR = "Financial Advisor"
    COMPLIANCE_OFFICER = "Compliance Officer"
    INVESTMENT_ANALYST = "Investment Analyst"
    FINANCIAL_PLANNER = "Financial Planner"
    TECHNICAL_SUPPORT = "Technical Support"
    TELLER = "Teller"
    
    @classmethod
    def to_string(cls) -> str:
        """return a string representation of all the roles to display

        Returns:
            str: the string representation of the roles
        """
        return ', '.join(member.value for member in cls)

    @classmethod
    def get_role_by_name(cls, role: str) -> Optional['Roles']:
        """Retreive a Role enum based on the name

        Returns:
            Optional[Role]: A Role if found, otherwise None
        """
        for enum_member in cls:
            if enum_member.value.lower() == role.lower():
                # Role Found
                return enum_member

        print(f"[ERROR]: get_role_by_name(...) could not find role {role}")
        return None

    @classmethod
    def role_exists(cls, role: str) -> bool:
        """Determine if a role exists

        Args:
            role (str): the role 

        Returns:
            bool: True if a role exists, otherwise False
        """
        for enum_member in cls:
            if enum_member.value.lower() == role.lower():
                # Role Found
                return True
        return False

class Actions(Enum): 
    """The Actions a user can perform
    """
    VIEW = "View"
    MODIFY = "Modify"
    SPECIAL = "Special"

    @classmethod
    def get_action_by_string(cls, action: str) -> Optional['Actions']:
        """retreive an action based on the string provided

        Returns:
            Optional[Actions]: the Action found, otherwise None
        """
        for enum_member in cls:
            if enum_member.value.lower() == action.lower():
                # Action found
                return enum_member
        return None

class Permissions(Enum):
    """Permissions available for the system
    """
    CLIENT_INFORMATION = "Client Information"
    ACCOUNT_BALANCE = "Account Balance"
    INVESTMENT_PORTFOLIO = "Investment Portfolio"
    FINANCIAL_ADVISOR_CONTACT = "Financial Advisor Contact"
    REQUEST_SUPPORT = "Request Support"
    FINANCIAL_PLANNER_CONTACT = "Financial Planner Contact"
    INVESTMENT_ANALYST_CONTACT = "Investment Analyst Contact"
    PRIVATE_CONSUMER_INSTRUMENT = "Private Consumer Intrament"
    MONEY_MARKET_INSTRUMENT = "Money Market Instrument"
    INTEREST_INSTRUMENT = "Interest Instrument"
    DERIVATIVES_TRADING = "Derivative Trading"
    REVIEW_SUPPORT_TICKETS = "Review Support Tickets"
    VALIDATE_MODIFICATIONS = "Validate Modifications"

# the type definition of the permission
permission_type = Dict[Actions, List[Permissions]]

# the user permissions 
user_permissions: Dict[Roles, permission_type] = {
    Roles.REGULAR_CLIENT: {
        Actions.VIEW: [Permissions.ACCOUNT_BALANCE, Permissions.INVESTMENT_PORTFOLIO, Permissions.FINANCIAL_ADVISOR_CONTACT],
        Actions.MODIFY: [Permissions.CLIENT_INFORMATION],
        Actions.SPECIAL: [Permissions.REQUEST_SUPPORT]
    },
    Roles.PREMIUM_CLIENT: {
        Actions.VIEW: [Permissions.ACCOUNT_BALANCE, Permissions.INVESTMENT_PORTFOLIO, 
                   Permissions.FINANCIAL_ADVISOR_CONTACT, Permissions.FINANCIAL_PLANNER_CONTACT, Permissions.INVESTMENT_ANALYST_CONTACT],
        Actions.MODIFY: [Permissions.INVESTMENT_PORTFOLIO],
        Actions.SPECIAL: [Permissions.REQUEST_SUPPORT]
    },
    Roles.FINANCIAL_ADVISOR: {
        Actions.VIEW: [Permissions.ACCOUNT_BALANCE, Permissions.INVESTMENT_PORTFOLIO,
                   Permissions.FINANCIAL_ADVISOR_CONTACT, Permissions.FINANCIAL_PLANNER_CONTACT, Permissions.INVESTMENT_ANALYST_CONTACT,
                   Permissions.PRIVATE_CONSUMER_INSTRUMENT],
        Actions.MODIFY: [Permissions.INVESTMENT_PORTFOLIO, Permissions.FINANCIAL_ADVISOR_CONTACT]
    },
    Roles.FINANCIAL_PLANNER: {
        Actions.VIEW: [Permissions.ACCOUNT_BALANCE, Permissions.INVESTMENT_PORTFOLIO,
                   Permissions.FINANCIAL_ADVISOR_CONTACT, Permissions.FINANCIAL_PLANNER_CONTACT, Permissions.INVESTMENT_ANALYST_CONTACT,
                   Permissions.PRIVATE_CONSUMER_INSTRUMENT, Permissions.MONEY_MARKET_INSTRUMENT],
        Actions.MODIFY: [Permissions.INVESTMENT_PORTFOLIO, Permissions.FINANCIAL_PLANNER_CONTACT]
    },
    Roles.INVESTMENT_ANALYST: {
        Actions.VIEW: [Permissions.ACCOUNT_BALANCE, Permissions.INVESTMENT_PORTFOLIO,
                   Permissions.FINANCIAL_ADVISOR_CONTACT, Permissions.FINANCIAL_PLANNER_CONTACT, Permissions.INVESTMENT_ANALYST_CONTACT,
                   Permissions.PRIVATE_CONSUMER_INSTRUMENT, Permissions.MONEY_MARKET_INSTRUMENT, Permissions.INTEREST_INSTRUMENT,
                   Permissions.DERIVATIVES_TRADING],
        Actions.MODIFY: [Permissions.INVESTMENT_PORTFOLIO, Permissions.INVESTMENT_ANALYST_CONTACT]
    },
    Roles.TELLER: {
        Actions.VIEW: [Permissions.ACCOUNT_BALANCE, Permissions.INVESTMENT_PORTFOLIO, 
                   Permissions.FINANCIAL_ADVISOR_CONTACT, Permissions.FINANCIAL_PLANNER_CONTACT, Permissions.INVESTMENT_ANALYST_CONTACT],
    },
    Roles.TECHNICAL_SUPPORT: {
        Actions.VIEW: [Permissions.CLIENT_INFORMATION],
        Actions.SPECIAL: [Permissions.REVIEW_SUPPORT_TICKETS]
    },
    Roles.COMPLIANCE_OFFICER: {
        Actions.VIEW: [Permissions.INVESTMENT_PORTFOLIO, Permissions.ACCOUNT_BALANCE],
        Actions.SPECIAL: [Permissions.VALIDATE_MODIFICATIONS]
    }
}

