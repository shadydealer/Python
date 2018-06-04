from source.controllers.user_controller import UserController
from source.controllers.movie_controller import MovieController
from source.controllers.projection_controller import ProjectionController
from source.controllers.reservation_controller import ReservationController

from datetime import datetime


def main():

    password = 'qwdqwdk'
    username = 'ivan'
    UserController.create_user(username=username, password=password)
    user = UserController.log_in(username=username, password=password)
    print(getattr(user, 'id'))

    rating = 0
    movieName = 'IQDOQD'

    MovieController.add_movie(name=movieName, rating=rating)

    date = datetime.strptime('20180910', '%Y%m%d').date()
    time = datetime.strptime('13:50', '%H:%M').time()

    ProjectionController.add_projection(movieName=movieName,
                      rhsType='3D',
                      rhsDate=date,
                      rhsTime=time)

    ProjectionController.add_projection(movieName=movieName,
                      rhsType='3D',
                      rhsDate=date,
                      rhsTime=time)
    #projDate = date(year=2018, month=9, day=10)
    ProjectionController.print_projection_by_movie_id_and_date(
        movieName=movieName)
    

    ReservationController.make_reservation(user=user,projectionID=1, row=1, col=1)

if __name__ == "__main__":
    main()
