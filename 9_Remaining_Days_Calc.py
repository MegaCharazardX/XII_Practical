# Program - 9
import datetime
a=0
b= datetime.datetime. now() 
print("Today's date:", b.day) 
if b. month == 2:
    a=28
elif b. month in (1,3,5,7,8, 10, 12):
    a=31
else:
    a=30
print("Total remaining days in the current month are:", a-b.day, "days")