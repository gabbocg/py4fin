# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 23:25:58 2021

@author: Habac
"""

def arithmetic_mean(n):
  output = sum(n) / len(n)
  return(output)

def net_present_value(cash_flow, rate):
   total = 0
   for i, num in enumerate(cash_flow):
     if i == 0:
       total += num
     else:
       total += num / (1 + rate) ** (i)
   return(total)