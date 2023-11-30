import unittest
import os
from src.implementation.passwordFileManager import PasswordFileManager
from src.implementation.rbac.roles import Roles

class TestPasswordFileManager(unittest.TestCase):

    def setUp(self) -> None:
        self.usernames = ["Tony", "Anthony", "Max", "Bardi"]
        self.passwords = ["Hd2332@@3", "PassS21@", "jdDs211#", "mMna!232"]
        self.roles = [Roles.TELLER.value, 
                      Roles.COMPLIANCE_OFFICER.value, 
                      Roles.FINANCIAL_PLANNER.value, 
                      Roles.REGULAR_CLIENT.value]
    
    def test_add_record(self):
        # remove the add record password file before making a new one 
        # basically, fresh slate for adding records tests
        file_test_path = "src/tests/test_passwd_add.txt"
        if os.path.exists(file_test_path):
            os.remove(file_test_path)

        pFM = PasswordFileManager(file_test_path)
        print()
        print("------------------")
        print("Testing the adding of record to the src/tests/test_passwd_add.txt")
        # Testing unique usernames
        for i, username in enumerate(self.usernames):
            expected = pFM.add_record(username, self.roles[i], username, "email", "phonenumber", self.passwords[i])
            print(f"Adding record for username {username} --> Expected: {True}, Actual: {expected}")
            self.assertTrue(expected)
        # Testing adding a duplicate username
        expected = pFM.add_record("Tony", Roles.TELLER.value, "tony_username", "email", "phonenumber", "password")
        print(f"Adding duplicate username 'Tony' --> Expected: {False}, actual {expected}")
        self.assertFalse(expected)
    
    def test_retreive_records(self):
        file_test_path = "src/tests/test_passwd_retrieve.txt" 
        pFM = PasswordFileManager(file_test_path)
        # remove password file for the retrieve record test if it's there
        # basically, fresh slate for adding records tests
        if os.path.exists(file_test_path):
            os.remove(file_test_path)
        # populate the retrieve_record_file for the tests
        for i, username in enumerate(self.usernames):
            pFM.add_record(username, self.roles[i], username, "email", "phonenumber", self.passwords[i])
        print()
        print("----------------------")
        print("Testing the retrieve of records")
        print()
        #retrieving valid users
        for i, username in enumerate(self.usernames):
            user = pFM.retrieve_record(username, self.passwords[i])
            print(f"Retrieving user {username}, Expected: Not Null, Actual\n{user}")
            self.assertTrue(user)
        # retrieving a none exsistent user
        expected = pFM.retrieve_record("invalid_user", "password")
        print(f"retrieving invalid user with username 'invalid_user' --> Expected: {None}, actual {expected}")
        # retrieving a user with valid username but incorrect password
        expected = pFM.retrieve_record(self.usernames[0], "password")
        print(f"retrieving correct user with username {self.usernames[0]} but incorrect password --> Expected: {None}, actual {expected}")
        # retrieving a user with invalid username but correct password
        expected = pFM.retrieve_record("invalid_user", self.passwords[0])
        print(f"retrieving invalid user with username 'invalid_user' but correct password {self.passwords[0]} --> Expected: {None}, actual {expected}")
            

    
    # def test_check_password(self):
    #     print()
    #     print("-----------------------")
    #     print("Testing valid_passowrd(...)")
    #     print()
    #     username = "Tony2@859!"

    #     success = self.pFM.valid_password(username, "hD53dj!85")
    #     print(f"Testing a valid password 'hD53dj!85' with username '{username}' -> Expected: True, Actual {success}")
    #     self.assertTrue(success)

    #     success = self.pFM.valid_password(username, "hD53dj@85224fgsdaf")
    #     print(f"Testing a password with too many characters 'hD53dj@85224fgsdaf' with username '{username}' -> Expected: False, Actual {success}")
    #     self.assertFalse(success)

    #     success = self.pFM.valid_password(username, "hD53dj @85")
    #     print(f"Testing a password with whitespace 'hD53dj @85' with username '{username}' -> Expected: False, Actual {success}")
    #     self.assertFalse(success)

    #     success = self.pFM.valid_password(username, "hD53dj85D")
    #     print(f"Testing a password with no special characters 'hD53dj85D' with username '{username}' -> Expected: False, Actual {success}")
    #     self.assertFalse(success)

    #     success = self.pFM.valid_password(username, "hDddsdj@ppS")
    #     print(f"Testing a password with no numbers 'hDddsdj@ppS' with username '{username}' -> Expected: False, Actual {success}")
    #     self.assertFalse(success)

    #     success = self.pFM.valid_password(username, "hd53dj@85")
    #     print(f"Testing a password with no uppercase characters 'hd53dj@85' with username '{username}' -> Expected: False, Actual {success}")
    #     self.assertFalse(success)

    #     success = self.pFM.valid_password(username, "hJ!85")
    #     print(f"Testing a password with too little characters 'hJ!85' with username '{username}' -> Expected: False, Actual {success}")
    #     self.assertFalse(success)

    #     success = self.pFM.valid_password(username, username)
    #     print(f"Testing a password with the same username '{username}' with username '{username}' -> Expected: False, Actual {success}")
    #     self.assertFalse(success)

    #     success = self.pFM.valid_password(username, "Tony@03/3/22")
    #     print(f"Testing a password with date format 'Tony@03/3/22' with username '{username}' -> Expected: False, Actual {success}")
    #     self.assertFalse(success)

    #     success = self.pFM.valid_password(username, "To@KXX123")
    #     print(f"Testing a password with license plate format 'To@KXx123' with username '{username}' -> Expected: False, Actual {success}")
    #     self.assertFalse(success)

    #     success = self.pFM.valid_password(username, "T@6132225555")
    #     print(f"Testing a password with phone-number format 'T@6132225555' with username '{username}' -> Expected: False, Actual {success}")
    #     self.assertFalse(success)

    #     success = self.pFM.valid_password(username, "PaASsword@1")
    #     print(f"Testing a password with common password 'PaASsword@1' with username '{username}' -> Expected: False, Actual {success}")
    #     self.assertFalse(success)
    #     print("-----------------------")
