import sqlite3
from queries.sqlite3_handler import execute_and_fetch

"""
    A class that is used to select/fetch from given database.
"""
class Fetcher:
    def __init__(self, *, dbName):
        self.dbName = dbName

    """
        Fetches a row from the database by given columns.

        @return value:
            Tuple containg the row data from the table.
    """

    def fetch_row(self, *, tableName, columnsAndValues):
        GET_ROW_SQL = f'''
        SELECT * FROM {tableName}
        WHERE {'OR '.join([f'{k} LIKE "%{v}%"' for k,v in columnsAndValues.items()])}; 
        '''
        return execute_and_fetch(dbName=self.dbName, query=GET_ROW_SQL)
