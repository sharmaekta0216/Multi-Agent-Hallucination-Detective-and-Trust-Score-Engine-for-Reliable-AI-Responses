import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="trust_score_db"
    )
    return connection

conn = connect_db()

if conn.is_connected():
    print("Database connected successfully!")


def close_db(connection):
    if connection.is_connected():
        connection.close()


def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()


def fetch_data(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return data