from enum import Enum

class Roles(Enum):
    REGULAR_CLIENT = "Regular Client"
    PREMIUM_CLIENT = "Premium Client"
    FINANCIAL_ADVISOR = "Financial Advisor"
    COMPLIANCE_OFFICER = "Compliance Officer"
    INVESTMENT_ANALYST = "Investment Analyst"
    FINANCIAL_PLANNER = "Financial Planner"
    TECHNICAL_SUPPORT = "Technical Support"
    TELLER = "Teller"

    @classmethod
    def get_role_by_name(cls, role: str):
        for enum_member in cls:
            if enum_member.value.lower() == role.lower():
                return enum_member

        print(f"[ERROR]: get_role_by_name(...) could not find role {role}")
        return None

    @classmethod
    def role_exists(cls, role: str) -> bool:
        for enum_member in cls:
            if enum_member.value.lower() == role.lower():
                return True
        return False
    
    