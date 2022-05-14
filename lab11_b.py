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
cntr=0
cursor.execute("SELECT * FROM Phonebook")
sqlid="UPDATE Phonebook SET id_phone=%s WHERE id_phone=%s;"
sqln="UPDATE Phonebook SET name_students=%s WHERE name_students=%s;"
sqlinsert="INSERT INTO Phonebook(id_phone, name_students) VALUES (%s, %s);"
results = cursor.fetchall()
if inf=='id':
    renameid=int(input())
    for i in results:
        if renameid==i[0]:
            renamedid=int(input())
            adr=(renamedid, renameid, )
            cursor.execute(sqlid, adr)
            cntr=cntr+1
    if cntr==0:   
        renamename=str(input())
        adr=(renameid, renamename )
            
        cursor.execute(sqlinsert, adr)

if inf=='name':
    renamename=str(input())
    
    for i in results:
        if renamename==i[1]:
            renamedname=str(input())
            adr=(renamedname, renamename, )
            cursor.execute(sqln, adr)
            cntr=cntr+1
    if cntr==0:
        renameid=int(input())
        adr=(renameid, renamename)
        cursor.execute(sqlinsert, adr)
cursor.execute("SELECT * FROM Phonebook")
results = cursor.fetchall()
print(results)
