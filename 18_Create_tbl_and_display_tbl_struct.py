
import pymysql

con = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd  = "*password*11",
    database="school"
                    )

cur = con.cursor()
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXIST stud(roll_num int(10), name varchar(25), std int(5))")
con.commit()
print("Table Created")
cur.execute("DESC stud")
for i in cur :
    print(i)