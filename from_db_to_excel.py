"""
Mysql-connector
"""
import mysql.connector
from openpyxl import Workbook

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

# for x in myresult:
#   print(x)

# Create Excel (.xlsx) file
wb = Workbook()

sheet = wb.create_sheet(0)
sheet.title = 'customers_table'
sheet.append(mycursor.column_names)
for row in myresult:
    sheet.append(row)

workbook_name = "test_workbook"
wb.save(workbook_name + ".xlsx")
