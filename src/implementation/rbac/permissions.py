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

