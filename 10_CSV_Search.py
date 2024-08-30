# Program - 10
import csv
with open("user-info.csv", "w") as obj: 
    fileobj = csv.writer (obj)
    fileobj.writerow(["User_ID", "Password"])
    while True:
        user_id=input("Enter ID: ")
        password= input("Enter password:") 
        record=[user_id, password]
        fileobj. writerow (record)
        x=input ("Press Y/y to continue or N/n to terminate the program:\n")
        if x in "Nn":
            break
        elif x in "Yy":
            continue
with open("user-info.csv", "r") as obj1:
    fileobj1 = csv. reader (obj1)
    given=input ("Enter the user-id to be Searched\n")
    for i in fileobj1:
        next(fileobj1)
        if i[0] == given:
            print ("Password is", i[1])
            break 
        else:
            print ("No record matches with thegiven user-id")