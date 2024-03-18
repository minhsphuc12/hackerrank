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

"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

# Enter your code here. Read input from STDIN. Print output to STDOUT
# def decodeHuff(root, s):
	#Enter Your Code Here
    # dict_decode = {}
    # encrypted = ''
    # def build_decode(root:Node):
    #     print(root)
    #     global dict_decode
    #     global encrypted
    #     if root is None: 
    #         return
    #     dict_decode[encrypted] = root.data
    #     print(root.data)
    #     print(encrypted)
    #     encrypted += '0'
    #     build_decode(root.left)
    #     encrypted += '1'
    #     build_decode(root.right)
    # build_decode(root)
        
    # def traverse(root:Node):
    #     if root is None: 
    #         return None
    #     print(root.data)
    #     traverse(root.left)
    #     print(0)
    #     traverse(root.right)
    #     print(1)
    # traverse(root)
    
    # decoded = ''
    # cursor = 0
    # # s = '1001011'
    # while cursor < len(s):
    #     length = 1
    #     while s[cursor:(cursor+length)] not in dict_decode:
    #         length +=1 
    #     decoded_char = dict_decode[s[cursor:(cursor+length)]]
    #     decoded += decoded_char
    #     cursor += length
    # return decoded
        
def decodeHuff(root, s):
	#Enter Your Code Here
    
    index=0
    current=root
    decoded_string=''
    
    while index < len(s):
        
        if s[index] == '0':
            current = current.left
        else:
            current = current.right
            
        if current.left is None and current.right is None:
            decoded_string += current.data
            current = root
        
        index += 1
        
    print(decoded_string)
 

ip = input()
freq = {}#maps each character to its frequency

cntr = 0

for ch in ip:
    if(freq.get(ch) == None):
        freq[ch] = 1
    else:
        freq[ch]+=1

root:Node = huffman_hidden()#contains root of huffman tree
root.data
root.left.data
root.left.left.data
root.left.right.data
root.right.data

code_hidden = {}#contains code for each object

dfs_hidden(root, "")

if len(code_hidden) == 1:#if there is only one character in the i/p
    for key in code_hidden:
        code_hidden[key] = "0"

toBeDecoded = ""

for ch in ip:
   toBeDecoded += code_hidden[ch]

decodeHuff(root, toBeDecoded)
