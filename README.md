Autocompletion with Python
==========================

A simple autocompletion class that performs an efficient lookup for words that match a prefix. The subsequent list is return sorted and with any duplicates removed.

Features
--------

The prefix "tra" would return a list like: ["trace", "track", "trade", etc].

The file `autocomplete.py` is a standalone script that can be executed directly. The script requires the specification of a text file that contains the dictionary of words (one word per line). On most unix systems `/usr/share/dict/words` is a good test case.

Example
-------

```
$> /usr/bin/python2.7 autocomplete.py /usr/share/dict/words
Please type the prefix of a word: 
elep
Suggestions:
elephant
elephanta
elephantiac
elephantiasic
elephantiasis
elephantic
elephanticide
elephantine
elephantlike
elephantoid
elephantoidal
elephantous
elephantry
```

Dependencies
------------

The class has no external dependencies other than python. The code has been tested under python 2.7 and 3.3.