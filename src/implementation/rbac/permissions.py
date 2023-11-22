from enum import Enum
from src.implementation.rbac.actions import Actions
from src.implementation.rbac.roles import Roles
from typing import Dict, List, Optional

class Permissions(Enum):
    """Permissions available for the system
    """
    CLIENT_INFORMATION = "Client_Information"
    ACCOUNT_BALANCE = "Account_Balance"
    INVESTMENT_PORTFOLIO = "Investment_Portfolio"
    FINANCIAL_ADVISOR_CONTACT = "Financial_Advisor_Contact"
    REQUEST_SUPPORT = "Request_Support"
    FINANCIAL_PLANNER_CONTACT = "Financial_Planner_Contact"
    INVESTMENT_ANALYST_CONTACT = "Investment_Analyst_Contact"
    PRIVATE_CONSUMER_INSTRUMENT = "Private_Consumer_Intrament"
    MONEY_MARKET_INSTRUMENT = "Money_Market_Instrument"
    INTEREST_INSTRUMENT = "Interest_Instrument"
    DERIVATIVES_TRADING = "Derivative_Trading"
    REVIEW_SUPPORT_TICKETS = "Review_Support_Tickets"
    VALIDATE_MODIFICATIONS = "Validate_Modifications"

    @classmethod
    def get_permission_by_string(cls, perm: str) -> Optional['Permissions']:
        """retreive an action based on the string provided

        Returns:
            Optional[Actions]: the Action found, otherwise None
        """
        for enum_member in cls:
            if enum_member.value.lower() == perm.lower():
                # Action found
                return enum_member
        return None

# the type definition of the permission
permission_type = Dict[Permissions, List[Actions]]

user_permissions:  Dict[Roles, permission_type] = {
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