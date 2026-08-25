# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 11:52:26 2021

@author: Gabriel E. Cabrera
"""

#%%''' List (list) '''

'''1.a'''
faan = ['Facebook', 'Apple', 'Amazon', 'Netflix']

# no. of elements in the list
len(faan)

# only the first element
faan[0]

# only the second element
faan[1]

# only the third element
faan[2]

# only the last element
faan[3]

# all the elements
faan[:]

# first element plus all the rest
faan[0:]

# second element plus all the rest
faan[1:]

# first element up to the third element (inclusive), the interval will be [,)
faan[0:3]

# select everything using an index that does not exist in the list but is larger than the existing one
faan[0:1000]

'''1.b'''
# first element
faan[-4]

# last element
faan[-1]

'''1.c'''
faan.insert(0, 'Nvidia') # in-place
faan.insert(3, 'Nvidia') # fourth position (in-place)

'''1.d'''
faan.append('Google') # important (in-place) by default it is the last position

'''1.e'''
len(faan)

'''1.f'''
faan.index('Apple') # it will show the first position that contains the element, but not all the ones that exist in the list

'''1.g'''
# way 1
del faan[faan.index('Nvidia')] # it will show the first one
del faan[faan.index('Netflix')]

# way 2
faan.pop(faan.index('Nvidia')) # .pop() by default removes the last one
faan.pop(faan.index('Netflix'))

# way 3
faan.remove('Nvidia')
faan.remove('Netflix')

'''1.h'''
faan.sort(key=len)

#%%''' Tuple (tuple) '''

'''2.a'''
part_a = [[0, 'a'], [1, 'b']]
part_b = [[2, 'c'], [3, 'd']]

combined_list1 = part_a + part_b

# using extend
part_a.extend(part_b) # in-place

'''2.b'''
# elements in the nested list
combined_list1[0]
combined_list1[0][0]
combined_list1[0][1]


'''3.a'''
num_list = list(range(1, 11))

# sort
num_list.sort(reverse=True) # in-place

# sorted (bult-in)
sorted(num_list)

'''3.b'''
num_list[::2]

tuple_ = 1, 2, 'Facebook', 'Amazon'
tuple_

nested_tuple1 = (1,2), ('Facebook', 'Amazon')
nested_tuple1

nested_tuple2 = (1,2), ('Facebook', 'Amazon'), ['Apple', 'Netflix']
nested_tuple2

nested_tuple2[2].append('Google')
nested_tuple2

('Facebook', 'Amazon') + ('Apple', 'Netflix')

('Facebook', 'Amazon') * 3

tuple([1, 2, 3, 4])

#%%''' Dictionary (dict) '''

dict1 = {'Name' : 'Janet Yellen',
         'Country' : 'United States',
         'Profession' : ' United States secretary of the treasury',
         'Age' : 74}

type(dict1)

print(dict1['Name'], dict1['Age'])

dict1.keys() # keys

dict1.values() # values

dict1.items()  # items = keys + values

#%%''' Set (set) '''

set1 = set([1, 2, 3, 4, 5, 5])
set1

set2 = set([3, 4, 5, 6, 9, 9, 7])
set2

# union
set1.union(set2)

# intersection
set1.intersection(set2)

set1.difference(set2)

set2.difference(set1)

set1.symmetric_difference(set2)
