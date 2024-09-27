# Program - 1
with open("Text_Files/p1.txt", "r") as f :
    line = " "
    while line :
        line = f.readline()
        for word in line.split() :
            print(word, end = "#")
        print()
    f.close()