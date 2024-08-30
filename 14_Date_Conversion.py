# Program - 14
import string # importing string module

month_dict = {
                '01': 'January', '02': 'February', '03': 'March', 
                '04': 'April', '05': 'May', '06': 'June', 
                '07': 'July', '08': 'August', '09': 'September', 
                '10': 'October', '11': 'November', '12': 'December'
            }  # initializing dictionary which contains the months 
def validation ():
    try:
        while True :
            global date
            
            date = str(input("Enter the date in the format of <MMDDYYYY> : "))
            
            if len(date)!= 8:
                print("!! Invalid Format !!")
                continue
            
            for i in string.ascii_letters + string.whitespace + string.punctuation :
                if i in date :
                    print("!! Characters Not Allowed !!")
                    break
                
            else :
                month = date[0:2]
                day = date[2 : 4]
                if month not in month_dict:
                    print("!! Invalid Month Entry !!")
                    continue
                
                if int(day) > 31 :
                    print("!! Date greater than 31 !!")
                    continue
                
                if month == "02" and int(day) > 29 :
                    print("!! February only has 29 days !!")
                    continue
                
                else:
                    month =  month_dict[month]
                    break
    except Exception as e:
        print(f'Caught {type(e)}: e')
        
    finally :
        return  month     
    
def standardize(_month):
    standard_form =f"{ _month}, {date[2 : 4]}, {date [4 : ]}"
    return standard_form

print(f"The Standard Form : {standardize(validation())}")