from src.queries.database_manager import DataBase

MOVIE_TABLE_NAME = 'Movies'


class MovieModel:
    def __init__(self):
        self.db = DataBase()

    def create(self, name, rating):
        self.db.insert(tableName=MOVIE_TABLE_NAME,
                       columns=['name', 'rating'],
                       values=[name, rating])

    def show_movie_projections(self, id, date=None):
        data = self.db.joined_fetch(mainTableName='Movies',
                                    columns=['movie_id',
                                             'date',
                                             'time'],
                                    joinTypes=['JOIN'],
                                    otherTables=['projections'],
                                    newTableNames=['t1'],
                                    on=['t1.movie_id=movies.id'],
                                    constraints=([f'date = \'{date}\'::date'] if date != None else None))
        print(data)
