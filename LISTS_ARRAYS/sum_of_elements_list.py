# Write a program to find the sum of all elements of a list.

# Examples

# 1. Input = [1, 2, 3, 4]
#    Output = 10

# 2. Input = [0,3,-1,2]
#    Output = 4

my_list = [1, 2, 3, 4, 5, 6]
sum_number = 0
for i in my_list:
    sum_number += i
print(sum_number)