create_user_table_query = """
        CREATE TABLE IF NOT EXISTS telegram_users
        (ID INTEGER PRIMARY KEY,
        TELEGRAM_ID INTEGER,
        USERNAME CHAR(50),        
        FIRST_NAME CHAR(50),        
        LAST_NAME CHAR(50),
        UNIQUE (TELEGRAM_ID))
"""
create_fsm_user_table_query = """
        CREATE TABLE IF NOT EXISTS user_form
        (ID INTEGER PRIMARY KEY,
        USER_ID INTEGER NOT NULL,
        TELEGRAM_ID INTEGER,
        NICKNAME CHAR(50),
        AGE INTEGER,
        BIO TEXT,
        PHOTO TEXT,
        FOREIGN KEY (USER_ID) REFERENCES telegram_users (ID))
"""

insert_user_query = """INSERT INTO telegram_users VALUES(?, ?, ?, ?, ?)"""

insert_user_form_query = """INSERT INTO user_form VALUES(?, ?, ?, ?, ?, ?)"""

select_user_query = """SELECT username FROM telegram_users """

select_user_id_query = """SELECT ID FROM telegram_users WHERE TELEGRAM_ID = ?"""

