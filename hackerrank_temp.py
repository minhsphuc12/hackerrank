# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

string = 'hello'
string

col = [1,2,4,7,3,5,4,3,3]

for i, value in enumerate(col):
    print('index is {}'.format(i) + ' value is {}'.format(value))
#    print()

mapping = {}
for i, value in enumerate(col):
#    mapping[value] = i
    print(i, value)
from collections import Counter
for i in Counter(col):
    print(i)

a = Counter(col)
a[4]
mapping

zipped = zip(col, col, [1,2])
#zipped.list()
list(zipped)

unzip = [(1,2), (3,4), (5,6)]
fname, lname = zip(*unzip)
fname
lname
list(reversed(unzip))

d1 = {'a' : 'some value', 'b' : [1, 2, 3, 4]}
'a' in d1
# d1[] = [12]
d1.pop('a')

mapping = dict(zip(col, reversed(col)))

words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}
for word in words:
    word= 'atom'
    letter = word[0]
    if letter not in by_letter:
        by_letter[letter] = [word]
    else:
        by_letter[letter].append(word)

for word in words:
    letter = word[0]
    by_letter.setdefault(letter, []).append(word)

from collections import defaultdict
by_letter = defaultdict(list)
for word in words:
    by_letter[word[0]].append(word)

hash([1,'a'])

set([1,1,2])


#import libraries
import numpy as np
import pandas as pd


a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}
a|b
a.union(b)
a.difference_update(b)
a.intersection_update(b)

d = [1]
d.copy()
c = a.copy()
# c = copy(a)

strings = ['nguyen minh phuc', 'ed', 'a', 'edd']
unique_length = {len(x) for x in strings}
{1,3,4,2}
{val:index for index, val in enumerate(strings)}
{index for index in enumerate(strings)}

all_data = [['John', 'Emily', ['Michael', 'blee'], 'Mary', 'Steven'],
            ['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]

[name for names in all_data for name in names if name.count('e')>=2]

[name for list_names in all_data for names in list_names for name in names
     if name.count('e')>=2]

flatten = lambda l: [name for list_names in all_data for names in list_names for name in names]
flatten(all_data)

somedict = {'a':1, 'b': 2}

# generator ------
def squares(n= 10):
    for i in range(1, n+1):
        yield i**2

gen = squares(15)
for i in gen: print(i)
[print(i) for i in gen]
[i**2 for i in iter(a)]
a = (x**2 for x in range(15))
for i in a: print(i)

import itertools
first_letter = lambda x:x[0]
names = ['phuc', 'colin', 'co']

for letter, namesz in itertools.groupby(names, first_letter): print(letter, list(namesz))

for i in itertools.combinations(names, r = 2): print(i)

def attempt_float(x):
	try:
		return float(x)
	except (ValueError, TypeError):
		return x

attempt_float((1,2))
# write_to_file()

# 1 4
# 1 2 3 4
# 5 6 7 8
import numpy as np
n, m = map(int, input().split())
n, m = int(input().split())
x= ('1', '2')
x.int()
a = np.zeros([n, m])
b = np.zeros([n, m])

a[0]= np.array(input().split(), int)
(x for x in range(4))
a, b = (np.array([input().split() for _ in range(n)], dtype = int) for _ in range(2))

print(a+b, a-b, a*b, a//b, a%b, a**b, sep = '\n')

a = np.array(input().split(' '), dtype = float)

np.floor(a)
print(np.floor(a))
np.ceil(a)
np.rint(a)
# print(np.array2string(np.floor(a), np.ceil(a), np.rint(a), sep = '\n')
print(np.floor(a), sep = ' ')
(map(lambda x: print(np.array2string(x, sign = ' ')), (np.floor(a), np.ceil(a), np.rint(a))))
np.floor(a)
import string
print('['+''.join([' '+str(i) for i in np.floor(a)])+']')
print('['+''.join([' '+str(i) for i in np.ceil(a)])+']')
print('['+''.join([' '+str(i) for i in np.rint(a)])+']')

print(np.array2string(np.floor(a), sign = ' ', prefix = '', separator = ' '))

n, m = map(int, input().split())
a = np.array([input().split() for _ in range(n)], dtype = int)
print(np.prod(np.sum(a, axis = 0)))

a = np.array([[1,2,3], [2,3,4]])
a.shape
print(np.array2string(np.mean(a, axis = 1), sign = ' '), np.array2string(np.var(a, axis = 0), sign = ' '), np.std(a, axis = None), sep = '\n')
np.set_printoptions(legacy = '1.2')
np.set_printoptions(precision = 1)

n = int(input())
a, b = (np.array([input().split() for _ in range(n)], dtype = int) for _ in range(2))

np.dot(a,b)
np.cross(a,b)
c = np.array([[(1.5,2,3), (4,5,6)], [(3,2,1), (4,5,6)]],dtype = float)
np.info(a)
a,b
np.inner(a,b)
np.outer(a, b)
print(np.inner(a,b), np.outer(a,b), sep = '\n')
int(np.inner(a,b))
[i for i in range(1)]

a, b = (np.array([input().split() for _ in range(1)], dtype = int) for _ in range(2))

a = np.array(input().split(), dtype = float)
x = int(input())
np.polyval(a, x)

n = int(input())
a = np.array([input().split() for _ in range(n)], dtype = float)
np.set_printoptions(legacy = '1.13')
print(np.linalg.det(a))

s = str(input())
import itertools as it
gr = it.groupby(s, key = None)
gr_count = [(len(list(y)), int(x)) for (x,y) in gr]

for i in gr_count: print (i, sep = '', end = ' ')

n = int(input())
nlist = input().split()
k = int(input())

all_com = list(it.combinations(nlist, k))
def detect_a(x):
	if 'a' in x:
		return 1
	else:
		return 0

def avg(x): return sum(x) / len(x)
print(float(avg(list(map(detect_a, all_com)))))
round(0.83333333333333337,4)

k, m = map(int, input().split())
s = [list(map(int, input().split()))[1:] for _ in range(k)]
all_com = list(it.product(*s))
print(max([sum(x**2 for x in com)%m for com in all_com]))
