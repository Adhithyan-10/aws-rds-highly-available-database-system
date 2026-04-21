import mysql.connector

try:
    conn = mysql.connector.connect(
        host="my-cloud-db.cvguyuq46gzk.ap-south-1.rds.amazonaws.com",
        user="admin",
        password="Adhi1234#",
        database="my_db"
    )

    cursor = conn.cursor()

    # ✅ Create table user_table
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS user_table (id INT, name VARCHAR(20))"
    )

    print("table created successfully")

    conn.commit()

except Exception as e:
    print("ERROR:", e)

finally:
    cursor.close()
    conn.close()
