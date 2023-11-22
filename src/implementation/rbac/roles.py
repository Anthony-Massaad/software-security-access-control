from enum import Enum
from typing import Optional

class Roles(Enum):
    """The Roles of the system
    """
    REGULAR_CLIENT = "Regular_Client"
    PREMIUM_CLIENT = "Premium_Client"
    FINANCIAL_ADVISOR = "Financial_Advisor"
    COMPLIANCE_OFFICER = "Compliance_Officer"
    INVESTMENT_ANALYST = "Investment_Analyst"
    FINANCIAL_PLANNER = "Financial_Planner"
    TECHNICAL_SUPPORT = "Technical_Support"
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





