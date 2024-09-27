# Program - 7
import csv
product_data= [
                ["PID", "PNAME", "COST", "QUANTITY"], 
                ["P1", "BRUSH", 50, 200],
                ["P2", "TOOTHPASTE", 120, 150],
                ["P3", "SOAP", 40,300], 
                ["P4", "SHEETS", 100, 500],
                ["P5", "PEN", 10, 250]
            ]

def write ():
    a= open("PRODUCT.csv", "w", newline="") 
    c= csv.writer (a)
    c. writerows (product_data)
    
def read ():
    a= open("PRODUCT.csv", "r") 
    c= csv.reader (a) 
    for i in c: 
        print (i)
write() 
read ()