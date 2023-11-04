from constants.roles import Roles
from constants.actions import Actions
from enum import Enum

class Permissions(Enum):
    CLIENT_INFORMATION = "Client Information"
    ACCOUNT_BALANCE = "account_balance"
    INVESTMENT_PORTFOLIO = "investment_portfolio"
    FINANCIAL_ADVISOR_CONTACT = "financial_advisor_contact"
    REQUEST_SUPPORT = "request_support"
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
        Actions.VIEW: set([Permissions.CLIENT_INFORMATION, Permissions.ACCOUNT_BALANCE, Permissions.INVESTMENT_PORTFOLIO, 
                   Permissions.FINANCIAL_ADVISOR_CONTACT]),
        Actions.MODIFY: set([Permissions.CLIENT_INFORMATION]),
        Actions.SPECIAL: set([Permissions.REQUEST_SUPPORT])
    },
    Roles.PREMIUM_CLIENT: {
        Actions.VIEW: set([Permissions.CLIENT_INFORMATION, Permissions.ACCOUNT_BALANCE, Permissions.INVESTMENT_PORTFOLIO, 
                   Permissions.FINANCIAL_ADVISOR_CONTACT, Permissions.FINANCIAL_PLANNER_CONTACT, Permissions.INVESTMENT_ANALYST_CONTACT]),
        Actions.MODIFY: set([Permissions.CLIENT_INFORMATION, Permissions.INVESTMENT_PORTFOLIO]),
        Actions.SPECIAL: set([Permissions.REQUEST_SUPPORT])
    },
    Roles.FINANCIAL_ADVISOR: {
        Actions.VIEW: set([Permissions.CLIENT_INFORMATION, Permissions.ACCOUNT_BALANCE, Permissions.INVESTMENT_PORTFOLIO,
                   Permissions.FINANCIAL_ADVISOR_CONTACT, Permissions.FINANCIAL_PLANNER_CONTACT, Permissions.INVESTMENT_ANALYST_CONTACT,
                   Permissions.PRIVATE_CONSUMER_INSTRUMENT]),
        Actions.MODIFY: set([Permissions.INVESTMENT_PORTFOLIO, Permissions.FINANCIAL_ADVISOR_CONTACT])
    },
    Roles.FINANCIAL_PLANNER: {
        Actions.VIEW: set([Permissions.CLIENT_INFORMATION, Permissions.ACCOUNT_BALANCE, Permissions.INVESTMENT_PORTFOLIO,
                   Permissions.FINANCIAL_ADVISOR_CONTACT, Permissions.FINANCIAL_PLANNER_CONTACT, Permissions.INVESTMENT_ANALYST_CONTACT,
                   Permissions.PRIVATE_CONSUMER_INSTRUMENT, Permissions.MONEY_MARKET_INSTRUMENT]),
        Actions.MODIFY: set([Permissions.INVESTMENT_PORTFOLIO, Permissions.FINANCIAL_PLANNER_CONTACT])
    },
    Roles.INVESTMENT_ANALYST: {
        Actions.VIEW: set([Permissions.CLIENT_INFORMATION, Permissions.ACCOUNT_BALANCE, Permissions.INVESTMENT_PORTFOLIO,
                   Permissions.FINANCIAL_ADVISOR_CONTACT, Permissions.FINANCIAL_PLANNER_CONTACT, Permissions.INVESTMENT_ANALYST_CONTACT,
                   Permissions.PRIVATE_CONSUMER_INSTRUMENT, Permissions.MONEY_MARKET_INSTRUMENT, Permissions.INTEREST_INSTRUMENT,
                   Permissions.DERIVATIVES_TRADING]),
        Actions.MODIFY: set([Permissions.INVESTMENT_PORTFOLIO, Permissions.INVESTMENT_ANALYST_CONTACT])
    },
    Roles.TELLER: {
        Actions.VIEW: set([Permissions.CLIENT_INFORMATION, Permissions.ACCOUNT_BALANCE, Permissions.INVESTMENT_PORTFOLIO, 
                   Permissions.FINANCIAL_ADVISOR_CONTACT, Permissions.FINANCIAL_PLANNER_CONTACT, Permissions.INVESTMENT_ANALYST_CONTACT]),
    },
    Roles.TECHNICAL_SUPPORT: {
        Actions.VIEW: set([Permissions.CLIENT_INFORMATION, Permissions.FINANCIAL_ADVISOR_CONTACT, Permissions.FINANCIAL_PLANNER_CONTACT, 
                   Permissions.INVESTMENT_ANALYST_CONTACT]),
        Actions.SPECIAL: set([Permissions.REVIEW_SUPPORT_TICKETS])
    },
    Roles.COMPLIANCE_OFFICER: {
        Actions.VIEW: set([Permissions.CLIENT_INFORMATION, Permissions.INVESTMENT_PORTFOLIO]),
        Actions.SPECIAL: set([Permissions.VALIDATE_MODIFICATIONS])
    }
}

