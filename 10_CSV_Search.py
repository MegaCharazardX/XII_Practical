# Program - 10
import csv
with open("user-info.csv", "w") as obj: 
    fileobj = csv.writer(obj)
    fileobj.writerow(["User_ID", "Password"])
    while True:
        user_id=input("Enter ID : ")
        password= input("Enter password : ") 
        record=[user_id, password]
        fileobj.writerow (record)
        x=input ("Press Y/y to continue or any other key to terminate the program : ")
        if x in "Yy":
            continue
        else:
            break
        
with open("user-info.csv", "r") as obj1:
    fileobj1 = csv.reader (obj1)
    given_id=input ("Enter the user-id to be searched : ")
    is_found = False
    _password = ""
    for i in fileobj1:
        next(fileobj1)
        if i[0] == given_id:
            is_found, _password = True , i[1]
        
    if is_found == True :
        print(f"UserID found.")
        print(f"Password of the given UserID : {_password}")
    
    else :
        print(f"UserID : {given_id} not found")