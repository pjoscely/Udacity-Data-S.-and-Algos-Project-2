# HTTP Router using a Trie

This program uses the 3 supplied Udacity classes and suggested methods. The program also uses a Trie data structure to build a framework for a HTTP Router with response handlers in the form of strings. The key data structure used in the Trie here is a Python dictionary. The dictionary contains keys which link to a node’s descendant nodes. Python dictionaries are dynamic, so a given node in the Trie can have a variable number of keys and hence descendant nodes. Upon researching Tries, some implementations suggested using a fixed number of keys for every node, For example: 26 keys corresponding to the letters in the alphabet. This approach potentially can waste storage space along with limiting the data stored that can be by referenced by the keys to a fixed number of characters.

Paths such as “/foo/bar/hello” or “/foo/bar/hello/world” can be added to the Router. Looking up these paths via the Router will return “hello handler” and “world handler” respectively. Should a path not be present such as “/foo/bar” None will be returned. Should the path “/foo/bar” be added either before or after the other paths, a look up of “/foo/bar” will now return “bar handler”. The path “/“ will always return “root handler”. 

Four extensive test cases and their output are included in the code.

## Time and Complexity Analysis 

### For the class `RouteTrieNode:`

- the insert method’s time and space complexity are both `O(1)`. This is because the insert method always inserts a single node to the Trie

### For the class class `RouteTrie:`

- the insert’s method time and space complexity are both `O(n)`, where n is the number path pieces in the url. For example: “/foo/bar/hello/world” yields n = 4. The insert loops through a list of piece strings e.g. [“foo", "bar". "hello", "world”] inserting into the Trie where needed. The method then has `O(n)` time complexity. Since the insert method can potentially add n new nodes to the Trie, its space complexity is also `O(n)`. 

- the find’s method time complexity is `O(n)` (n as defined above). Like the insert method, the find method starts at the root of the Trie attempting to the match the list of piece strings e.g. [“foo", "bar". "hello", "world”]. A full match then requires a time complexity of `O(n)`. Since the find method internal workings do not scale with the size of the piece strings list its space complexity is `O(1)`.


### For the class `Router`:

-the add_handler’s method time and space complexity are both `O(n)` (n as defined above). This follows from the add_handler directly calling the `RouteTrie's` insert method.

-the lookup method’s time complexity is `O(n)` (n as defined above). The space complexity is `O(1)`. This follows from the  lookup directly calling the `RouteTrie's` find method.

- the split_path’s method time and space complexity are both `O(n)` (n as defined above). The split_path is a helper method whic takes a url and returns a list of path pieces. For example: “/foo/bar/hello/world” yields a list of piece strings e.g. [“foo", "bar". "hello", "world”]. The split_path calls the Python method split("/") on the url yielding the required list. The time complexity is then `O(n)` (https://www.quora.com/What-is-the-runtime-for-Python-split-built-in-method), where n is the number path pieces in the url. Since the split_method's internal workings do not scale with the size of the piece strings list its space complexity is `O(1)`.
