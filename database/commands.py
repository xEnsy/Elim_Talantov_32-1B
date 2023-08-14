import sqlite3
from database import queris


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("db.sqlite3")
        self.cursor = self.connection.cursor()

    def sql_create(self):
        if self.connection:
            print("База данных успешно подключена")

        self.connection.execute(queris.create_user_table_query)
        self.connection.commit()

    def sql_insert_start(self, username, first_name, last_name):
        self.cursor.execute(queris.insert_user_query, (None,
                                                       username,
                                                       first_name,
                                                       last_name))
        self.connection.commit()

    def sql_user(self):
        return self.cursor.execute(queris.select_user_query).fetchall()
