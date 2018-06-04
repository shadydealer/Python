from source.models.models import User, Session
from hashlib import pbkdf2_hmac
from os import urandom


class UserController:
    session = Session()

    @staticmethod
    def __fetch_user_by_username(*, username):
        user = UserController.session.query(User).filter(
            User.username == username).first()
        return user

    @staticmethod
    def __fetch_user_by_password(*, password):
        user = UserController.session.query(User).filter(
            User.password == password).first()
        return user

    @staticmethod
    def log_in(*, username, password):
        user = UserController.__fetch_user_by_username(username=username)
        if user != None:
            passSalt = user.salt
            passHash = pbkdf2_hmac('sha256', bytes(
                password, 'utf-8'), passSalt, 1)

            user = UserController.__fetch_user_by_password(password=passHash)

            if user != None:
                print("Login successful.")
                return user

        print("Invalid credentials.")
        return None

    @staticmethod
    def create_user(*, username, password):
        user = UserController.__fetch_user_by_username(username=username)
        if user == None:
            salt = urandom(16)
            hashedPassword = pbkdf2_hmac(
                'sha256', bytes(password, 'utf-8'), salt, 1)
            UserController.session.add(
                User(username=username, password=hashedPassword, salt=salt))
            UserController.session.commit()
            print("Account creation was successful!")
            return UserController.log_in(username=username, password=password)

        print("Username is already in use.")
        return None
