import unittest
from src.implementation.accessControl import AccessControl
from src.implementation.user import User
from src.implementation.rbac.roles import Roles
from src.implementation.rbac.permissions import Permissions
from src.implementation.rbac.actions import Actions
from datetime import datetime

class TestAccessControl(unittest.TestCase):

    def setUp(self):
        self.ac = AccessControl()

    def test_enforce_ABAC(self) -> None: 
        print()
        print("-----------------------")
        print("testing enforce_ABAC(...) using real time")
        print()
        is_between_hours = True
        curr_time = datetime.now()
        curr_hour = curr_time.hour
        if curr_hour < 9 or curr_hour > 16:
            is_between_hours = False
        actual_result = self.ac.enforce_ABAC(Roles.TELLER, initial=True)
        if is_between_hours:
            print(f"user is Within hours -> Expected: {is_between_hours}, Actual: {actual_result}")
            self.assertTrue(actual_result)
        else:
            print(f"user is not Within hours -> Expected: {is_between_hours}, Actual: {actual_result}")
            self.assertFalse(actual_result)
        print("-----------------------")

    def test_access_control_policy(self) -> None: 
        print()
        print("-----------------------")
        print("Testing access_control_policy(...)")
        print()
        permision_granted = self.ac.perform_access_control_policy(Roles.TELLER, Actions.VIEW, Permissions.CLIENT_INFORMATION)
        print("Test User Teller with view permision on client information.")
        print(f"Expected: True, Acutal: {permision_granted}")
        self.assertFalse(permision_granted)

        permision_granted = self.ac.perform_access_control_policy(Roles.COMPLIANCE_OFFICER, Actions.SPECIAL, Permissions.VALIDATE_MODIFICATIONS)
        print(f"Test User Compliance Officer with special permision on {Permissions.VALIDATE_MODIFICATIONS.value}")
        print(f"Expected: True, Acutal: {permision_granted}")

        permision_granted = self.ac.perform_access_control_policy(Roles.PREMIUM_CLIENT, Actions.VIEW, Permissions.VALIDATE_MODIFICATIONS)
        print(f"Test Premium User with view permision on {Permissions.VALIDATE_MODIFICATIONS.value}")
        print(f"Expected: False, Acutal: {permision_granted}")

        self.assertFalse(permision_granted)
        print("-----------------------")
