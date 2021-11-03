#  print the calendar of a given month and year

import calendar

y = int(input("Enter a year: "))
m = int(input("Enter a month: "))
print(calendar.month(y, m))

# program to calculate number of days between two dates.

from datetime import date

f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days, "days")

# get the difference between a given number and 17, if the number is greater than 17 return double the
# absolute difference

number = 15
if number > 17:
    difference = number - 17
    final_value = difference * 2
    print(final_value)
else:
    print(17 - number)

# calculate the sum of three given numbers, if the values are equal then return three times of their sum.

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))#
total = n1 + n2 + n3
if n1 == n2 == n3:
    total *= 3
    print(total)
else:
    print(total)


# count the number 4 in a given list.

given_list = [7, 9, 4, 5, 67, 9, 12, 4, 8, 4, 56, 13, 4]
count = 0
for item in given_list:
    if item == 4:
        count = count + 1

print(count)




