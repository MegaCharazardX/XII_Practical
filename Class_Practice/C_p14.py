import string

class dateConversion:
    def __init__(self, _date : str) -> None:
        self._date = _date
        self.__month_dict = {
                '01': 'January' , '02': 'February' , '03': 'March'     , 
                '04': 'April'   , '05': 'May'      , '06': 'June'      , 
                '07': 'July'    , '08': 'August'   , '09': 'September' , 
                '10': 'October' , '11': 'November' , '12': 'December'
            } 
        
    def is_mmddyyyy_form(self):
        temp_date = self._date
        if len(temp_date) == 8 :
            self.day = temp_date[2:4]
            self.month = temp_date[0:2]
            self.year = temp_date[4 : ]
            
            
        for i in string.ascii_letters + string.whitespace + \
                    string.punctuation :
            if i in temp_date :
                #print("!! Characters Not Allowed !!")
                return False
                break
            
            if month not in self.__month_dict:
                #print("!! Invalid Month Entry !!")
                return False
                continue
            
            if int(day) > 31 :
                #print("!! temp_date greater than 31 !!")
                return False
                continue
            
            if month == "02" and int(day) > 29 :
                #print("!! February only has 29 days !!")
                return False
                continue
            
            else:
                month =  self.__month_dict[month]  #break
        
        else : 
            return False
    
obj = dateConversion("02312024")
obj.is_mmddyyyy_form()