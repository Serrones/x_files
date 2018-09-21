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

# Create table
# mycursor.execute("CREATE TABLE customers (name VARCHAR(30), fone VARCHAR(9))")

# Alter table
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# Show tables
# mycursor.execute("SHOW TABLES")
#
# for item in mycursor:
#     print('Table ', item[0])
