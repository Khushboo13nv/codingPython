# Website: https://projecteuler.net/archives
# Project Euler 
# Problem - 1

# ---------------------------------------------------------------------------
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of 
# all the multiples of 3 or 5 below 1000.
# ---------------------------------------------------------------------------

import numpy as np

# Multiple of 3 or 5
multiple_of_three_five = []
for i in range(999):
    #print(i)
    if (i+1)%3 == 0 or (i+1)%5 == 0: # % modulus operator: used to find remainder
        multiple_of_three_five.append(i+1)
        #print(i)

multiple_of_three_five_sum = np.sum(multiple_of_three_five)
print(multiple_of_three_five_sum)
