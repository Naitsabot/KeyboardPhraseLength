import sys
from keymaps import *
from phrase_key_travel import *

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
