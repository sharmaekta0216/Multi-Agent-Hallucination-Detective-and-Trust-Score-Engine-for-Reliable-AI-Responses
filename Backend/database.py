# import mysql.connector


# def get_connection():
#     try:
#         connection = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="root123",
#             database="trust_score_db"
#         )

#         return connection

#     except mysql.connector.Error as err:
#         print("Database Error:", err)
#         return None
import mysql.connector

def get_connection():
    print("Trying to connect to MySQL...")

    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root123",
        database="trust_score_db",
        connection_timeout=5
    )

    print("Connected successfully!")
    return conn