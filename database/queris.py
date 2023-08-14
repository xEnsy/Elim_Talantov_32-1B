
create_user_table_query = """
       CREATE TABLE IF NOT EXISTS telegram_users 
       (ID INTEGER PRIMARY KEY, USERNAME CHAR (50),
       FIRST_NAME CHAR(50), LAST_NAME CHAR (50))    
"""

insert_user_query = """INSERT INTO telegram_users VALUES(?, ?, ?, ?)"""

select_user_query =  """SELECT username FROM telegram_users """