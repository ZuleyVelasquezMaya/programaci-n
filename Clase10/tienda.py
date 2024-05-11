import mysql.connector 

conexion = mysql.connector.connect (

    host = "localhost",
    user = "root",
    password = "0000",
    database = "tienda"

)

cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE productos(               
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR (255) NOT NULL,
    precio DECIMAL (10, 2) NOT NULL
 )  
""")