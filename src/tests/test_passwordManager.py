import unittest
from src.implementation.passwordFileManager import PasswordFileManager

class TestPasswordFileManager(unittest.TestCase):
    
    def setUp(self):
        self.pFM = PasswordFileManager()
    
    def test_check_password(self):
        print()
        print("-----------------------")
        print("Testing valid_passowrd(...)")
        print()
        username = "Tony2@859!"

        success = self.pFM.valid_password(username, "hD53dj!85")
        print(f"Testing a valid password 'hD53dj!85' with username '{username}' -> Expected: True, Actual {success}")
        self.assertTrue(success)

        success = self.pFM.valid_password(username, "hD53dj@85224fgsdaf")
        print(f"Testing a password with too many characters 'hD53dj@85224fgsdaf' with username '{username}' -> Expected: False, Actual {success}")
        self.assertFalse(success)

        success = self.pFM.valid_password(username, "hD53dj @85")
        print(f"Testing a password with whitespace 'hD53dj @85' with username '{username}' -> Expected: False, Actual {success}")
        self.assertFalse(success)

        success = self.pFM.valid_password(username, "hD53dj85D")
        print(f"Testing a password with no special characters 'hD53dj85D' with username '{username}' -> Expected: False, Actual {success}")
        self.assertFalse(success)

        success = self.pFM.valid_password(username, "hDddsdj@ppS")
        print(f"Testing a password with no numbers 'hDddsdj@ppS' with username '{username}' -> Expected: False, Actual {success}")
        self.assertFalse(success)

        success = self.pFM.valid_password(username, "hd53dj@85")
        print(f"Testing a password with no uppercase characters 'hd53dj@85' with username '{username}' -> Expected: False, Actual {success}")
        self.assertFalse(success)

        success = self.pFM.valid_password(username, "hJ!85")
        print(f"Testing a password with too little characters 'hJ!85' with username '{username}' -> Expected: False, Actual {success}")
        self.assertFalse(success)

        success = self.pFM.valid_password(username, username)
        print(f"Testing a password with the same username '{username}' with username '{username}' -> Expected: False, Actual {success}")
        self.assertFalse(success)

        success = self.pFM.valid_password(username, "Tony@03/3/22")
        print(f"Testing a password with date format 'Tony@03/3/22' with username '{username}' -> Expected: False, Actual {success}")
        self.assertFalse(success)

        success = self.pFM.valid_password(username, "To@KXX123")
        print(f"Testing a password with license plate format 'To@KXx123' with username '{username}' -> Expected: False, Actual {success}")
        self.assertFalse(success)

        success = self.pFM.valid_password(username, "T@6132225555")
        print(f"Testing a password with phone-number format 'T@6132225555' with username '{username}' -> Expected: False, Actual {success}")
        self.assertFalse(success)

        success = self.pFM.valid_password(username, "PaASsword@1")
        print(f"Testing a password with common password 'PaASsword@1' with username '{username}' -> Expected: False, Actual {success}")
        self.assertFalse(success)
        print("-----------------------")
