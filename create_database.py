"""
Mysql-connector
"""
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="username",
    passwd="password"
    )

mycursor = mydb.cursor()

# Create database
# mycursor.execute("CREATE DATABASE database_teste")

# Show databases
mycursor.execute("SHOW DATABASES")

for item in mycursor:
    print('Database ', item[0])
