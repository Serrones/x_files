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

# Insert table
# 1 row
# sql = "INSERT INTO customers (name, fone) VALUES (%s, %s)"
# val = ("Michael Door", "992987677")
# mycursor.execute(sql, val)
#
# mydb.commit()
#
# print(mycursor.rowcount, "record inserted.")

# Multiple rows
sql = "INSERT INTO customers (name, fone) VALUES (%s, %s)"
val = [
  ('Peter', '238754569'),
  ('Amy', '109873457'),
  ('Hannah', '912834758'),
  ('Michael', '123456789'),
  ('Sandy', '154365789'),
  ('Betty', '153425687'),
  ('Richard', '123456789'),
  ('Susan', '098765432'),
  ('Vicky', '098765432'),
  ('Ben', '098765432'),
  ('William', '098765432'),
  ('Chuck', '098765432'),
  ('Viola', '098765432')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
