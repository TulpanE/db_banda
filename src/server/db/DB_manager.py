import sqlite3
from server.settings import BASE_PATH
import os

class DBmanager:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def check_base(self):
        return os.path.exists(self.db_path)


    def connect_base(self):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        return conn, cur

    def create_base(self, script_path: str):
        if not self.check_base():
            conn, cur = self.connect_base()
            cur.executescript(open(script_path).read())
            conn.commit()
            conn.close()

    def execute(self, query: str, args=(), many: bool = True):
        conn, cur = self.connect_base()
        res = cur.execute(query, args)
        result = res.fetchall() if many else res.fetchone()
        conn.commit()
        return result


base_manager = DBmanager(BASE_PATH)
