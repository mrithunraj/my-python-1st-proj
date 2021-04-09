from xml.dom.minidom import *

m=xml.dom.minidom.parse('mmm.xml')

schl=m.documentElement

if schl.hasAttribute ('name'):
    print("the school name:",schl.getAttribute('name'))
          
clas=schl.getElementsByTagName('class')

for cla in clas:
          if cla.hasAttribute('name'):
               print("class name is:",cla.getAttribute('name'))
          Name=cla.getElementsByTagName('name')[0]
          print("Name:",Name.childNodes[0].data)

          Age=cla.getElementsByTagName('age')[0]
          print("Age:",Age.childNodes[0].data)

          Subject=clg.getElementsByTagName('subject')[0]
          print("Subject:",Subject.childNodes[0].data)
          
