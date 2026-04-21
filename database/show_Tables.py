import mysql.connector

try:
    conn = mysql.connector.connect(
        host="my-cloud-db.cvguyuq46gzk.ap-south-1.rds.amazonaws.com",
        user="admin",
        password="Adhi1234#",
        database="my_db"
    )

    cursor = conn.cursor()
    cursor.execute("show tables")

    for i in cursor.fetchall():
        print(i)

    conn.commit()

except Exception as e:
    print("ERROR", e)

finally:
    cursor.close()
    conn.close()
