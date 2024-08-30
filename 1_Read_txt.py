# Program - 1
f = open("p1.txt", "r")
line = " "
while line :
    line = f.readline()
    for word in line.split() :
        print(word, end = "#")
    print()
f.close()