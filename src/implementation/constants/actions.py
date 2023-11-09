from enum import Enum
from typing import Optional

class Actions(Enum): 
    VIEW = "View"
    MODIFY = "Modify"
    SPECIAL = "Special"

    @classmethod
    def get_action_by_string(cls, action: str) -> Optional['Actions']:
        for enum_member in cls:
            if enum_member.value.lower() == action.lower():
                return enum_member
        return None