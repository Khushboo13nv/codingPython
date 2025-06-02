# Project Euler 
# Problem - 4

#-----------------------------------------------------------------------------------
# A palindromic number reads the same both ways. The largest palindrome made from 
# the product of two 2-digit numbers is 9009=91x99.

# Find the largest palindrome made from the product of two 3-digit numbers.
#-----------------------------------------------------------------------------------

# Palindromic number:

import numpy as np
import sys

def palindronic_num(N_start, N_end):
    numbers = []
    for i in np.arange(N_start, N_end,1):
        for j in np.arange(N_start, N_end,1):
            num = str(i*j)
            n = len(num)
            for k in range(n):
                palin_num = False
                if num[k] != num[(n-1)-k]:
                    break                    
                else: 
                    palin_num = True
            if palin_num == True:
                numbers.append(int(num))
    return numbers


number_list = palindronic_num(100, 1000)
large_num = np.max(number_list)
# print(number_list)
print(large_num)

