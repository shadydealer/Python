from queries.fetcher import Fetcher
from queries.inserter import Inserter

ALREADY_IN_USE_STR = "The {} you've provided is already in use."
USER_TABLE = 'BaseUser'

"""
    A class that is used to validate logins and user creations.
"""


class UserValidator:

    def __init__(self, *, dbName):
        self.dbName = dbName
        self.fetch = Fetcher(dbName=dbName)

    """
        Checks if the passed in password
        matches the password in the database
        associated with the user.

        @return value:
            True if the password matches the user password.
            False otherwise.
    """

    def __validate_password(self, *, password, user):
        return password == user[2]

    """
        Checks if the login credentials are valid. 

        @return value:
            True if the user exists in the database and the password matches the user.
            False if the user does not exist or if the password doesn't match the user.
    """

    def validate_login(self, *, username, password):
        user = self.fetch.fetch_row(
            tableName=USER_TABLE,
            columnsAndValues={
                'user_name': f'{username}'
            })

        if user != None:
            if self.__validate_password(password=password, user=user):
                return True

        return False

    """
        Checks if the username already exists in the database.

        @return value:
            True if the username exists.
            False otherwise. 
    """

    def __username_is_taken(self, *, username):
        user = self.fetch.fetch_row(
            tableName=USER_TABLE,
            columnsAndValues={
                'user_name': f'{username}'
            }
        )
        if user != None:
            print(ALREADY_IN_USE_STR.format('username'))
            return True
        return False

    """
        Checks if the password already exists in the database.

        @return value:
            True if the password exists.
            False otherwise. 
    """

    def __password_is_taken(self, *, password):
        user = self.fetch.fetch_row(
            tableName=USER_TABLE,
            columnsAndValues={
                'password': f'{password}'
            }
        )
        if user != None:
            print(ALREADY_IN_USE_STR.format('password'))
            return True
        return False

    """
        Checks if the email already exists in the database.

        @return value:
            True if the email exists.
            False otherwise. 
    """

    def __email_is_taken(self, *, email):
        user = self.fetch.fetch_row(
            tableName=USER_TABLE,
            columnsAndValues={
                'email': f'{email}'
            }
        )
        if user != None:
            print(ALREADY_IN_USE_STR.format('email'))
            return True
        return False

    """
        Checks if any of the parameters exist
        in the database.

        @return value:
            True if none of the values exist in the database.
            False if any of the values exist in the database.
    """

    def validate_account_creation(self, *, username, password, email):
        if self.__username_is_taken(username=username):
            return False
        if self.__password_is_taken(password=password):
            return False
        if self.__email_is_taken(email=email):
            return False
        return True


"""
    A class that will be used to create new entries into the database.
"""

MECHANIC_TABLE = 'mechanic'
CLIENT_TABLE = 'client'


class User:
    def __init__(self, *, dbName):
        self.dbName = dbName
        self.inserter = Inserter(dbName=dbName)
        self.fetcher = Fetcher(dbName=dbName)

    """
        Inserts a new mechanic into the mechanic table. 
    """
    def __create_mechanic(self, *, id):
        self.inserter.insert(tableName=MECHANIC_TABLE,
                             columnsAndValues={'base_id': id})
    
    """
        Inserts a new client into the client table. 
    """
    def __create_client(self, *, id):
        self.inserter.insert(tableName=CLIENT_TABLE,
                             columnsAndValues={'base_id': id})

    """
        Adds a new user to the user table and also adds a mechanic or a client
        to their respective tables if depending on the type parameter value. 
    """
    def create_user(self, *, userType, username, password,
                    email, phoneNumber, address):
        userDict = {
            'user_name': username,
            'password': password,
            'email': email,
            'phone_number': phoneNumber,
            'address': address
        }
        self.inserter.insert(tableName=USER_TABLE, columnsAndValues=userDict)

        user = self.fetcher.fetch_row(tableName=USER_TABLE,columnsAndValues={'user_name':username})
        print(user)
        if userType == 'client':
            self.__create_client(id=user[0])
        
        elif userType == 'mechanic':
            self.__create_mechanic(id=user[0])
        