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
sqlid="UPDATE Phonebook SET id_phone=%s WHERE id_phone=%s;"
sqln="UPDATE Phonebook SET name_students=%s WHERE name_students=%s;"
results = cursor.fetchall()
if inf=='id':
    renameid=int(input())
    renamedid=int(input())
    for i in results:
        if renameid==i[0]:
            adr=(renamedid, renameid, )
            cursor.execute(sqlid, adr)
if inf=='name':
    renamename=str(input())
    renamedname=str(input())
    for i in results:
        if renamename==i[1]:
            adr=(renamedname, renamename, )
            cursor.execute(sqln, adr)
cursor.execute("SELECT * FROM Phonebook")
results = cursor.fetchall()
print(results)
