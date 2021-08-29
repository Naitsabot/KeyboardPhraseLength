# KeyboardPhraseLength
Script to calculate length of travel between letters on a keyboard in a given phrase/word

Works with all letters, spaces and singular symbols. (Accents are not counted.)

Status:  
only has a keymap of DK-keyboard

The Calculation happens in the function phrase_key_travel from ```phrase_key_travel.py```  
Data for the keyboards kan be found in ```keymaps.py```  
```main.py``` can be called for easy one-off calls  

____________________________________________________________

Terminal use:  
```python.exe [print?-bool] "[phrase/word)" [keymap] [print?-debud-vectors-bool]```

Examples:  
```python.exe  main.py True "T| êst" DK_keymap False```  
```pyrhon.exe main.py True "T| êst"```  
```pyrhon.exe main.py False "T| êst"```

(excuse any weird spelling og phrasing)
