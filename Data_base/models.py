import sqlite3
from treid_bot_tg.Data_base.users_db import base_user

USERS = 'users'

def create_table():
    with sqlite3.connect(base_user) as conn:
        cur = conn.cursor()
        cur.execute(f'''
        CREATE TABLE IF NOT EXISTS {USERS}(
            user_id INTEGER AUTO_INCREMENT,
            tg_id INTEGER PRIMARY KEY,
            date_con TEXT,
            status TEXT
        )
        ''')
        conn.commit()