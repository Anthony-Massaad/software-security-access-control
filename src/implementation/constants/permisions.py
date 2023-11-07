from src.implementation.constants.roles import Roles
from src.implementation.constants.actions import Actions
from enum import Enum

class Permissions(Enum):
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

user_permissions = {
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

