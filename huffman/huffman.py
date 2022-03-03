import queue as Queue

cntr = 0

class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None
        global cntr
        self._count = cntr
        cntr = cntr + 1
        
    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self._count < other._count

def huffman_hidden():#builds the tree and returns root
    q = Queue.PriorityQueue()

    
    for key in freq:
        q.put((freq[key], key, Node(freq[key], key) ))
    
    while q.qsize() != 1:
        a = q.get()
        b = q.get()
        obj = Node(a[0] + b[0], '\0' )
        obj.left = a[2]
        obj.right = b[2]
        q.put((obj.freq, obj.data, obj ))
        
    root = q.get()
    root = root[2]#contains root object
    return root

def dfs_hidden(obj, already):
    if(obj == None):
        return
    elif(obj.data != '\0'):
        code_hidden[obj.data] = already
        
    dfs_hidden(obj.right, already + "1")
    dfs_hidden(obj.left, already + "0")
# --------- START SOLUTION ----------
"""
https://www.hackerrank.com/challenges/one-week-preparation-kit-tree-huffman-decoding/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-seven&h_r=next-challenge&h_v=zen

class Node:
    def __init__(self, freq,data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None
"""
# S="1001011"
# Processing the string from left to right.
# S[0]='1' : we move to the right child of the root. We encounter a leaf node with value 'A'. We add 'A' to the decoded string.
# We move back to the root.
# 
# S[1]='0' : we move to the left child. 
# S[2]='0' : we move to the left child. We encounter a leaf node with value 'B'. We add 'B' to the decoded string.
# We move back to the root.
# 
# S[3] = '1' : we move to the right child of the root. We encounter a leaf node with value 'A'. We add 'A' to the decoded string.
# We move back to the root.
# 
# S[4]='0' : we move to the left child. 
# S[5]='1' : we move to the right child. We encounter a leaf node with value C'. We add 'C' to the decoded string.
# We move back to the root.
# 
#  S[6] = '1' : we move to the right child of the root. We encounter a leaf node with value 'A'. We add 'A' to the decoded string.
# We move back to the root.
# 
# Decoded String = "ABACA"

from collections import deque
def decodeHuff(root, s):
    # Handle trivial case.
    if len(s) == 1:
        print(root.data, end="")
        return
    
    # Handle regular cases.
    current = root
    for character in s:
        children = {"1": current.right, "0": current.left}
        child = children[character]
        if child:
            if child.data != "\x00":
                print(child.data, end="")
                current = root
            else:
                current = child
# --------- END SOLUTION ----------
ip = input()
freq = {}#maps each character to its frequency

cntr = 0

for ch in ip:
    if(freq.get(ch) == None):
        freq[ch] = 1
    else:
        freq[ch]+=1

root = huffman_hidden()#contains root of huffman tree

code_hidden = {}#contains code for each object

dfs_hidden(root, "")

if len(code_hidden) == 1:#if there is only one character in the i/p
    for key in code_hidden:
        code_hidden[key] = "0"

toBeDecoded = ""

for ch in ip:
   toBeDecoded += code_hidden[ch]

decodeHuff(root, toBeDecoded)
