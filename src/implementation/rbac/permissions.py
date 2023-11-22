from enum import Enum
from src.implementation.rbac.actions import Actions
from src.implementation.rbac.roles import Roles
from typing import Dict, List

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