import unicodedata
from keymaps import *

def phrase_key_travel(phrase: str, dict_map: dict = DK_keymap(), db_vec: bool = False) -> int:
     """Centimeter travel between keys of  phrase/word on keyboard (dict_map) """
     
     phrase = str(unicodedata.normalize('NFKD', phrase.lower()).encode('ASCII', 'ignore'))
     from math import sqrt
     length = 0

     for i in range(len(phrase)):
        if i == 0 : continue 

        vec = [dict_map[phrase[i-1]][0] - dict_map[phrase[i]][0], 
            dict_map[phrase[i-1]][1] - dict_map[phrase[i]][1]]

        if db_vec == True: print(vec)

        length += sqrt(vec[0]**2 + vec[1]**2)
     
     return round(length, 3)