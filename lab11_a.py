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
results = cursor.fetchall()
for i in results:
    if inf=='id':
        print(i[0])
    if inf=='name':
        print(i[1])
