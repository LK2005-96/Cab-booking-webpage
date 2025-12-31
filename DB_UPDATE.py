import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'Deepika'
)
mycursor = mydb.cursor()
sql = 'UPDATE staff name="hema"'


mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, 'records updated')
