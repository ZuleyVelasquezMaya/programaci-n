import mysql.connector

mydb = mysql.connector.connect (

    host = "localhost",
    user = "root",
    password = "0000",
    database = "testbd"

)

my_cursor = mydb.cursor()

my_sql = "DELETE FROM users WHERE user_id = 2"
my_cursor.execute(my_sql)
mydb.commit()



