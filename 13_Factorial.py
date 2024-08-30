# Program - 13
def factorial (n): 
    if n<0: 
        fact=-1 
        while n<-1: 
            fact *=n
            n-=-1
        return fact
    elif n ==0 or n == 1:
        return 1
    else:
        fact = 1
        while n>1: 
            fact *= n
            n-=1
        return fact
num = int (input("Enter the number to find factorial!" ))

print(" Factorial of ", num, "is", factorial (num))