import sqlite3
from sqlite3_handler import execute_and_commit

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
        return 'AUTOINCREMENT' if self.autoincrement else ''

    def foreign_key(self):
        if self.isForeignKey:
            return f',\nFOREIGN KEY({self.columnName}) REFERENCES {self.references}(ID)'
        return ''

    def generate_column_creation_query(self):
        return f'''{self.columnName} {self.columnType} {self.nullable()} {self.autoinc()}'''


class DataBase:
    def __init__(self, *, dbName):
        self.dbName = dbName

    def create_table(self, *, tableName, columns):
        foreign_key_string = ''

        CREATE_TABLE_SQL = f'''\
CREATE TABLE IF NOT EXISTS {tableName} (
ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL'''

        for c in columns:
            foreign_key_string += c.foreign_key()
            CREATE_TABLE_SQL += f',\n{c.generate_column_creation_query()}'
        CREATE_TABLE_SQL += foreign_key_string
        CREATE_TABLE_SQL += '\n);'

        print('-------')
        print(foreign_key_string)
        print('~~~~~~~')
        print(CREATE_TABLE_SQL)
        execute_and_commit(dbName=self.dbName,query=CREATE_TABLE_SQL)

    def drop_table(self, *, tableName):
        DROP_TABLE_SQL = f'''
        DROP TABLE IF EXISTS {tableName};
        '''
        execute_and_commit(dbName=self.dbName,query=DROP_TABLE_SQL)


DATABASE = 'queries/database/vehicle_management.db'


def generate_database():

    db = DataBase(dbName=DATABASE)

    db.drop_table(tableName='BaseUser')
    db.create_table(
        tableName='BaseUser',
        columns=[
            Column(columnName='user_name',
                   columnType='VARCHAR',
                   isNullable=False),
            Column(columnName='password',
                   columnType='VARCHAR',
                   isNullable=False),
            Column(columnName='email',
                   columnType='VARCHAR'),
            Column(columnName='phone_number',
                   columnType='INTEGER',
                   isNullable=False),
            Column(columnName='address',
                   columnType='VARCHAR',
                   isNullable=False)
        ]
    )

    db.drop_table(tableName='Client')
    db.create_table(
        tableName='Client',
        columns=[
            Column(columnName='base_id',
                   columnType='INTEGER',
                   isForeignKey=True,
                   references='BaseUser')
        ]
    )

    db.drop_table(tableName='Mechanic')
    db.create_table(
        tableName='Mechanic',
        columns=[
            Column(columnName='base_id',
                   columnType='INTEGER',
                   isForeignKey=True,
                   references='BaseUser'),
            Column(columnName='title',
                   columnType='VARCHAR',
                   isNullable=False),
        ]
    )

    db.drop_table(tableName='Vehicle')
    db.create_table(
        tableName='Vehicle',
        columns=[
            Column(columnName='category',
                   columnType='VARCHAR',
                   isNullable=False),
            Column(columnName='make',
                   columnType='VARCHAR',
                   isNullable=False),
            Column(columnName='model',
                   columnType='VARCHAR',
                   isNullable=False),
            Column(columnName='register_number',
                   columnType='VARCHAR',
                   isNullable=False),
            Column(columnName='gear_box',
                   columnType='VARCHAR',
                   isNullable=False),
            Column(columnName='owner',
                   columnType='INTEGER',
                   isForeignKey=True,
                   references='Client')
        ]
    )

    db.drop_table(tableName='Service')
    db.create_table(
        tableName='Service',
        columns=[
            Column(columnName='name',
                   columnType='VARCHAR',
                   isNullable=False),
            Column(columnName='mechanic_id',
                   columnType='INTEGER',
                   isForeignKey=True,
                   references='Mechanic')
        ]
    )

    db.drop_table(tableName='MechanicService')

    db.drop_table(tableName='VehicleRepair')
    db.create_table(
        tableName='VehicleRepair',
        columns=[
            Column(columnName='date',
                   columnType='VARCHAR',
                   isNullable=False),
            Column(columnName='start_hour',
                   columnType='VARCHAR',
                   isNullable=False),
            Column(columnName='vehicle',
                   columnType='INTEGER',
                   isForeignKey=True,
                   references='Vehicle'),
            Column(columnName='bill',
                   columnType='REAL',
                   isNullable=False),
            Column(columnName='mechanic_service',
                   columnType='INTEGER',
                   isForeignKey=True,
                   references='MechanicService')
        ]
    )


if __name__ == '__main__':
    generate_database()
