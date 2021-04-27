import mysql.connector
conection=mysql.connector.connect(host="localhost",user="root",passwd="")

cursor=conection.cursor()
curso.execute("show databases")

for base in cursor:
    print(base)

connection.close()