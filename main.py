import sys
from keymaps import *
from phrase_key_travel import *

def main(prase, bprint, bdebug, keymap):  
    # call
    if bprint == False:
        phrase_key_travel(phrase=arg1, dict_map=arg2, db_vec=arg3)
    else:
        print(phrase_key_travel(phrase=arg1, dict_map=arg2, db_vec=arg3),"cm")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='oh yeah...')
    parser.add_argument("phrase", help="working phrase")
    parser.add_argument("keymap", required=0, default="DK_keymap()", help="used keymap")
    parser.add_argument("print", required=0, default=0, help="print output")
    parser.add_argument("debug", required=0, default=0, help="debug print")
    args, unknown = parser.parse_known_args()
    main(args.phrase, bool(args.print), bool(args.debug), args.keymap)
