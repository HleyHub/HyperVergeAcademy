# Given a year, report if it is a leap year.

#The tricky thing here is that a leap year in the Gregorian calendar occurs:
#```
#on every year that is evenly divisible by 4
#  except every year that is evenly divisible by 100
#    unless the year is also evenly divisible by 400
#```

#Examples
# 1997 is not a leap year
# 1996 is a leap year
# 1900 is not a leap year
# 2000 is a leap year

# Take input as the year and print: 
# 'Yes' if it is a leap year
# 'No' if it is not a leap year

year = int(input("Enter a year: "))
if (year % 400 == 0) and (year % 100 == 0):
    print("Yes")
elif (year % 4 == 0) and (year % 100 != 0):
    print("Yes")
else:
    print("No")