import pymysql

class DatabaseHandler:
    def _init_(self, host, username, password, db):
        self.host = host
        self.username = username
        self.password = password
        self.db = db
        self.connection = pymysql.Connect(host=self.host, user=self.username, password=self.password, database=self.db)

    def execute(self, query, args=None):
        try:
            self.cursor.execute(query, args)
            self.conn.commit()
        except Exception as e:
            print(f"Error executing query: {e}")

    def select(self, query, args=None):
        self.cursor.execute(query, args)
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
