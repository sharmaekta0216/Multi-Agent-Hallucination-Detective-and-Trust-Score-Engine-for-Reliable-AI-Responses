import mysql.connector
def connect_db():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = " ",
        database = " "
    )
    return connection
def close_db():
def execute_query():
def fetch_data():