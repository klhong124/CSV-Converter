import mysql.connector

print('before ok')

mysql.connector.connect(
  host='localhost',
  port='8888',
  database='cc_logistics',
  user='root',
  password='root'
)

print('ok')