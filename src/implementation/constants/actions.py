from enum import Enum

class Actions(Enum): 
    VIEW = "View"
    MODIFY = "Modify"
    SPECIAL = "Special"

    @classmethod
    def get_action_by_string(cls, action: str):
        for enum_member in cls:
            if enum_member.value.lower() == action.lower():
                return enum_member
        return None