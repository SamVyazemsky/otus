import pymysql
import pyodbc


conn = pymysql.connect(host='localhost', user='store', password='qwerty', db='shop')
conn2 = pyodbc.connect()
cursor = conn.cursor()

cursor.execute('select * from oc_banner')
print(cursor.fetchall())
print(cursor.rowcount)
cursor.execute('select * from oc_banner')
print(cursor.fetchmany(size=1))
print(cursor.rowcount)
cursor.close()
cursor.execute('select * from oc_customer')
conn.close()
# rest_of_rows = cursor.fetchall()
# print(row)
# print('_______')
# print(rest_of_rows)