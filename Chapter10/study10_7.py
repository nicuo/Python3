from datetime import date
from datetime import timedelta
my_day = date(2017,8,1)
print (my_day)
print (my_day.weekday())

party_day = my_day + timedelta(days=10000)
print(party_day)
