# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 23:25:58 2021

@author: Habac
"""
#%%''' Applications '''

'''1.a'''
def sum_of_squares(n):
  total = 0
  for i in range(1,n+1):
    total += i ** 2
  return(total)

sum_of_squares(5)

'''1.b'''
def divisible(n):
  if (n % 4) == 0:
    return(print('The number '+str(n)+' is divisible by 4.'))
  else:
    return(print('The number '+str(n)+' is not divisible by 4.'))

divisible(16)

'''1.c'''
def arithmetic_mean(n):
  output = sum(n) / len(n)
  return(output)

arithmetic_mean([1,2,3,4,5])

'''1.d'''
def net_present_value(cash_flow, rate):
   total = 0
   for i, num in enumerate(cash_flow):
     if i == 0:
       total += num
     else:
       total += num / (1 + rate) ** (i)
   return(total)

cash_flows = [-500000,100000,150000,180000,200000,300000]

net_present_value(cash_flows, 0.12)

#%%''' Anonymous Functions (Lambda) '''

seq = [1, 2, 4]

def apply_to_a_list(list_, f):
    return [f(x) for x in list_]

apply_to_a_list(seq, lambda x: x ** 2)

#%%''' Importing Functions'''

# it must be in the same directory, if you use * instead of the name of each function all the available functions are loaded
from helper_functions import arithmetic_mean, net_present_value

# function from 1.3
arithmetic_mean([1,2,3,4,5])

# function from 1.4
cash_flows = [-500000,100000,150000,180000,200000,300000]

net_present_value(cash_flows, 0.12)
