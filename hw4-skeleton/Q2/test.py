# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 19:01:35 2019

@author: yao_p
"""

#%%
def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))