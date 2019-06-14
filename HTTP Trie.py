#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 19:23:45 2019

@author: joscelynec
"""

"""
The purpose of an HTTP Router is to take a URL path like "/", 
"/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure 
out what content to return. In a dynamic web server, 
the content will often come from a block of code called a handler.

We could split the path into letters similar to how we did the autocomplete Trie, 
but this would result in a Trie with a very large number of nodes and lengthy 
traversals if we have a lot of pages on our site. A more sensible way to split 
things would be on the parts of the path that are separated by slashes ("/"). 
A Trie with a single path entry of: "/about/me" would look like:

(root, None) -> ("about", None) -> ("me", "About Me handler")

We can also simplify our RouteTrie a bit by excluding the suffixes 
method and the endOfWord property on RouteTrieNodes. We really just 
need to insert and find nodes, and if a RouteTrieNode is not a leaf node,
it won't have a handler which is fine.

For this problem you need to create three classes:

RouteTrie should be similar to the Trie class you created for Problem 5. 
You won't need the exists method. Each node that represents the end of a 
valid path will need to store a handler.

RouteTrieNode is used to encapsulate each node in the Trie. 
This will store the handler, and link to all of the children of the node.

Router is the class that code will interact with to add and lookup routes. 
This is the class that your test cases will call. It will initialize a Trie, 
and handle splitting up paths into a list so that you can use a path string with the Trie.
Each node in the trie will be a path part. So if the path is /foo/bar/hello, then foo, bar, 
and hello will each be separate nodes. If you had the following two paths:

/foo/bar/hello
/foo/bar/hello/world
... then both paths will lay along the same branch of the Trie. 
The hello node and world node will both have handlers.
If you then added a path like /foo/bar/udacity, then bar would have 
two children: {hello, udacity}.

"""

class RouteTrieNode:
    def __init__(self, handler = None):
        self.handler = handler
        self.children = {}
    
    def insert(self, path_piece, handler):
         self.children[path_piece] = RouteTrieNode()
         
    def __repr__(self):
        return str(self.children)

 
class RouteTrie:
    def __init__(self):
        self.root = RouteTrieNode("root handler")

     
    def insert(self, path, handler):
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        #Set current node to root
        current_node = self.root
        #Set length of path
        for path_piece in path:
            if path_piece not in current_node.children.keys():
                current_node.children[path_piece] = RouteTrieNode('not found handler')
            #Advance current node
            current_node = current_node.children[path_piece]
        #Insert handler tp current node
        current_node.handler = handler
        

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match 
        #This handles the root "/" returns "root handler"
        if len(path) == 0:
            self.root.handler
        #Set current node to root
        current_node = self.root
        for path_piece in path:
            if path_piece not in current_node.children.keys():
                return "not found handler"
            #Advance current node
            current_node =  current_node = current_node.children[path_piece]
        #If successfully reached the path's end return current node's children handler
        return current_node.handler


# The Router class wraps the RouteTrie class 
      
class Router:
    def __init__(self, handler):
        self.route_trie = RouteTrie()
        self.route_trie.root.handler = handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        path_pieces = self.split_path(path)
        self.route_trie.insert(path_pieces , handler)
        

    def lookup(self,path):
        # lookup path (by parts) and return the associated handler
        path_pieces = self.split_path(path)
        return  self.route_trie.find(path_pieces)
        
    def split_path(self, path):
        return path[1:]#This removes the initial empty string = ""
    
# Test 0   
router1 = Router("root handler") 
router1.add_handler("/", "root handler") 
print("********** Test 0 ***********")
print(router1.lookup("/")) # should print 'root handler'   

# Test 1
router1 = Router("root handler") 
router1.add_handler("/home/about", "about handler")  # add a route

print("********** Test 1 ***********")
print(router1.lookup("/")) # should print 'root handler'
print(router1.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router1.lookup("/home/about")) # should print 'about handler'
print(router1.lookup("/home/about/")) # should print not found handler does not handle trailing slashes
print(router1.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
router1.add_handler("/home/about/me", "me handler") 
print(router1.lookup("/home/about/me"))# should print 'me handler'
print(router1.lookup("/home/about"))# should print 'about handler'

# Test 2
router2 = Router("root handler") 
router2.add_handler("/foo/bar/hello", "hello handler")
router2.add_handler("/foo/bar/udacity", "udacity handler")
router2.add_handler("/foo/bar/hello/world", "world handler")
print("********** Test 2 ***********")
print(router2.lookup("/"))
print(router2.lookup("/foo/bar/udacity"))
print(router2.lookup("/foo/bar/hello"))
print(router2.lookup("/foo/bar/udacity"))
print(router2.lookup("/foo/bar/hello/world"))
print(router2.lookup("/foo/bar"))
print(router2.lookup("/foo/ba"))

# Test 3
router3 = Router("root handler") 
router3.add_handler("/about/pets/four legs", "four legs handler")
router3.add_handler("/about/pets/four legs/dogs/white dogs/bichon frise", "bichon frise handler")
print("********** Test 3 ***********")
print(router3.lookup("/"))
print(router3.lookup("/about/pets/four legs/dogs/white dogs/bichon frise"))
print(router3.lookup("/about/pets/four legs"))
print(router3.lookup("/about"))
"""
********** Test 0 ***********
root handler
********** Test 1 ***********
root handler
not found handler
about handler
not found handler
not found handler
me handler
about handler
********** Test 2 ***********
root handler
udacity handler
hello handler
udacity handler
world handler
not found handler
not found handler
********** Test 3 ***********
root handler
bichon frise handler
four legs handler
not found handler
"""