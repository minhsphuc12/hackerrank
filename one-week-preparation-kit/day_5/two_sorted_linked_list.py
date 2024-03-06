#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

list1 = SinglyLinkedList()
list2 = SinglyLinkedList()
list1.insert_node(1);list1.insert_node(2);list1.insert_node(3)
list2.insert_node(3);list2.insert_node(4)
head1 = list1.head
head2 = list2.head

list3 = SinglyLinkedList()
current_node_head1 = head1
current_node_head2 = head2

stop = False

while not stop:
    if current_node_head1 is None and current_node_head2 is not None or (current_node_head1 is not None and current_node_head2 is not None and current_node_head1.data >= current_node_head2.data):
        list3.insert_node(current_node_head2.data)
        current_node_head2 = current_node_head2.next

    if current_node_head2 is None and current_node_head1 is not None or (current_node_head2 is not None and current_node_head1 is not None and current_node_head1.data < current_node_head2.data):
        list3.insert_node(current_node_head1.data)
        current_node_head1 = current_node_head1.next

    if current_node_head1 is None and current_node_head2 is None:
        stop = True

print_singly_linked_list(list3.head, sep='-', fptr = open('test_data', 'w'))

# other

l1, l2 = [], []
node = head1
while node:
    l1.append(node.data)
    node = node.next
node = head2
while node:
    l2.append(node.data)
    node = node.next
l3 = sorted(l1+l2)
list3 = SinglyLinkedList()
for i in l3:
    list3.insert_node(i)
