import pymysql
connection = pymysql.connect(host="localhost", user="root", password="", database="hangman-project")

print(connection)

cur = connection.cursor()
cur.execute("select * from topic")
res = cur.fetchall()

print(res)