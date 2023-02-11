import pymysql

class DbHandler:
    def __init__(self, host, username, password, db):
        self.host = host
        self.username = username
        self.password = password
        self.db = db
        self.connection = pymysql.Connect(host=self.host, user=self.username, password=self.password, database=self.db)
        self.cursor = self.connection.cursor()

    def execute(self, query, args=None):
        try:
            self.cursor.execute(query, args)
            self.connection.commit()
        except Exception as e:
            print(f"Error executing query: {e}")

    def select(self, query, args=None):
        self.cursor.execute(query, args)
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()

    def checkUserExist(self, email, password, acctype):
        try:
            if acctype == "admin":
                query = "select * from admin where ad_email = %s and ad_password = %s";
                args = (email, password)
                rows = self.select(query, args)
                if rows:
                    return True
                return False
            elif acctype == "rider":
                query = "select * from rider where rider_email = %s and rider_password = %s";
                args = (email, password)
                rows = self.select(query, args)
                if rows:
                    return True
                return False
            elif acctype == "consumer":
                query = "select * from consumer where con_email = %s and con_password = %s";
                args = (email, password)
                rows = self.select(query, args)
                if rows:
                    return True
                return False
        except Exception as e:
            print(e)
        finally:
            self.close()

    def Signup(self, username, email, password, cnic, phoneNo, license, criminalRec ):
        try:
            query = "INSERT INTO rider (rider_name, rider_email, rider_password, rider_cnic, rider_phone, " \
                    "rider_license,rider_criminalRec) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            args = (username, email, password, cnic, phoneNo, license, criminalRec)
            self.execute(query, args)
            print ("ïnsert")
        except Exception as e:
            print("Error: ", e)
        finally:
            self.close()