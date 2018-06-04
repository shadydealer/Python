
from src.queries.database_manager import DataBase
from src.models.movie_model import MovieModel
from src.models.users_model import UserModel
from os import urandom

DATABASE_NAME = 'cinema'


def main():

    userModel = UserModel()
    username = "qdkqo"
    password = "wqodkwq`"

    userModel.log_in(username=username,
                     password=password)


"""     userModel.create_account(username=username,
                             password=password)
"""



if __name__ == "__main__":
    main()
