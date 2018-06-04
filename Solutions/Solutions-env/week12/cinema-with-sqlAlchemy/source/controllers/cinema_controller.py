from source.controllers.movie_controller import MovieController
from source.controllers.projection_controller import ProjectionController
from source.controllers.user_controller import UserController
from source.controllers.reservation_controller import ReservationController


class CinemaController:

    @staticmethod
    def show_movies():
        MovieController.show_movies()
    