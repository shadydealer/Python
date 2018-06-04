from source.models.models import Movie, Projection, Session
from source.controllers.movie_controller import MovieController
from datetime import datetime

YIELDED_ROWS_COUNT = 1024


class ProjectionController:
    session = Session()

    @staticmethod
    def fetch_projection(*, movieID, movieType, projectionDate, projectionTime):
        """
            Fetches a single projection from the database.

            @param values movieID - id of the movie.
            @param values movieType - type of the movie.
            @param values projectionDate - date of the projection.
            @param values projectionTime - time of the projection.

            @param types movieID -integer.
            @param types movieType - string.
            @param types projectionDate - date.
            @param types projectionTime - time.

            @return type:
                Projection object if  there's a row with the given values.
                None otherwise.
        """
        return ProjectionController.session.query(Projection).filter(
            Projection.movie_id == movieID,
            Projection.type.like(movieType),
            Projection.date == projectionDate,
            Projection.time == projectionTime
        ).first()

    @staticmethod
    def add_projection(*, movieName, rhsType, rhsDate, rhsTime):
        """
            Adds a projection by given movie name to the database
            if the movie is in the database.

            @param values movieName - name of the movie we want to add a projection of.
            @param values rhsType - type of the movie.
            @param values rhsDate - date of the projection.
            @param values rhstime - time of the projection.

            @param types movieName - string.
            @param types rhsType - string.
            @param types rhsDate - date.
            @param types rhstime - time.

        """
        movie = MovieController.fetch_movie_by_name(name=movieName)
        if movie != None:
            projection = ProjectionController.fetch_projection(movieID=movie.id,
                                                               movieType=rhsType,
                                                               projectionDate=rhsDate,
                                                               projectionTime=rhsTime)
            if projection == None:
                movie.projections.append(Projection(
                    movie_id=movie.id, type=rhsType, date=rhsDate, time=rhsTime))

                MovieController.session.commit()
                print(
                    "Successfully added {} projection at {}-{}.".format(movieName, rhsDate, rhsTime))
            else:
                print("Projection already exists.")
        else:
            print("{} does not exists in the database.".format(movieName))

    @staticmethod
    def print_projection_by_movie_id_and_date(*, movieName, date=None):
        """
            Prints all projections of a specific movie by its id
            for a specific date(date is optional).

            @param values movie_id - id of the movie.
            @param values date - date for which we want to list projections.

            @param types movie_id - integer.
            @param types date- date.
        """

        if date != None:
            projections = ProjectionController.session.query(
                Movie.name, Projection.time).join(Projection).filter(Projection.date == date).yield_per(YIELDED_ROWS_COUNT)
        else:
            projections = ProjectionController.session.query(
                Movie.name, Projection.time).join(Projection).yield_per(YIELDED_ROWS_COUNT)

        for projection in projections:
            print(projection[0], ' ', projection[1])
