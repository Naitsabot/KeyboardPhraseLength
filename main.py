import sys
import unicodedata

def DK_keymap() -> dict:
    """Coordinates (cm) for standard DK (danish) keyboard (hoisontal space: 1.9 cm)"""

    return {
        "½":[0, 0], "1":[1.9, 0], "2":[3.8, 0], "3":[5.7, 0], "4":[7.6, 0], "5":[9.5, 0], "6":[11.4, 0], "7":[13.3, 0], "8":[15.2, 0], "9":[17.1, 0], "0":[19, 0], "+":[20.9, 0], "´":[22.8, 0], 
        "§":[0, 0], "!":[1.9, 0], '"':[3.8, 0], "#":[5.7, 0], "¤":[7.6, 0], "%":[9.5, 0], "&":[11.4, 0], "/":[13.3, 0], "(":[15.2, 0], ")":[17.1, 0], "=":[19, 0], "?":[20.9, 0], "`":[22.8, 0],
        "@":[3.8, 0], "£":[5.7, 0], "$":[7.6, 0], "€":[9.5, 0], "{":[13.3, 0], "[":[15.2, 0],"]":[17.1, 0], "}":[19, 0], "|":[22.8, 0],
        "\t":[1.1, 1.9], "q":[0.5, 1.9], "w":[2.4, 1.9], "e":[4.3, 1.9], "r":[6.2, 1.9], "t":[8.1, 1.9], "y":[10, 1.9], "u":[11.9, 1.9], "i":[13.8, 1.9], "o":[15.7, 1.9], "p":[17.6, 1.9], "å":[19.5, 1.9], "¨":[21.4, 1.9],
        "€":[4.3, 1.9], "^":[21.4, 1.9], "~":[21.4, 1.9],
        "a":[0.75, 3.8], "s":[2.65, 3.8], "d":[4.55, 3.8], "f":[6.45, 3.8], "g":[8.35, 3.8], "h":[10.25, 3.8], "j":[12.15, 3.8], "k":[14.05, 3.8], "l":[15.95, 3.8], "æ":[17.85, 3.8], "ø":[19.75, 3.8], "'":[21.65, 3.8],
        "*":[21.65, 3.8],
        "<":[0.25, 5.7], "z":[2.15, 5.7], "x":[4.05, 5.7], "c":[6, 5.7], "v":[7.85, 5.7], "b":[9.75, 5.7], "n":[11.65, 5.7], "m":[13.55, 5.7], ",":[15.45, 5.7], ".":[17.35, 5.7], "-":[19.25, 5.7],
        ">":[0.25, 5.7], "\\":[0.25, 5.7], ";":[15.45, 5.7], ":":[17.35, 5.7], "_":[19.25, 5.7],
        " ":[9.75, 5.7]
        }

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

def main():
    n = len(sys.argv)

    # arg 0: print
    if n > 2:
        printbol = eval(sys.argv[1])
        continuation = False

    # arg 1: phrase
    if n > 3:
        arg1 = str(sys.argv[2])
        continuation = True
    
    # arg 2: map
    if n > 4:
        arg2 = eval(sys.argv[3]+"()")
    else:
        arg2 = DK_keymap()
    
    # arg 3: debug
    if n == 5:
        arg3 = eval(sys.argv[4])
    else: 
        arg3 = False
    
    # call
    if continuation == True:
        if printbol == False:
            phrase_key_travel(phrase=arg1, dict_map=arg2, db_vec=arg3)
        else:
            print(phrase_key_travel(phrase=arg1, dict_map=arg2, db_vec=arg3),"cm")

if __name__ == "__main__":
    main()
