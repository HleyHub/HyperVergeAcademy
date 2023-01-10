# An Armstrong number(https://en.wikipedia.org/wiki/Narcissistic_number) is a number that is the sum of its own digits each raised to the power of the number of digits. Determine whether a number is an Armstrong number.

# Examples
# 9 is an Armstrong number, because `9 = 9^1 = 9`
# 10 is *not* an Armstrong number, because `10 != 1^2 + 0^2 = 1`
# 153 is an Armstrong number, because: `153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153`
# 154 is *not* an Armstrong number, because: `154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190`

# Take the number as input, and print:
# "Yes" if it is an Armstrong Number
# "No" if it is not an Armstrong Number

number = int(input("Enter a number: "))
length_number_of_digits = len(str(number))
sum_digit = 0
temp = number
while temp > 0:
    digit = temp % 10
    sum_digit += digit ** length_number_of_digits  
    temp //= 10

if number == sum_digit:
    print("Yes")
else:
   print("No")