from datetime import *

d=datetime.today()
print(d)

t=datetime.now()
print(t)

w=datetime.weekday(d)

print(w)


print(d.day)
print(d.month)
print(d.year)

print(t.strftime("%Y"))
print(t.strftime("%y"))
print(t.strftime("%A"))
print(t.strftime("%a"))
print(t.strftime("%B"))
print(t.strftime("%b"))

print(t.strftime("%x"))
print(t.strftime("%X"))

print(t.strftime("%D"))
print(t.strftime("%d"))
print(t.strftime("%m"))

print(t.strftime("%c"))

print(t.strftime("%H"))
print(t.strftime("%M"))

print(t.strftime("%S"))

print(t.strftime("%p"))

print(t.strftime("%H--%M--%S %D-%m-%Y"))

from datetime import timedelta

print(t+timedelta(hours=-2))
print(t+timedelta(days=4))

import calendar
import time
print(calendar.prcal(2021))

print(calendar.isleap(2020))

print(calendar.monthrange(2021,4))

print(calendar.weekday(2021,3,12))


print(time.localtime())































