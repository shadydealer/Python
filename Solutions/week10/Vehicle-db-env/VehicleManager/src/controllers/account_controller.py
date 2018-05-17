from controllers.user_controller import UserValidator, User
from queries.inserter import Inserter

"""
    A class that will be used to control logins and account creation.
"""


class AccountController:

    def __init__(self, *, dbName):
        self.dbName = dbName
        self.validator = UserValidator(dbName=dbName)
        self.user = User(dbName=dbName)

    """
        Checks the database to see if a user with
        the specified username and password exists.

        @return value:
            True if the account name and password exist and match the same user.
            False otherwise.
    """

    def login(self, *, username, password):
        valid_User = self.validator.validate_login(username=username,
                                                   password=password)

        if valid_User:
            print("Log in was successful.")
            return True

        print("Invalid login.")
        return False

    """
        Creates a new user by given
        username, password, email, phoneNumber and address.

        @return value:
            True if no account with the same username, password or email exists.
            False otherwise.
    """

    def create_account(self, *, userType, username, password,
                       email, phoneNumber, address):
        valid_User = self.validator.validate_account_creation(username=username,
                                                              password=password,
                                                              email=email)
        if valid_User:
            self.user.create_user(userType=userType, username=username, password=password,
                                  email=email, phoneNumber=phoneNumber, address=address
                                  )
            print("Account was successfully created!")
            return True
        return False
