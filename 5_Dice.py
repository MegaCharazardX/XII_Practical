# Program - 5
import random, time 
print("Random Number Generator")

def generate_num():
    time.sleep(2.1)
    a=random.randint (1,6) 
    return a

c= True

while c:
    print ("Generating...")
    print(f"Number : {generate_num()}")
    b=input ("Do you want to go again (y/n)?")
    if b == 'y':
        continue
    else:
        c=False
