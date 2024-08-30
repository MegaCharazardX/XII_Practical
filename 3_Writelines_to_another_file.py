# Program - 3
f = open("Text_Files\p1.txt", "r")
line = f.readlines()
f.close()
file_with_a=  open(r"Text_Files\file_with_a.txt", "w+")
file_without_a = open(r"Text_Files\file_without_a.txt", "w+")

for i in line :
    if "a" in i :
        file_with_a.writelines(i)
    else:
        file_without_a.writelines(i)
file_without_a.close()
file_with_a.close()


