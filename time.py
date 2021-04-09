from datetime import *

d=datetime.today()
print(d)

t=datetime.now()
print(t)

w=datetime.weekday(t)
print(w)

print(t.day)
print(t.month)
print(t.year)

print(t.strftime ("%Y"))
print(t.strftime ("%y"))
print(t.strftime ("%A"))
print(t.strftime ("%a"))
print(t.strftime ("%B"))
print(t.strftime ("%b"))

print(t.strftime ("%x"))
print(t.strftime ("%X"))

print(t.strftime ("%D"))
print(t.strftime ("%d"))
print(t.strftime ("%m"))


print(t.strftime ("%c"))
print(t.strftime ("%H"))

print(t.strftime ("%M"))
print(t.strftime ("%S"))
print(t.strftime ("%p"))


from datetime import timedate

print(t+timedelta(hours=-2))




































