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
# import mysql.connector

# def get_connection():
#     print("Trying to connect to MySQL...")

#     conn = mysql.connector.connect(
#     host="127.0.0.1",
#     user="root",
#     password="",
#     database="trust_score_db",
#     connection_timeout=5
# )

#     print("Connected successfully!")
#     return conn
# import mysql.connector

# def get_connection():
#     print("Trying to connect to MySQL...")

#     conn = mysql.connector.connect(
#         host="127.0.0.1",
#         user="root",
#         password="sarthak@0216",
#         database="trust_score_db",
#         connection_timeout=5
#     )

#     print("Connected successfully!")
#     return conn

# if __name__ == "__main__":
#     try:
#         get_connection()
#     except Exception as e:
#         print("Database Error:", e)
# import mysql.connector
# import pymysql

# print("Step 1")


# try:
#     print("Step 2")

#     conn = pymysql.connect(
#         host="127.0.0.1",
#         port=3306,
#         user="root",
#         password="sarthak@0216",
#         database="trust_score_db",
#         connect_timeout=5
#     )

#     print("Step 3 - Connected")
#         return conn

#   except Exception as e:
#     print("Step 4 - Error")
#     print(e)
#       return None

# print("Step 5")
# import mysql.connector

# print("Step 1")

# def get_connection():
    
#         print("Step 2 - Connecting to MySQL...")

#         conn = mysql.connector.connect(
#             host="127.0.0.1",
#             port=3306,
#             user="root",
#             password="sarthak@0216",
#             database="trust_score_db",
#             connection_timeout=5
#         )
#         print("Step 3 - Database Connected Successfully")
#         return conn
        

#         # if conn.is_connected():
          
# import mysql.connector
# from mysql.connector import Error

# # def get_connection():
#     try:
#         print("Trying to connect to MySQL...")

#         connection = mysql.connector.connect(
#             host="127.0.0.1",
#             user="root",
#             password="sarthak@0216",      # Replace with your MySQL password
#             database="trust_score_db",   # Replace with your database name
#             port=3306,
#             connect_timeout=10
#         )

#         if connection.is_connected():
#             print("✅ Connected to MySQL successfully!")
#             return connection

#     except Error as e:
#         print("❌ Database connection failed:")
#         print(e)
#         return None

# if __name__ == "__main__":
#     conn = get_connection()

#     if conn:
#         print("Database is working.")
#         conn.close()
#         print("Connection closed.")
#     else:
#         print("Database is not working.")


# import os
# print("Running file:", os.path.abspath(__file__))
# print("Step 1")

# try:
#     print("Step 2")

#     connection = mysql.connector.connect(
#         host="127.0.0.1",
#         user="root",
#         password="sarthak@0216",
#         database="trust_score_db",
#         port=3306,
#         connect_timeout=10
#     )

#     print("Step 3")

#     if connection.is_connected():
#         print("Connected!")

# except Exception as e:
#     print("Step 4")
#     print(e)

# print("Step 5")
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
# import mysql.connector

# def get_connection():
#     print("Trying to connect to MySQL...")
#     conn = mysql.connector.connect(
#         host="127.0.0.1",
#         user="root",
#         password="sarthak@0216",
#         database="trust_score_db",
#         port=3306
#     )

# if __name__ == "__main__":
#     print("Before connect")
#     conn = get_connection()
#     print("After connect")
#     print(conn.is_connected())
#     conn.close()
# import os

# print("Running:", os.path.abspath(__file__))
# import mysql.connector

# def get_connection():
#     print("Trying to connect to MySQL...")

#     conn = mysql.connector.connect(
#         host="127.0.0.1",
#         user="root",
#         password="sarthak@0216",
#         port=3306,
#         database="trust_score_db",
#         connect_timeout=10
#     )

#     print("Connected successfully!")
#     return conn

# if __name__ == "__main__":
#     print("Before connect")
#     conn = get_connection()
#     print(conn.is_connected())
#     conn.close()
# import mysql.connector

# print("Before connect")

# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="sarthak@0216",
#     port=3306,
#     connect_timeout=5
# )

# print("Connected to MySQL Server")

# cursor = conn.cursor()
# cursor.execute("SHOW DATABASES")
# print(cursor.fetchall())

# conn.close()
# print("Done")
# import mysql.connector

# print("Before connect")
# def get_connection():
#     print("Trying to connect to MySQL...")
#     return mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="sarthak@0216",
#         auth_plugin="caching_sha2_password",
#     use_pure=True,
#     database="trust_score_db"
# )

# print("Connected!")
# conn = get_connection()
# print(conn.is_connected())

# conn.close()
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

print("Before connect")


def get_connection():
    print("Trying to connect to MySQL...")

    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
         port=os.getenv("DB_PORT"),
        auth_plugin="caching_sha2_password",
        use_pure=True,
    )


if __name__ == "__main__":
    print("Connected!")

    conn = get_connection()

    print(conn.is_connected())

    conn.close()