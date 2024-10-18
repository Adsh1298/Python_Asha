
# Create a python script to store data into a MySQL database where the data should be of LaptopInformation: Id, SlNo, Model, Brand, Price.
# The script should have a menu driven program that performs all CURD operations.
# It should not terminate itself, other than a request from the user.


import pymysql

# Class that abstracts the MySQL code from UR Flask Application.
class MySqlDatabase:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = pymysql.connect(host = "localhost", user = "root",
                                              password="root", database=" test")
            print("Connected to the database")
        except Exception as ex:
            print("Exception: ", ex)

    def disconnect(self):
        if self.connection:
            self.connection.cursor().close()
            self.connection.close()
            print("Disconnected from the database")

    def get_all_users(self):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                query = "SELECT * FROM LaptopInformation"
                cursor.execute(query)
                users = cursor.fetchall()
        except Exception as ex:
            print("Exception : ", ex)
        else:
                return users
        finally:
                self.disconnect()

    def get_user_by_id(self, id):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                query = "SELECT * FROM LaptopInformation WHERE id = %s"
                cursor.execute(query, id)
                selected_user = cursor.fetchone()
        except Exception as ex:
            print("Exception : ", ex)
        else:
                return selected_user
        finally:
                self.disconnect()

    def add_user(self, name, pwd, email):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                query = (f"INSERT INTO LaptopInformation (id,SlNo, Model, Brand, "
                         f"price) values (%s, %s, %s,%s)")
                cursor.execute(query, (name, pwd, email))
                self.connection.commit()
        except Exception as ex:
            print("Exception while inserting: ", ex)
        finally:
            self.disconnect()

    def update_user(self, id, name, pwd, email):
        try:
            self.connect();
            with self.connection.cursor() as cursur:
                query = (f"UPDATE LaptopInformation SET id = %s, SlNo= %s , "
                         f" Model = %s "
                         f"Brand = %s "
                         f"where id = %s")
                cursur.execute(query, (id,SlNo, Model, Brand,price))
                self.connection.commit()
        except Exception as ex:
            print(f"Exception: {ex}")
        finally:
            self.disconnect()