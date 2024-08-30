# Program - 2
ch = " "
v_num = 0
c_num = 0
l_num = 0
u_num = 0
v_list = ["a", "A","e", "E","i", "I","o", "O","u", "U"]

with open("Text_Files\p1.txt", "r") as f :
    while ch:
        ch = f.read(1)
        if ch.islower():
            l_num += 1
        if ch.isupper():
            u_num +=1
        if ch in v_list:
            v_num +=1
        elif ch not in v_list and ch.isalpha():
            c_num +=1
            
print(f"The number of vowels : {v_num}")
print(f"The number of consonants : {c_num}")
print(f"The number of lowercase letters : {l_num}")
print(f"The number of uppercase letters : {u_num}")
