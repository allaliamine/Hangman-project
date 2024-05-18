import mysql.connector
connection = mysql.connector.connect(host="localhost", user="root", password="", database="hangman")

print(connection)

cur = connection.cursor()
cur.execute("select * from word")
res = cur.fetchall()

print(res)