# Program - 15
import math

def is_fib_perfect_square(x):
    s = int(math.sqrt(x))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    return s*s == x

def is_fibonacci (n):
    return is_fib_perfect_square(5*n*n+4) \
        or is_fib_perfect_square(5*n*n-4)

num = float(input("Enter a number : "))
if is_fibonacci(num) == True :
    print(f"{num} is a fibonacci number.")
else :
    print(f"{num} is not a fibonacci number.") 