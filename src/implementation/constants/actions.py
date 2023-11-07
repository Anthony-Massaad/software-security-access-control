from enum import Enum

class Actions(Enum): 
    VIEW = "View"
    MODIFY = "Modify"
    SPECIAL = "Special"

    @classmethod
    def valid_action(cls, action: str) -> bool:
        for enum_member in cls:
            if enum_member.value.lower() == action.lower():
                return True
        return False