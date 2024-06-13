import mysql.connector
try:
    connection = mysql.connector.connect(host="localhost",
                                         user="root",
                                         password="",
                                         database="hangman")
except Exception:
    print("Connection failed!!")

