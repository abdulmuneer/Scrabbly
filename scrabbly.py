'''
Created on March 08, 20123

@author: MUNEER
'''
import os, re
from pprint import pprint

from lib.scrab import Scrabbly, Helpers
from config import file_mapping

def main():
    scrabble_checker = Scrabbly()
    scrabble_checker.kick_start()

if __name__ == '__main__':
    main()
    
