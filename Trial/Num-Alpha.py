import string                                   

#all_num_dict = {}                               
num_all_dict = {}

# def init_all_num_dict():
    
#     for i in range(len(string.ascii_lowercase)): # Itrating the lowercase letter
        
#         letter = string.ascii_lowercase[i] 
#         if i < 10:                               # If number less than 10 add a 0 infront
#             number = "0" + str(i+1)
#         else:
#             number = str(i)

#         all_num_dict[letter]=number
        
def init_num_all_dict():
    
    for i in range(len(string.ascii_lowercase)):
        
        letter = string.ascii_lowercase[i] 
        if i <+ 9:                              
            number = "0" + str(i+1)
        else:
            number = str(i+1)
        num_all_dict[number]=letter
        
init_num_all_dict()



def num_to_alpha(_str):                         
    
    con_num = ""
    lst = []
    for i in range(0, len(_str), 2) :
        lst .append(_str[i : i+2]) 
    
    print(lst)    
    for i in lst :
        
        if i in num_all_dict :                  
            con_num = con_num + num_all_dict[i] 
        else :                                  
              con_num = con_num + i
    return con_num                              

# Main Programm (__main__)
        
#init_all_num_dict()                             

str_input = input("Enter a string : ").lower()  

ans = num_to_alpha(str_input)                   

print(ans)                                      

#print(num_all_dict)