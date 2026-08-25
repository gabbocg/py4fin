# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 22:26:45 2021

@author: Gabriel E. Cabrera
"""

#%%""" Variables """

# = assignment operator (not the only one)
phone_number = 12345678 # the symbol = is the assignment operator
phone_number

a = 1; b = 2; c = 3

a, b, c = 1, 2, 3

#%%""" Conventions """

# library
import keyword

# reserved keywords
keyword.kwlist

# this is a single-line comment

"""
this
is
a
multi-line
comment
"""

#%%""" Data Types (scalars) """

'''Basic data types'''
# integers
integer = 2
type(integer) # identification
isinstance(integer, int)  # identification

# float
floating = 3.14
type(floating)
isinstance(floating, float)

# string
string = "hello world"
type(string)
isinstance(string, str)

# boolean
boolean = True
type(boolean)
isinstance(boolean, bool)

'''casting'''
# integers
int('1')
int(True)
int(False)

# float
float('1')
float(True)
float(False)

# string
str(1)
str(True)
str(False)

# boolean
bool(1)
bool(0)

#%%
"""
Numeric Expressions
"""

'''1'''
a = 4
b = 3

# addition
a + b

# subtraction
a - b

# multiplication
a * b

# division
a / b

# modulo
a % b

# integer part
a // b

# power
a ** b

'''2'''
1 + 2 ** 3 / 4 * 5

'''3'''
present_value = 1000 / (1 + 0.1) ** 1 +  1000 / (1 + 0.1) ** 2 + 1000 / (1 + 0.1) ** 3 + 1000 / (1 + 0.1) ** 4 + 1000 / (1 + 0.1) ** 5
print('The present value is: ' + str(present_value))

#%%
"""
Strings
"""

'''1.a'''
text = "There are some things money can't buy, for everything else there's mastercard"
len(text)

# first character
text[0]

# first 5 characters
text[0:5]

# last character
text[-1]

'''1.b'''
text.count('r')
text.count('r', text.find(','))

'''1.c'''
text.find('mastercard')

'''1.d'''
text.replace('mastercard', 'Mastercard')


'''2.a'''
lower_name = "guido von rossum"
lower_name.upper()

'''2.b'''
lower_name.title()


'''3'''
# https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting
template = '{0:.2f} {1:s} is equivalent to $CLP{2:d}'
template.format(2.45535, 'dollars', 1808)


'''4'''
# concatenation, both must be str()
'2' + '25'

#%%
"""
Boolean Logic
"""

'''1'''
a = 4
b = 3

'''comparison operators'''
# greater than
a > b

# less than
a < b

# equal to
a == b

# not equal to
a != b

# greater than or equal to
a >= b

# less than or equal to
a <= b

''' logical operators'''
x = True
y = False

# True and False = False
x and y

# True or False = True
x or y

# not True = False
not x


'''2'''
text = "There are some things money can't buy, for everything else there's mastercard"

# membership operator
'''2.a'''
'z' in text

'''2.b'''
'm' in text

'''2.c'''
'visa' in text


'''3'''
A = True
B = False

not(A and B) == (not(A) or not(B))

A = False
B = True

not(A and B) == (not(A) or not(B))

A = True
B = True

not(A and B) == (not(A) or not(B))

A = False
B = False

not(A and B) == (not(A) or not(B))
