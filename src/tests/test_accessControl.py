import unittest
from src.implementation.accessControl import AccessControl
from src.implementation.user import User
from src.implementation.constants.roles import Roles
from src.implementation.constants.permisions import Permissions
from src.implementation.constants.actions import Actions
from datetime import datetime

class TestAccessControl(unittest.TestCase):
    print("Testing AccessControl class")
    print("---------------------------")

    def test_valid_grant_role(self) -> None:
        print("testing grant_role(...) by passing valid roles:")
        teller_role = AccessControl.grant_role(Roles.TELLER)
        print(f"Getting Teller from grant role -> Expected: {Roles.TELLER.value} Acutal: {teller_role.role.value}")
        self.assertEqual(teller_role.role, Roles.TELLER)
        compliance_role = AccessControl.grant_role(Roles.COMPLIANCE_OFFICER)
        print(f"Getting Teller from grant role -> Expected: {Roles.COMPLIANCE_OFFICER.value} Acutal: {compliance_role.role.value}")
        self.assertEqual(compliance_role.role, Roles.COMPLIANCE_OFFICER)
        print()
    
    def test_invalid_grant_role(self) -> None:
        print("testing grant_role(...) by passing invalid roles:")
        random_role = AccessControl.grant_role(None)
        print(f"Getting an unknown role from grant role -> Expected: {None} Acutal: {random_role}")
        self.assertIsNone(random_role)
        print()

    def test_enforce_ABAC(self) -> None: 
        print("testing enforce_ABAC(...) using real time")
        is_between_hours = True
        curr_time = datetime.now()
        curr_hour = curr_time.hour
        if curr_hour < 9 or curr_hour > 16:
            is_between_hours = False
        user = User("tony", "tony", 'tony@gmai.com', "23432", Roles.TELLER)
        actual_result = AccessControl.enforce_ABAC(user)
        if is_between_hours:
            print(f"user is Within hours -> Expected: {is_between_hours}, Actual: {actual_result}")
            self.assertTrue(actual_result)
        else:
            print(f"user is not Within hours -> Expected: {is_between_hours}, Actual: {actual_result}")
            self.assertFalse(actual_result)
        print()

    def test_access_control_policy(self) -> None: 
        print("Testing access_control_policy(...)")
        user = User("tony", "tony", 'tony@gmai.com', "23432", Roles.TELLER)
        permision_granted = AccessControl.perform_access_control_policy(user, Actions.VIEW, Permissions.CLIENT_INFORMATION)
        print("Test User Teller with view permision on client information.")
        print(f"Teller's view Permisions: {user.role.print_permisions_of_action(Actions.VIEW)}")
        print(f"Expected: True, Acutal: {permision_granted}")
        self.assertTrue(permision_granted)

        user = User("tony", "tony", 'tony@gmai.com', "23432", Roles.COMPLIANCE_OFFICER)
        permision_granted = AccessControl.perform_access_control_policy(user, Actions.SPECIAL, Permissions.VALIDATE_MODIFICATIONS)
        print(f"Test User Compliance Officer with special permision on {Permissions.VALIDATE_MODIFICATIONS.value}")
        print(f"Compliance Officer Special Permisions: {user.role.print_permisions_of_action(Actions.SPECIAL)}")
        print(f"Expected: True, Acutal: {permision_granted}")

        user = User("tony", "tony", 'tony@gmai.com', "23432", Roles.PREMIUM_CLIENT)
        permision_granted = AccessControl.perform_access_control_policy(user, Actions.VIEW, Permissions.VALIDATE_MODIFICATIONS)
        print(f"Test Premium User with view permision on {Permissions.VALIDATE_MODIFICATIONS.value}")
        print(f"Premium User View Permisions: {user.role.print_permisions_of_action(Actions.VIEW)}")
        print(f"Expected: False, Acutal: {permision_granted}")

        self.assertFalse(permision_granted)
        print()
