import sqlite3
from queries.sqlite3_handler import execute_and_commit

"""
    A class that is used to insert values into a table by given database.
"""
class Inserter:
    def __init__(self,*,dbName):
        self.dbName = dbName
    
    """
        Inserts a row with given values into the passed in table. 
    """
    def insert(self,*,tableName,columnsAndValues):
        columns_str = ''
        values_str=''
        for k, v in columnsAndValues.items():
            columns_str += f'{k},\n'
            values_str +=f'"{v}",\n'
        
        columns_str = columns_str[:-2]
        values_str = values_str[:-2]

        INSERT_ROW_SQL=\
        f'''
INSERT INTO {tableName}(
{columns_str}
)
VALUES(
{values_str}
);
        '''
        print(INSERT_ROW_SQL)
        execute_and_commit(dbName=self.dbName,query=INSERT_ROW_SQL)
