# import mysql.connector

# print("Before connect")

# try:
#     conn = mysql.connector.connect(
#         host="127.0.0.1",
#         user="root",
#         password="sarthak@0216",
#         port=3306
#     )

#     print("After connect")

#     if conn.is_connected():
#         print("Connected successfully")

#         cursor = conn.cursor()
#         cursor.execute("SELECT VERSION();")
#         print(cursor.fetchone())

#         conn.close()

# except Exception as e:
#     print("Error:", e)
# import mysql.connector

# print("Step 1")

# try:
#     conn = mysql.connector.connect(
#         host="127.0.0.1",
#         port=3306,
#         user="root",
#         password="sarthak@0216"
#     )

#     print("Step 2")
#     print("Connected:", conn.is_connected())

#     cursor = conn.cursor()
#     cursor.execute("SHOW DATABASES")
#     print(cursor.fetchall())

#     conn.close()

# except Exception as e:
#     print("ERROR:", repr(e))
# import mysql.connector

# print("Before connect")

# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="sarthak@0216",
#     port=3306,
#     use_pure=True
# )

# print("After connect")
# print(conn.is_connected())
# conn.close()
import os

print("Running:", os.path.abspath(__file__))
import mysql.connector

def get_connection():
    print("Trying to connect to MySQL...")

    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="sarthak@0216",
        port=3306,
        database="trust_score_db",
        connect_timeout=10
    )

    print("Connected successfully!")
    return conn

if __name__ == "__main__":
    print("Before connect")
    conn = get_connection()
    print(conn.is_connected())
    conn.close()