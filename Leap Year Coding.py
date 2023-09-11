#Program to check a year is leap year or not
def isLeapYear(year):
  return bool(year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
year=(int(input("Enter the year:")))
if isLeapYear(year):
  print("{} is leap year".format(year))
else:
  print("{} is not leap year:".format(year))
    
