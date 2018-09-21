"""
Mysql-connector
"""
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="username",
    passwd="password",
    database="database_teste"
    )

mycursor = mydb.cursor()

# Select table
mycursor.execute("SELECT id, name, fone FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
