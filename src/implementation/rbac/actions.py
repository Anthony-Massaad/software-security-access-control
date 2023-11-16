from enum import Enum
from typing import Optional

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