import sys
from time import sleep

class Tprint:
    
    def __init__(self, word):
        self.word = word
    
    def tprint(self):
        for char in self.words:
            sleep(0.015)
            sys.stdout.write(char)
            sys.stdout.flush()
            
a = Tprint("Hello. This Hari Dhejus V.S. of grade 12.")
a.tprint
()