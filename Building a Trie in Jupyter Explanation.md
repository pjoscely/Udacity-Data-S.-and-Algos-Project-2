## Building A Trie in Python.ipynb

Trie class used here more or less follows the Trie presented in the Udacity notes. The key data structure used in this Trie is a Python dictionary. The dictionary contains keys which link to a node’s descendant nodes. Python dictionaries are dynamic, so a given node in the Trie can have a variable number of descendant nodes. Upon researching Tries, some implementations use a fixed number of keys for every node: like 26 for the letters in the alphabet. This approach has the potential to waste storage space along with limiting the data stored that can be stored by the keys to a fixed number of characters.

For the Trie class, besides the constructor, an insert and exist methods are both implemented. An array of diverse test strings, including Null and empty strings, are tested for the Trie class in the Jupyter notebook submission. 

For the Finding Suffixes, a recursive helper function is used to return a list of all complete words  with a given prefix. This list is then filtered by the actual suffixes function to return a list with the suffix stripped from the words. An extensive word list with common prefixes is  tested via the supplied Udacity widget code.

According to https://en.wikipedia.org/wiki/Trie the time complexity of looking data up in a Trie is `O(m)  (where m is the length of a search string)`
 
According to https://www.geeksforgeeks.org/trie-insert-and-search/
The space complexity of trie seems to be: `O(ALPHABET_SIZE * key_length * N)` where N is number of keys in Trie.