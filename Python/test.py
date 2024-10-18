# Create a python script to store data into a MySQL database where the data should be of LaptopInformation: Id, SlNo, Model, Brand, Price.
# The script should have a menu driven program that performs all CURD operations.
# It should not terminate itself, other than a request from the user.
import pymysql
sql_select_all ="SELECT * FROM  LaptopInformation"
sql_select_by_id = "SELECT * FROM  LaptopInformation WHERE id = %s"
sql_insert = "insert into LaptopInformation(id,SlNo, Model, Brand, price) values( %s,%s,%s, %s,)"
sql_update = ("UPDATE USERINFO SET id = %s, SlNo = %s, Model = %s ,Brand =%s, "
              "price = %s where "
              "id %s")

# sql_update = "UPDATE LaptopInformation SET username = %s, emailaddress = %s, password = %s where id = %s"
# sql_delete = "DELETE FROM  LaptopInformation WHERE id = %s"

#MySql Configurations:
db_config ={
    'host' : 'localhost',
    'user' : 'root', #root
    'password' : 'cdacacts', #cdacacts
    'db' : 'sampledb'
}

def get_all_users():
    connection = pymysql.connect(**db_config)
    cursur = connection.cursor()
    try:
        cursur.execute(sql_select_all)
        users= cursur.fetchall()

    except Exception  as ex:
            print("Exception raised: ", ex)
    else:
        return users
    finally:
        cursur.close()
        connection.close()

def get_user_by_id():
    connection = pymysql.connect(**db_config)
    cursur = connection.cursor()
    try:
        cursur.execute(sql_select_by_id, id)
        user = cursur.fetchone()
    except Exception as ex:
        print("Exception while fetching single record: ", ex)
    else:
        return user
    finally:
        cursur.close()
        connection.close()

def add_user(id,SlNo, Model, Brand, price):
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    try:
        cursor.execute(sql_insert, (id,SlNo, Model, Brand, price))
        connection.commit()
    except Exception as ex:
        print("Failed to insert: ", ex)
    finally:
        cursor.close()
        connection.close()
        try:
            # todo: take inputs from the user and pass it as args to the add_user func
            add_user("2", "apple@123", "abcd1234")
            users = get_all_users()
        except:
            print("Error occured: ")
        else:
            for user in users:
                print(f"{user[1]} with id: {user[3]} is identified as {user[0]}")
        finally:
            print("End of the Application")


