from src.queries.database_manager import DataBase, Column, DATABASE_NAME


def generate_database():

    db = DataBase()

    db.drop_table(tableName='Movies')
    db.create_table(
        tableName='Movies',
        columns=[
            Column(columnName='name',
                   columnType='VARCHAR',
                   isNullable=False),
            Column(columnName='rating',
                   columnType='REAL',
                   isNullable=False)
        ]
    )

    db.drop_table(tableName='Projections')
    db.create_table(
        tableName='Projections',
        columns=[
            Column(columnName='movie_id',
                   columnType='INTEGER',
                   isNullable=False,
                   isForeignKey=True,
                   references='Movies'),
            Column(columnName='type',
                   columnType='VARCHAR',
                   isNullable=False),
            Column(columnName='date',
                   columnType='DATE',
                   isNullable=False),
            Column(columnName='time',
                   columnType='TIME',
                   isNullable=False)
        ]
    )

    db.drop_table(tableName='Users')
    db.create_table(
        tableName='Users',
        columns=[
            Column(columnName='username',
                   columnType='VARCHAR',
                   isNullable=False),
            Column(columnName='password',
                   columnType='VARCHAR',
                   isNullable=False),
            Column(columnName='salt',
                   columnType='VARCHAR',
                   isNullable=False),
        ]
    )

    db.drop_table(tableName='Reservations')
    db.create_table(
        tableName='Reservations',
        columns=[
            Column(columnName='user_id',
                   columnType='INTEGER',
                   isNullable=False,
                   isForeignKey=True,
                   references='Users'),
            Column(columnName='projection_id',
                   columnType='INTEGER',
                   isNullable=False,
                   isForeignKey=True,
                   references='Projections'),
            Column(columnName='row',
                   columnType='INTEGER',
                   isNullable=False),
            Column(columnName='col',
                   columnType='INTEGER',
                   isNullable=False)
        ]
    )


if __name__ == '__main__':
    generate_database()
