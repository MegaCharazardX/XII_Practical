
import pymysql

con = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd  = "*password*11",
    database="school"
                    )

cur = con.cursor()
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS stud(roll_num int(10), name varchar(25), std varchar(10))")
con.commit()
print("Table Created successfully")
cur.execute("DESC stud")
for i in cur :
    print(i)