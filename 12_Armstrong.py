# Program - 12
def arm ():
    n=int(input("Enter the number:"))
    s=n
    b= len(str (n)) 
    Sum=0
    while n!=0: 
        Sum=Sum+(8** b)
        n = n //10
        if s==Sum:
            print (" The given number", s, "isarmstrong number")
        else:
            print (" The given number", s, " is not armstrong number")
arm()