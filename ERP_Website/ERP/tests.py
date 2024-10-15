from django.test import TestCase

import datetime as dt
import os
# Create your tests here.

times = []
for i in range(5,19):
    times.append(str(i))

day_funcs = []
today = dt.date.today()


for i in range(7):
    newdate = today + dt.timedelta(i)
    dayname = newdate.strftime('%A')
    if dayname != "Thursday":
        dayname = dayname[:3].lower()
    else:
        dayname = dayname[:4].lower()
    day_funcs.append(dayname)


for day in day_funcs:
    for time in times:
        print(day, time)