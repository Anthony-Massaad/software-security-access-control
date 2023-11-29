import unittest
from src.implementation.accessControl import AccessControl
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
        print("testing enforce_ABAC(...)")
        print()
        is_between_hours = True
        curr_time = datetime.now()
        curr_hour = curr_time.hour
        if curr_hour < 9 or curr_hour > 16:
            is_between_hours = False
        
        for role in Roles: 
            if role != Roles.TELLER:
                actual_result = self.ac.enforce_ABAC(role)
                print(f"Testing ABAC on Role {role.value} -> Expected: {True}, Actual: {actual_result}")
                self.assertTrue(actual_result)
            else:
                print("Testing ABAC on Teller using real time")
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
        for role in Roles:
            for permission in Permissions:
                for action in Actions:
                    perms = self.ac.get_permissions(role)
                    expected = action in perms.get(permission, {})
                    permision_granted = self.ac.perform_access_control_policy(role, action, permission)
                    print(f"Test access control of role {role.value} trying to {action.value} perform on {permission.value}")
                    print(f"Expected {expected}, Actual: {permision_granted}")
                    if expected: self.assertTrue(permision_granted)
                    else: self.assertFalse(permision_granted)
        print("-----------------------")
