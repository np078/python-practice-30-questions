'''
Q13: Write a Python program that prints the calendar for a given month and year.
Note : Use 'calendar' module.
'''
# Solution
import calendar

y= int(input("Enter the year: "))
m = int(input("Enter the month: "))

print(calendar.month(y,m))