import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql@123"   # apna password likho
    )

    print("✅ Connected Successfully!")

    conn.close()

except Exception as e:
    print("❌ Error:")
    print(e)