# Program 17

import pymysql

con = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd  = "*password*11"
                    )

cur = con.cursor()
cur = con.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS School ;")
print("DB Created")
cur.execute("SHOW DATABASES ;")
for i in cur :
    print(i)