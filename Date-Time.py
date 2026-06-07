#importing datetime modules as dt (short form)
import datetime as dt
# store today's date in a variable
today = dt.date.today()
#printing today's date
print(today.month)
print(today.day)
print(today.year)

#storing a date
new_year = dt.date(2027,1,1)
print(new_year.month)
print(new_year.day)
print(new_year.year)

#days left to new year
days = new_year - today
print(days)

