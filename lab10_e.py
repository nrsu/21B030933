import psycopg2
import pandas as pd
import pyodbc
conn=psycopg2.connect(
    host='localhost',
    dbname='postgres',
    user='postgres',
    password='boxer31'
)
cursor=conn.cursor()
inf=str(input())

cursor.execute("SELECT * FROM Phonebook")
sqlid="DELETE FROM Phonebook WHERE id_phone=%s;"
sqln="DELETE FROM Phonebook WHERE name_students=%s;"
results = cursor.fetchall()
if inf=='id':
    deletecol=int(input())
    for i in results:
        if deletecol==i[0]:
            adr=(deletecol, )
            cursor.execute(sqlid, adr)
if inf=='name':
    deletecol=str(input())
    for i in results:
        if deletecol==i[1]:
            adr=(deletecol, )
            cursor.execute(sqln, adr)
cursor.execute("SELECT * FROM Phonebook")
results = cursor.fetchall()
print(results)
