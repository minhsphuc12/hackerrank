#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

def noPrefix(words):
    # Write your code here
    for i, w in enumerate(words):
        remain = words[:i]# + words[(i+1):]
        for w2 in remain:
            if w2.startswith(w) or w.startswith(w2):
                print('BAD SET')
                print(w)
                return
                # print('BAD SET')
                # print(w)
                # return
    print('GOOD SET') 

class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode() # create new node on this node children if current character not exist in this node "children"
            node = node.children[i] # move to next node
            if node.word: # if current node is end of word, mean a current inserting word is using existed word as prefix, then return False
                return False
        if node.children:
            return False # if at the end of insertion, there is still some children left, then this inserting word is prefix of another existed word, return Fasle
        node.word = True # if no violation, mark current inserted node as new end of word, add this to vocab.
        return True

trie = Trie()
trie.insert('abcd')
trie.root.word
trie.root.children['a'].children

def noPrefix(words):
    trie = Trie()
    for s in words:
        if not trie.insert(s):
            print("BAD SET")
            print(s)
            return
    print("GOOD SET")
    return
    
words = ['ab', 'bc', 'cd']
noPrefix(words)
words = ['abcd', 'bcd', 'abcde', 'bcde']
noPrefix(words)
words = open('one-week-preparation-kit/day_7/test_case_1', 'r').read().split('\n')
noPrefix(words)
words = open('one-week-preparation-kit/day_7/test_case_2', 'r').read().split('\n')
noPrefix(words)


if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
