import mysql.connector

mydb = mysql.connector.connect (

    host = "localhost",
    user = "root",
    password = "0000",
    database = "testbd"

)

my_cursor = mydb.cursor()

my_sql = "DROP TABLE IF EXISTS users"
my_cursor.execute(my_sql)
mydb.commit()