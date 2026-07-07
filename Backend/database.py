import mysql.connector


def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root123",
            database="trust_score_db"
        )

        return connection

    except mysql.connector.Error as err:
        print("Database Error:", err)
        return None