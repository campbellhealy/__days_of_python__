# what_date
'''
  Calculates the new `datetime.datetime` value after adding `n` days to `d`.
'''
from os import system
import datetime
from datetime import date, datetime, timedelta

system('cls')
# print(dir(datetime)) # Attributes of datetime
# print(dir(timedelta)) # Attributes of timedelta
# print(format(datetime)) # class
# print(date.today()) # Date  YYYY-mm-DD
# print(date.today().strftime('%d-%m-%y'))  # Reorder the date - split, YY year
# print(date.today().strftime('%d-%m-%Y'))  # Reorder the date - split, YYYY year
# print(date.today().strftime('%D'))  # Reorder the date / split
# print( datetime.now()) # DTS YYYY-mm-DD HH:MM:SS
# print(date.fromtimestamp(1689244364)) # dts from a timestamp
# print(date.today().year)
# print(date.today().month)
# print(date.today().day)

def what_date(n, d):
  print(d + timedelta(n)) # Default Format
  fd = d + timedelta(n)
  fd = fd.strftime('%d-%m-%Y') # Using formatting
  return fd

print(what_date(3, date(1970, 12, 20)) )