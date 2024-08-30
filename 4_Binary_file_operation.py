# Program - 4
import pickle

f = open("Text_Files\Students.dat", "wb+")
n = int(input("No. of records : "))
d = {}
for i in range(1, n+1):
    print(f"({i})")
    name = input("Enter the name of the student :")
    rollno = int(input("Enter the roll No. :"))
    d[rollno]=name
pickle.dump(d,f)
f.close()
f = open("Text_Files\Students.dat", "rb+")
a = int(input("Enter the roll no. to search by : "))
b = pickle.load(f)
if a in b.keys():
    print(f"The name of the student with the given roll\
        no. {a} is {b[a]}")
else:
    print("No record matches with the given roll no.")
f.close()