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
data=pd.read_csv(r'labsql.csv')
df=pd.DataFrame(data)
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO Phonebook (id_phone, name_students)
                VALUES (?,?)
                ''',
                (row.id_phone, 
                row.name_students)
                )
conn.commit()
cursor.execute("SELECT * FROM Phonebook")
results = cursor.fetchall()
print(results)