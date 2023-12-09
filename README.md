# software-security-access-control

## Description 

Access Control implementaiton for Finvest Holdings user authentication. Through Role-Based Access control (RBAC), allow users to use the system based on their role. The system also allows for enrollment of users authenticated through a password policy. Attribute-Based Access Control (ABAC) is also used to verify restrictions as users use the system and upon signing in. 

### Password Policy
Password is valid if it:
- is between 8-12 characters long
- includes at least one upper case letter
- includes at least one numeric digit
- includes one special character from the set {!, @, #, $, %, ?, ∗}
- does not match your username/user_id
- does not match a liscense plate
- does not match some date format (i.e., dd/mm/yyyy or d/m/yy)
- does not match a phone number
- is not considered a weak password

### ABAC Policy
- Teller role can only access the system between 9am-5pm

## Usage
Requires Python 3.8 or greater to run the program. 
1. Go to the folder root directory (one before src)
2. Open the command prompt or terminal within that directory
3. On the command line, type one of the following:

### Run the Interface
`python3 user_interface.py` 

Select 'e' to enroll a user, or 'l' to login as a user.

### Run all the tests
`python3 -m unittest src/tests/test_*.py`

## Credit
Anthony Massaad
