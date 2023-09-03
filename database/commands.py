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
        self.connection.execute(queris.create_fsm_user_table_query)
        self.connection.commit()

    def sql_insert_start(self,
                         telegram_id,
                         username,
                         first_name,
                         last_name):
        self.cursor.execute(queris.insert_user_query, (None,
                                                       telegram_id,
                                                       username,
                                                       first_name,
                                                       last_name))
        self.connection.commit()

    def sql_user(self):
        self.cursor.row_factory = lambda cursor, row: {'username': row[0]}
        return self.cursor.execute(queris.select_user_query).fetchall()

    def select_user_id_query(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {'id': row[0]}
        return self.cursor.execute(queris.select_user_id_query, (telegram_id,)).fetchall()

    def sql_insert_start_fsm(self,
                             user_id,
                             telegram_id,
                             nickname,
                             age,
                             bio,
                             gender,
                             photo
                             ):
        self.cursor.execute(queris.insert_user_form_query, (None,
                                                            user_id,
                                                            telegram_id,
                                                            nickname,
                                                            age,
                                                            bio,
                                                            gender,
                                                            photo))
        self.connection.commit()
