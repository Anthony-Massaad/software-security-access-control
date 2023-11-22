from enum import Enum
from typing import Optional

class Actions(Enum): 
    """The Actions a user can perform
    """
    VIEW = "View"
    MODIFY = "Modify"
    SPECIAL = "Special"