import sqlite3

def execute_and_commit(*,dbName,query):
    connection = sqlite3.connect(dbName)
    curs = connection.cursor()
    
    curs.execute(query)
    connection.commit()
    
    connection.close()

def execute_and_fetch(*,dbName, query):
    connection = sqlite3.connect(dbName)
    curs = connection.cursor()

    curs.execute(query)
    connection.commit()

    row = curs.fetchone()
    connection.close()

    return row



