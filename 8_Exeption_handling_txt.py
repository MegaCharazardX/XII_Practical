# Program - 8
error_name = ""
try : 
    file_loc = input("Enter your file location and name :")
#of the file : ")
    f1 = open(file_loc, "r")
    content = f1.read()
    print(content)

except FileNotFoundError as err :
    error_name = "FileNotFoundError"
    print("File Not Found")

except IOError as err:
    error_name = "IOError"    
    print("Error occured while reading the file.")

except Exception as e :
    print(f"Caught {e}")

finally :
    if error_name != "FileNotFoundError":
        f1.close()
        print("File Closed")
        