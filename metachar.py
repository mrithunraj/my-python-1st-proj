#metacharacter

import re

'''txt="The rain in Spain"

a=re.search("^The .*Spain",txt)

if(a):
    print("YES! we have a match")
else:
    print("No mactch")

#[a-z]

import re

txt="The rain in Spain"

a=re.findall("[a-z]",txt)
print(a)

a=re.findall("[A-Z]",txt)
print(a)

#{}

import re

txt="The rain in Spaiiiiiin"

a=re.findall("ai{5}",txt)
print(a)


#\d:"it will check digits in characters"

import re

txt="The price will be 7786pounds"

a=re.findall("\d",txt)
print(a)

#..

txt="hi mrithunraj"

a=re.findall("h..........a",txt)
print(a)'''


#speical sequences

'''import re

txt="The rain in Spain"

a=re.findall("\AThe",txt)
print(a)

if(a):
    print("Yes,we have a match!")
else:
    print("No match")'''

'''import re

txt="The rain in Spain"

a=re.findall("\Bain",txt)
print(a)

if(a):
    print("Yes,we have a match!")
else:
    print("No match")

#Z-it will check the word is present end,but NOT at the end of a word:

a=re.findall("ain\Z",txt)
print(a)

if(a):
    print("Yes,we have a match!")
else:
    print("No match")'''


##
import re

txt="The word58 is Python39"

a=re.findall("\d",txt)
print(a)

if(a):
    print("Yes,there is at least one match!")
else:
    print("No match")


##

import re

txt="The number8056094363 is Present"

a=re.findall("\D",txt)
print(a)

if(a):
    print("Yes,there is match!")
else:
    print("No match")


##

import re

txt="I am studying Python"

a=re.findall("\s",txt)
print(a)

if(a):
    print("Yes,there is a match")
else:
    print("No match")



import re

txt="I am studying Python"

a=re.findall("\S",txt)
print(a)

if(a):
    print("Yes,there is a match")
else:
    print("No match")



import re

txt="I am studying Python"

a=re.findall("\w",txt)
print(a)

if(a):
    print("Yes,there is a match")
else:
    print("No match")



import re

txt="I am studying Python"

a=re.findall("\W",txt)
print(a)

if(a):
    print("Yes,there is a match")
else:
    print("No match")



#sets:

import re

txt="I am learning Python"

a=re.findall("[^srn]",txt)
print(a)

 
if(a):
    print("Yes,there is a match")
else:
    print("No match")
    

txt="I am learning Python39045"

a=re.findall("[0123456789105]",txt)
print(a)


if(a):
    print("Yes,there is a match")
else:
    print("No match")

txt="My time is now 12.30PM"

a=re.findall("[0-9]",txt)
print(a)

if(a):
    print("Yes,there is a match!")
else:
    print("No match")


import re

txt="My time is now 12.48PM"

a=re.findall("[0-4][0-9]",txt)
print(a)

if(a):
    print("Yes,there is a match!")
else:
    print("No match")


import re

txt="My time is now 12.48PM"

a=re.findall("[a-zA-Z]",txt)
print(a)

if(a):
    print("Yes,there is a match!")
else:
    print("No match")

import re

txt="My time is now 12.48PM"

a=re.findall("[.]",txt)
print(a)

if(a):
    print("Yes,there is a match!")
else:
    print("No match")



#findall

import re

txt="The rain in Spain"

a=re.findall("in",txt)
print(a)


#search

import re

txt="The rain in Spain"

a=re.findall("in",txt)
print(a)

#split

txt="The rain in Spain"

a=re.split("\S",txt)
print(a)


#sub

import re

txt="The rain in Spain"

a=re.sub("\s","--",txt)
print(a)









    













    





                  
    


















































