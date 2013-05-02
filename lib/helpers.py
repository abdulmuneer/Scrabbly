'''
Created on Apr 22, 2013

@author: MUNEER
'''
from collections import Counter
import string
from pprint import pprint
tiles = {
          'a':{'count':9,'points':1},
          'b':{'count':2,'points':3},
          'c':{'count':2,'points':3},
          'd':{'count':4,'points':2},
          'e':{'count':12,'points':1},
          'f':{'count':2,'points':4},
          'g':{'count':4,'points':2},
          'h':{'count':2,'points':4},
          'i':{'count':9,'points':1},
          'j':{'count':1,'points':8},
          'k':{'count':1,'points':5},
          'l':{'count':4,'points':1},
          'm':{'count':2,'points':3},
          'n':{'count':6,'points':1},
          'o':{'count':8,'points':1},
          'p':{'count':2,'points':3},
          'q':{'count':1,'points':10},
          'r':{'count':6,'points':1},
          's':{'count':4,'points':1},
          't':{'count':6,'points':1},
          'u':{'count':4,'points':1},
          'v':{'count':2,'points':4},
          'w':{'count':2,'points':4},
          'x':{'count':1,'points':8},
          'y':{'count':2,'points':4},
          'z':{'count':1,'points':10},
          '.':{'count':2,'points':0},
           }
#trbeaiyarmadfuckednogsimatofeweredlductzlgoyaaohowxventsparesijiuhinbrevetiiangloetoonieq.spean.
def calculate_remaining_letters(available=None, used=None):
    if not available:
        available = {key: value['count'] for key, value in tiles.items()}
    counts = Counter(used)
    for items in counts:
        if items in available:
            available[items] -= counts[items]
    available = {ltr:cnt for ltr, cnt in available.items() if cnt}
    return(available)
    
def get_available_letters():
    available = None # just to initialize
    while True:
        used = list(raw_input('\n\tEnter Word:\n').lower())
        if used[0] == '~':
            return 
        if any( [ y not in (string.ascii_lowercase + '.') for y in used]):
            print 'Invalid Entry. Please re-enter'
            continue
        available = calculate_remaining_letters(available, used)
        print(available)

if __name__ == '__main__':
    get_available_letters()
                
        
        