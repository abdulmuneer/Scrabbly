'''
Created on Apr 22, 2013

@author: MUNEER
'''
from collections import Counter
import string
from resources import bingo_stems, tiles


#trbeaiykedarmadfucnogsimatofeweredlductzlgoyaaohowxventsparesijiuhinbrevetiiangloetoonieq.spean.
class Extras():
    '''
    Extra utilities
    '''
    def __init__(self):
        pass
    def calculate_remaining_letters(self,available=None, used=None):
        if not available:
            available = {key: value['count'] for key, value in tiles.items()}
        counts = Counter(used)
        for items in counts:
            if items in available:
                available[items] -= counts[items]
        available = {ltr:cnt for ltr, cnt in available.items() if cnt}
        return(available)
        
    def get_available_letters(self):
        available = None # just to initialize
        while True:
            used = list(raw_input('\n\tEnter Word:\n').lower())
            if used[0] == '~':
                return 
            if any( [ y not in (string.ascii_lowercase + '.') for y in used]):
                print 'Invalid Entry. Please re-enter'
                continue
            available = self.calculate_remaining_letters(available, used)
            print(available)

    def get_bingo_stems(self, query):
        qry = set(query.upper())
        result_stems =[word for word in bingo_stems if set(word).issubset(qry)]
        return result_stems
        
        
                
        
        