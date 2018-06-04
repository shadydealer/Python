from src.queries.database_manager import DataBase
from hashlib import pbkdf2_hmac
from os import urandom


class UserModel:
    def __init__(self):
        self.db = DataBase()

    """
        Returns a row from the user table by the username column.

        @params username- username of the user.

        @return types:
            Tuple containing a row from the user table if the username exists in the table.
            None otherwise. 
    """

    def __fetch_user_by_username(self, *, username):
        return self.db.fetch(tableName='users',
                             constraints=[f'username LIKE \'{username}\''])

    """
        Returns a row from the user table by the password column.

        @params password- password of the user.

        @return types:
            Tuple containing a row from the user table if the password exists in the table.
            None otherwise. 
    """

    def __fetch_user_by_password(self, *, password):
        return self.db.fetch(tableName='users',
                             constraints=[f'password LIKE \'{password}\''])

    """
        Checks if the passed in credentials match any of the user rows in the users table.

        @params username - string. Name of the user.
        @params password - string. User password. 
    """

    def log_in(self, *, username, password):
        user = self.__fetch_user_by_username(username=username)
        if user != None:
            salt = user[2]
            passHash = pbkdf2_hmac('sha256', bytes(password,'utf-8'), bytes(salt,'utf-8'),1)
            if(passHash == user[1]):
                print("Successfully logged in!")
                return True
            else:
                print("Invalid password.")
        else:
            print("Invalid username.")
        return False

    """
        Checks if the passed in username and password exist
        if not a new user is created and added to the db.

        @params username - string. Username of the user.
        @params passwod - string. Pasword of the user. 
    """

    def create_account(self, *, username, password):
        user = self.__fetch_user_by_username(username=username)
        if user == None:
            user = self.__fetch_user_by_password(password=password)
            if user == None:
                salt = urandom(16)

                passHash = pbkdf2_hmac('sha256', bytes(password,'utf-8'), salt, 1)
                self.db.insert(tableName='users',
                               columns=[
                                   'username',
                                   'password',
                                   'salt'
                               ],
                               values=[
                                   username,
                                   passHash,
                                   salt
                               ])
                print("Successful account creation!")
                return True

            else:
                print("Password already in use.")
        else:
            print("Username already in use.")

        return False
