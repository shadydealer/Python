from source.models.models import Movie, Session


class MovieController:
    session = Session()

    @staticmethod
    def fetch_movie_by_name(*, name):
        return MovieController.session.query(Movie).filter(Movie.name.like(name)).first()

    @staticmethod
    def show_movies():
        for movie in MovieController.session.query(Movie).order_by(Movie.rating.desc()).all():
            print(movie.name, ' ', movie.rating)

    @staticmethod
    def add_movie(*, name, rating):
        movie = MovieController.fetch_movie_by_name(name=name)
        if movie == None:
            MovieController.session.add(Movie(name=name, rating=rating))
            MovieController.session.commit()
            print("Successfully added {}.".format(name))
        else:
            print("{} already exists in the database.".format(name))
