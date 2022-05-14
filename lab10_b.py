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
idp=str(input())
sname=str(input())
cursor.execute('''
            INSERT INTO Phonebook (id_phone, name_students)
            VALUES (?,?)
            ''',
            (idp, 
            sname)
            )
conn.commit()
cursor.execute("SELECT * FROM Phonebook")
results = cursor.fetchall()
print(results)