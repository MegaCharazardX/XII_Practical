# Program - 6
a=[]
while True:
    print ("\nPush -> 1")
    print ("Pop -> 2")
    print ("Display-Stack −> 3") 
    print ("Exit -> 4\n")
    b= int(input("Enter your choice: "))
    
    if b==1:
        c=input("Enter any element:") 
        if "," in c :
            c = c.split(",")
            if " "  in c :
                c.remove(" ")
            print(c)
        a.append (c)
        
    elif b==2:
        if a== []:
            print (" Underflow! Stack is empty...")
        else:
            print("Popped element is", a.pop())
            
    elif b==3:
        if a== []:
            print ("Stack is empty...")
        else:
            d= len(a)
            for i in range (d-1,-1,-1): 
                print (f"\n{a[i]}")
                
    elif b==4:
        print ("End... Thank You.")
        break
    else:
        print("Invalid choice!")
