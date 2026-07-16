import mysql.connector

print("Connector imported")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sarthak@0216"
)

print("Connected!")
conn.close()