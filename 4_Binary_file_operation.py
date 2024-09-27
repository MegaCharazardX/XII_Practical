# Program - 4
import pickle

f = open("Text_Files/Students.dat", "wb+")
n = int(input("Enter the number of records : "))
d = {}

for i in range(1, n+1):
    print(f"({i})")
    name = input("Enter the name of the student : ")
    rollno = int(input("Enter the roll no. : "))
    d[rollno]=name
pickle.dump(d,f)

f.close()

f = open("Text_Files/Students.dat", "rb+")
a = int(input("Enter the roll number to search by : "))
b = pickle.load(f)

if a in b.keys():
    print(f"The name of the student with the roll\
 no. {a} is {b[a]}")
else:
    print(f"No records match with the roll no. {a}.")
f.close()