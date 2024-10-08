
import pymysql

con = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd  = "*password*11",
    database="school"
                    )

cur = con.cursor()
cur = con.cursor()
cur.execute("""INSERT INTO stud VALUES 
            (4, 'AKIL', 'XIIA'),
            (6, 'AMAL', 'XIIB')
            """)
con.commit()
print("Inserted successfully")
cur.execute("DESC stud")
for i in cur :
    print(i)