import json
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

mydb = mysql.connector.connect(
  host="database-1-instance-1.cx6lbzv1spei.us-east-1.rds.amazonaws.com",
  user="admin",
  password="mysql123",
  database="employeedb"
)

mycursor = mydb.cursor()

sql = "INSERT INTO employee (empid, empname, empaddress) VALUES (%s, %s, %s)"

val = [
  ('100', 'bala', 'chennai'),
  ('101', 'venkatesh', 'madurai')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
