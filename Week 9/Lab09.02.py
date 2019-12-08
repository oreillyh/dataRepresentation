import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE datarepresenation")

sql="CREATE TABLE grocery (id INT AUTO_INCREMENT PRIMARY KEY, type VARCHAR(255), item type VARCHAR(255), name VARCHAR(255), quantity INT )"

mycursor.execute(sql)