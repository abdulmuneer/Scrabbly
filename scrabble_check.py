'''
Created on March 08, 20123

@author: MUNEER
'''
import re
from pprint import pprint

file_mapping = {
    'sowpods' : 'sowpods.txt',
    'twl' : 'twl.txt'
        }


def main():
    scrabble_checker = ScrabbleChecker()
    scrabble_checker.kick_start()

class Helpers():
    '''
    Class for re-usable helper functions
    '''
    def error_message(self):
        print"Dictionary not found in the path."
        print "Please copy appropriate word list file to the same directory as program"
        print "and re-run the program again.."
        return False

    def validate(self, query):
        import string
        valid_chars = set('[\^$.|?*+~()]{}' + string.ascii_lowercase)
        query = set(query)
        return query.issubset(valid_chars)

    def choose_wordlist(self):
        word_list = None
        while not word_list:
            print 'CHOOSE WORD LIST..(S)OWPODS or (T)WL?',
            print 'Enter ~ to quit\n'
            x = raw_input().lower()
            if x.startswith('s'):
                word_list = file_mapping['sowpods']
                print('SOWPODS chosen.')
            elif x.startswith('t'):
                word_list = file_mapping['twl']
                print('TWL Chosen.')
            elif x.startswith('~'):
                word_list = '~'
            else:
                word_list = None
                print('Invalid option specified.')
        return None if word_list == '~' else word_list

class ScrabbleChecker():
    '''
    Contains all relevant methods like search, match etc.
    '''
    def __init__(self):
        self.helpers = Helpers()
        self.function_map = {
                            'c' : self.check,
                            's' : self.suggest,
                            'm' : self.matches,
                            'p' : self.possibilities,
                            'b' : self.bingo_finder
                            }

    def get_options(self):
        """
        ask user if he wants to search, check or explore possible words etc
        """
        option_obtained = False
        while not option_obtained:
            print '\tChoose Options: ',
            print sorted(x.__name__ for x in self.function_map.values())
            print '\tEnter the first character of any option. Or enter ~ to exit.'

            option = raw_input('\n')
            option = option.lower()

            if option in ['~'] + self.function_map.keys():
                option_obtained = True
            else:
                print 'invalid option entered'

        return None if option=='~' else option

    def get_query_string(self):
        '''
        gets query, validates it and returns a tuple (query, wordlength)
        '''
        query_obtained = False
        while not query_obtained:
            query_string = raw_input(
                '\tEnter querystring <wordlength>\n\t(or "~" to exit)\n').lower()
            if not query_string:
                print '\tNo search word entered'
                continue
            query = query_string.split(' ')[0]
            if query == '~':
                return None, 0
            if not self.helpers.validate(query):
                print 'Invalid word or regex entered'
                continue
            query_obtained = True

        try:
            length = int(query_string.split(' ')[1])
        except:
            length = 0
        return query, length

    def exit(self):
        print '~'*14,'\nGood Bye!! :-)\n','~'*14

    def kick_start(self):
        word_list = self.helpers.choose_wordlist()
        if not word_list:
            return self.exit()
        try:
            x = open(word_list)
        except:
            x.close()
            self.helpers.error_message()
            return self.exit()

        with open(word_list) as scrabblefile:
            print 'Word list opened..'
            self.scrabblefile = tuple(x.strip().lower() for x in scrabblefile)
            print 'total words = %s\n'%len(self.scrabblefile)
            #Now set things in motion
            is_running = True
            while is_running:
                option = self.get_options()
                if not option:
                    return self.exit()
                query, word_length = self.get_query_string()
                if not query:
                    return self.exit()
                is_running = self.function_map[option](query, word_length)


    def check(self, query, length=0):
        '''
        Checks if the entered word is valid or not
        '''
        for lines in self.scrabblefile:
            if query == lines.strip().lower():
                print "\nACCEPTED Word..\n"
                return True
        else:
            print "\n'%s' is NOT an accepted word\n"%query
            return True

    def suggest(self, query, length=0):
        '''
        Displays all possible words that have the query string as a part of it
        Regexes accepted
        '''
        if length:
            result = (x.upper() for x in self.scrabblefile if
                      len(x)==length and re.search(query, x))
        else:
            result = (x.upper() for x in self.scrabblefile if
                      re.search(query, x))
        pprint(sorted(result, key=lambda x:len(x)))
        return True

    def matches(self, query, length=0):
        '''
        Shows all possible words that are starting with a specific sequence.
        Regexes are accepted
        '''
        pattern = re.compile(query)
        if length:
            result = (x.upper() for x in self.scrabblefile if
                      len(x)==length and pattern.match(x))
        else:
            result = (x.upper() for x in self.scrabblefile if
                      pattern.match(x))
        pprint(sorted(result, key=lambda x:len(x)))
        return True

    def possibilities(self, query, length=0):
        '''
        Displays the possible words that can be made out of your characters
        Regexes not accepted
        '''
        def letter_count(recommended, source):
            '''
            recommended letters should not be greater than the query.
            used by the enveloping method.
            '''
            for letters in recommended:
                if recommended.count(letters) > source.count(letters):
                    return False
            return True

        result = (x.upper() for x in self.scrabblefile 
                if set(x).issubset(set(query)) and letter_count(x, query))
        if length:
            result = (x for x in result if len(x)==length)
        pprint(sorted(result, key=lambda x:len(x)))
        return True

    def bingo_finder(self, query, length=0):
        '''
        Helps in finding words that you can form using all letters you have
        '''
        wordlength = len(query)
        def is_valid(recommended, query):
            '''
            suggested words dhould have all letters from query
            '''
            letters = set(query)
            for letter in letters:
                if query.count(letter)>recommended.count(letter):
                    return False
            return True


        result = (x.upper() for x in self.scrabblefile
                if len(x)>=wordlength and set(query).issubset(set(x)) and is_valid(x, query))
        if length:
            result = (x for x in result if len(x)==length)
        pprint(sorted(result,key=lambda x:len(x)))
        return True




if __name__ == '__main__':
    main()
    
