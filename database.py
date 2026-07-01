# import mysql.connector

# def get_connection():
#     connection= mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="root123",
#         database="trust_score_db"
#     )
#     return connection

# # ##conn = get_connection()

# ##if conn.is_connected():
#     print("Database connected successfully!")


# ###def close_db(connection):
#     if connection.is_connected():
#         connection.close()


# def execute_query(connection, query):
#     cursor = connection.cursor()
#     cursor.execute(query)
#     connection.commit()
#     cursor.close()


# def fetch_data(connection, query):
#     cursor = connection.cursor()
#     cursor.execute(query)
#     # data = cursor.fetch
#     cursor.close()
#     return data()
import mysql.connector

def get_connection():
    print("Trying to connect...")

    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root123",
        database="trust_score_db"
    )

    print("Connected successfully!")

    return connection