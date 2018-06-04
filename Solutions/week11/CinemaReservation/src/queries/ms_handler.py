#import sqlite3
import psycopg2

"""
    Executes and commits a query that makes changes to the dbName.

    @params dbName - name of the database we're altering.
    @params query - query we're executing.  
"""
def execute_and_commit(*, dbName, query,values=None):

    connection = psycopg2.connect(f'dbname={dbName}')
    curs = connection.cursor()

    curs.execute(query,values)
    connection.commit()

    connection.close()


"""
    Executes a fetch query and returns a tuple containing the returned row. 
    
    @params dbName - name of the database we're peeking in.
    @params query- query we're executing.
"""
def execute_and_fetch(*, dbName, query):
    connection = psycopg2.connect(f'dbname={dbName}')
    curs = connection.cursor()

    curs.execute(query)
    connection.commit()

    row = curs.fetchone()
    connection.close()

    return row
