# Website: https://projecteuler.net/archives

# Project Euler 
# Problem - 6

#--------------------------------------------------------------------------------
# The sum of the squares of the first ten natural numbers is, 
# 1^2 + 2^2 + ... + 10^2 = 385.

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the first ten natural 
# numbers and the square of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred 
# natural numbers and the square of the sum.
#---------------------------------------------------------------------------------


N = int(input("Enter total number of terms of natural numbers:"))
num_sq_sum = 0
num_sum = 0
for i in range(1,N+1):
    num_sq_sum = i**2 + num_sq_sum
    num_sum = i + num_sum

result = num_sum**2 - num_sq_sum

print(result)
