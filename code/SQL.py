
import sqlite3

class SQL:
    def __init__(self,db_name=":memory:"):

        # Open connect to db

        self.conn = sqlite3.connect(db_name)

        self.cursor = self.conn.cursor()

    def generate_tables(self):

        self.cursor.execute("""
            CREATE TABLE 
            IF NOT EXISTS
            data 
            (
                instanceID TEXT,
                _id TEXT,
                timestamp INT,
                name TEXT,
                amount INT,
                type TEXT, 

                UNIQUE (_id, timestamp, name) ON CONFLICT IGNORE
            )
            """)

        self.cursor.execute("""
            CREATE TABLE 
            IF NOT EXISTS
            goods 
            (
                name TEXT UNIQUE ON CONFLICT IGNORE
            )
            """)

        self.cursor.execute("""
            CREATE TABLE 
            IF NOT EXISTS
            instances 
            (
                instanceID TEXT UNIQUE ON CONFLICT IGNORE,
                server_name TEXT UNIQUE ON CONFLICT IGNORE
            )
            """)

        self.conn.commit()

    def save_element(self, iid, _id, ts, name, amount):
        self.cursor.execute("""
            INSERT INTO 
            data
            (instanceID, _id, timestamp, name, amount)
            VALUES
            (?,?,?,?,?)
            """,
            (iid, _id, ts, name, amount)
            )
        self.cursor.execute("""
            INSERT INTO 
            goods
            (name)
            VALUES
            (?)
            """,
            (name,)
            )
        self.cursor.execute("""
            INSERT INTO 
            instances
            (instanceID)
            VALUES
            (?)
            """,
            (iid,)
            )
        self.conn.commit()
        pass