# Program - 3
f = open("Text_Files\p1.txt", "r")
line = f.readlines()
l1 = []
l2 = []
for i in line :
    if "a" in i :
        l1.append(i)
    else:
        l2.append(i)
f.close()

f =  open(r"Text_Files\p2.txt", "w")
f.writelines(l1)
f.close()

f =  open(r"Text_Files\ p2-3.txt", "w")
f.writelines(l2)
f.close()


