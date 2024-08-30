# This colored text means it is a comment
import string                                    # Importing the module to acces the characters to reduce the work of typing

all_num_dict = {}                                # Dictionary used for  reference in the coversion

def init_all_num_dict():
    for i in range(len(string.ascii_lowercase)): # Itrating the lowercase letter
        
        letter = string.ascii_lowercase[i] 
        if i < 9:# ---> The change               # If number less than 10 add a 0 infront
            number = "0" + str(i+1)
        else:
            number = str(i+1)# ---> The change
        all_num_dict[letter]=number

def alpha_to_num(_str):                          # Function to  Convert alphabet into numbers
    
    con_num = ""
    for i in _str :
        
        if i in all_num_dict :                   # If the itrating character is in the dictionary (Letters)
            con_num = con_num + all_num_dict[i] 
        else :                                   # If the itrating character is not in the dictionary (<space>, punctiation)
              con_num = con_num + i
    return con_num                               # Returning the conveted string

# Main Programm (__main__)
        
init_all_num_dict()                              # Calling the function to initialize the dictionary

str_input = input("Enter a string : ").lower()   # Lowercasing the input to standardize

ans = alpha_to_num(str_input)                    # Calling the convertion function and assigning it to a variable
print(ans)                                       # Printing the converted string 
    
# Instead of : 
# ans = alpha_to_num(str_input)                
# print(ans) 
# You can use :
# print(alpha_to_num(str_input)) ---> No need to declare another variable 