# Program - 5
import random, time 
print("Random Number Generator")

def generate_num():
    time.sleep(2)
    a=random.randint (1,6) 
    print (a)

C= True
while C:
    print ("Generating...")
    generate_num()
    b=input ("Do you want to roll the dice once more (y/n)?")
    if b == 'y':
        continue
    else:
        C=False
