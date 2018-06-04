# import sqlite3
import psycopg2
from src.queries.ms_handler import execute_and_commit, execute_and_fetch


AUTOINCREMENT_SERIAL = 'SERIAL'
DATABASE_NAME = 'cinema'


class Column:
    def __init__(self, *,
                 columnName, columnType,
                 autoincrement=False, isNullable=True,
                 isForeignKey=False, references=''):

        self.columnName = columnName
        self.columnType = columnType
        self.autoincrement = autoincrement
        self. isNullable = isNullable
        self.isForeignKey = isForeignKey
        self. references = references

    def nullable(self):
        return 'NOT NULL' if not self.isNullable else ''

    def autoinc(self):
        return f'{AUTOINCREMENT_SERIAL}' if self.autoincrement else ''

    def foreign_key(self):
        if self.isForeignKey:
            return f',\nFOREIGN KEY({self.columnName}) REFERENCES {self.references}(ID)'
        return ''

    def generate_column_creation_query(self):
        return f'''{self.columnName} {self.columnType} {self.nullable()} {self.autoinc()}'''


class DataBase:
    def __init__(self):
        self.dbName = DATABASE_NAME

    """
        Generates an sql string that joins tables.

        @params joinTypes- list of strings. The join that's going to be executed (left outer, right outer, etc).
        @params tables - list of strings. The tables you're joining.
        @params on - list of strings. Which columns they're about to be joined on.
                     If there are multiple columns that the tables need to be joined on,
                     the string must be in the following format:
                     (<first_table_column1_name>=<second_table_column1_name> and
                      <first_table_column2_name>=<second_table_column2_name>)
        @params newTableNames- list of the names of the joined tables.
    """

    def __joined_fetch_clause(self, joinTypes, tables, newTableNames, on):
        temp = '\n'.join(
            [f'{comb[0]} {comb[1]}  AS {comb[2]} ON {comb[3]}' for comb in zip(
                joinTypes, tables, newTableNames, on)]
        )
        return temp

    """
        Creates a table in the database with specific columns.

        @params tableName - name of the table which we're creating.
        @params columns - the columns of the table which we're creating.
    """

    def create_table(self, *, tableName, columns):
        foreign_key_string = ''

        CREATE_TABLE_SQL = (f'CREATE TABLE IF NOT EXISTS {tableName} (\n'
                            f'ID {AUTOINCREMENT_SERIAL} PRIMARY KEY NOT NULL')

        for c in columns:
            foreign_key_string += c.foreign_key()
            CREATE_TABLE_SQL += f',\n{c.generate_column_creation_query()}'
        CREATE_TABLE_SQL += foreign_key_string
        CREATE_TABLE_SQL += '\n);'

        print(CREATE_TABLE_SQL)
        print('-------')
        execute_and_commit(dbName=self.dbName, query=CREATE_TABLE_SQL)

    """
        Drops a table from the database.
    """

    def drop_table(self, *, tableName):
        DROP_TABLE_SQL = f'DROP TABLE IF EXISTS {tableName} CASCADE;'

        execute_and_commit(dbName=self.dbName, query=DROP_TABLE_SQL)

    """
        Inserts a row into a specified table by columns and their values.

        @params tableName -name of the table we're inserting in.
        @params columns -columns which we're inserting values in.
        @PARAMS values - values which we're inserting into the columns we've specified.
    """

    def insert(self, *, tableName, columns, values):
        columns_str = ',\n'.join(columns)

        INSERT_ROW_SQL = (
            f'INSERT INTO {tableName}(\n '
            f'{columns_str}\n '
            ')\n '
            f'VALUES(\n '
            f'{", ".join(["%s"]*len(values))}\n'
            f');\n')
        print(INSERT_ROW_SQL)

        execute_and_commit(dbName=self.dbName, query=INSERT_ROW_SQL,values=values)

    """
        Fetches a row from a specified table by columns and their values.

        @params tablename - name of the table we're faetching from.
        @params constraints - string that contains the column constraints.
    """

    def fetch(self, *, tableName, constraints):
        GET_ROW_SQL = (f'SELECT * FROM {tableName}\n'
                       f'WHERE {"AND".join(constraints)};'
                       )
        print(GET_ROW_SQL)
        return execute_and_fetch(dbName=self.dbName, query=GET_ROW_SQL)

    """
        Fetches a row from the joined tables.

        @params mainTableName- string. Name of the main table.
        @params columns - list of strings. Names of the columns we want to fetch.
        @params joinTypes- list of strings. Types of joins we want to make for each table.
        @params otherTables- list of strings. Names of the tables we want to join.
        @params on- list of strings. What we're joining them on.
        @params newTableNames - list of strings. Names of the joined tables.
    """

    def joined_fetch(self, *, mainTableName, columns, joinTypes,
                     otherTables, on, newTableNames,
                     constraints=None):
        joinedTables = self.__joined_fetch_clause(
            joinTypes, otherTables, newTableNames, on)
        GET_JOINED_ROW_SQL = (f'SELECT {", ".join(columns)} FROM {mainTableName}\n'
                              f'{joinedTables}')

        if constraints != None:
            GET_JOINED_ROW_SQL += f'\nWHERE {"AND".join(constraints)}'

        GET_JOINED_ROW_SQL += ';'

        return execute_and_fetch(dbName=DATABASE_NAME, query=GET_JOINED_ROW_SQL)
