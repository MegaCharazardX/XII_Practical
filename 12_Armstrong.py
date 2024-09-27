#print("Program to find armstrong number") to check if it is amstrong number 
numbertofind = int(input("Enter the number : "))
numlist = list(str(numbertofind))
finalval = 0
for i in range (0,len(numlist)) :
    current_value = int(numlist[i])
    #armstrong = current_value**len(numb)
    temp = 1
    for j in range (0,len(numlist)):
        temp = temp*current_value

    finalval = finalval +  temp

print(f"The given number is {'an Armstrong Number'\
      if (numbertofind == finalval) else 'not an Armstrong Number'}")

# print(f"The sum of the power {len(numblist)} of {numbertofind} is {finalval}. Hence\
#  it is {'an Amstrong Number'if (numbertofind == finalval) else 'not an Amstrong Number'}")



#print("The sum of the power {0} of {1} is {2}. Hence it is {3}."
#.format(len(numblist),numbertofind,finalval,
#'an Amstrong Number' if (numbertofind == finalval)
#else 'not an Amstrong Number'))


#print("The sum of the power of {0}  is {1}.".format(numbertofind,finalval))
"""if finalval == numbertofind :
    print("The given number is an Armstrong number ")
else :
    print("The given number is not an Armstrong number ")"""
#input()

"It is a number that equals to the sum of the digits, each raised th the power of the number of the digits."
"eg."
"1634"
"1^4+6^4+3^4+4^4"