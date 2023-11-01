import re

class Password:
    # in regex, \d is any digit from 0 to 9, so match any numeric digit
    # .*? indicates match any character before the specified statement
    # Initial pattern for the password complexity requirements
    # (?=.*[A-Z]) specifies at least 1 upper case letter
    # (?=.*[a-z]) specifies at least 1 lower case letter
    # (?=.*\d) specifies at least 1 numerical digit
    # (?=.*[!@#$%?∗]) specifies at least one special character defined in the [...]
    # (?!.*\s) indicates no white space included
    # {8,12} indicates the password must be 8-12 length long inclusive
    __password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%?∗])(?!.*\s).{8,12}$"
    # List of prohibited formats (e.g., calendar dates, license plate numbers, phone numbers)
    # .*?(?=\d{1,2}/\d{1,2}/\d{2,4}): This pattern matches dates in the format of "dd/mm/yyyy" or "d/m/yy." ignores anything before and after
    # (?:[A-Z]{3,4}(?:-|)?[0-9]{3,4})|(?:[0-9]{3,4}(?:-|)?[A-Z]{3,4}): This pattern matches sequences that start with one to three uppercase letters followed by one to six digits.
    # .*?(?=\d{10,11}): This pattern matches sequences of 10 or 11 consecutive digits
    __prohibited_formats = [r".*?(?=\d{1,2}/\d{1,2}/\d{2,4})", r"(?:[A-Z]{3,4}(?:-|)?[0-9]{3,4})|(?:[0-9]{3,4}(?:-|)?[A-Z]{3,4})", r".*?(?=\d{10,11})"]
    __common_passwords = ["PaASsword@1", "Qwerty#@123", "Qaz12!3wsx"] # tpm
    
    @classmethod
    def valid_password(cls, user_id: str, password: str) -> bool:
        is_common_password = any([bool(re.match(password, x, re.IGNORECASE)) for x in cls.__common_passwords]) # needs to be false
        valid_pattern = bool(re.match(cls.__password_pattern, password)) # needs to be true
        invalid_format = any([bool(re.match(x, password)) for x in cls.__prohibited_formats]) # needs to be false
        eq_username_password = bool(re.match(f".*?(?={re.escape(user_id)})", password)) # needs to be false
        return valid_pattern and not invalid_format and not eq_username_password and not is_common_password


if __name__ == "__main__":
    # testing purposes
    print("Password main Testing")
    password = "hD53dj!85"
    password2 = "hD53dj@85224fgsdaf"
    password3 = "hD53dj @85"
    password4 = "hD53dj85"
    password5 = "hDddsdj@pp"
    password6 = "hd53dj@85"
    password7 = "hj!85"
    userid = "Tony2@859!"
    password8 = "Tony2@859!"
    pro1 = "Tony@03/3/22"
    pro2 = "KXx123"
    pro3 = "T6132225555"
    common = "PaASsword@1"
    common2 = "paassword@1"

    print("Valid password: ", Password.valid_password("any", password))
    print("Invalid password with too many characters: ", Password.valid_password("a", password2))
    print("Invalid password with whitespace: ", Password.valid_password("a", password3))
    print("Invalid password with no special characters: ", Password.valid_password("a", password4))
    print("Invalid password with no numbers: ", Password.valid_password("a", password5))
    print("Invalid password with no uppercase: ", Password.valid_password("a", password6))
    print("Invalid password with too little characters: ", Password.valid_password("a", password7))
    print("Invalid password with the same userID: ", Password.valid_password(userid, password8))
    print("Invalid password with date format: ", Password.valid_password(userid, pro1))
    print("Invalid password with license plate: ", Password.valid_password(userid, pro2))
    print("Invalid password with phonenumber: ", Password.valid_password(userid, pro3))
    print("Invalid password with common password 1: ", Password.valid_password(userid, common))
    print("Invalid password with common password 2: ", Password.valid_password(userid, common2))