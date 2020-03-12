"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.

   input None
   if
   print current datetime

 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.

   input arg1 only
   if
   print month of current year datetime?

 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.

   input arg1 arg2
   if
   print month of year

 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

   else
   this should actually be paired with the first parameter/functionality above
   print("program expects arguments to be given")


Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime



if len(sys.argv) > 2:
  month = int(sys.argv[1])
  year = int(sys.argv[2])
elif len(sys.argv) > 1:
  month = int(sys.argv[1])
else:
  month = 0
  year = 0

# print(sys.argv)
# print(month)
  
current_year = datetime.today().year
current_month = datetime.today().month

# print(current_year)
# print(current_month)
# print(calendar.TextCalendar().prmonth(current_year,3, w=0, l=0))
#DONT FORGET TO INSTANTIATE TEXTCALENDAR!!!!!!!!!!!!!!

def print_calendar(year, month):
  if year < 1 and month < 1:
    print("program expects arguments to be given")
    print(calendar.TextCalendar().prmonth(current_year, current_month))
  elif month > 0 and year < 1:
    print(calendar.TextCalendar().formatmonth(current_year, month))
  else:
    print(month)
    print(calendar.TextCalendar().formatmonth(year, month) + " " + calendar.TextCalendar().formatyear(year))


print_calendar(year, month)