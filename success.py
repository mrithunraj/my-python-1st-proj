from xml.dom.minidom import *

s=xml.dom.minidom.parse('xml.xml')

shopName=s.documentElement

if shopName.hasAttribute('name'):
    print("The Shop name : ",shopName.getAttribute('name'))
drinks = shopName.getElementsByTagName('drink')

for drink in drinks:
    if drink.hasAttribute('name'):
       print ("Drink name is : ", drink.getAttribute('name'))

    Name=drink.getElementsByTagName('name')[0]
    print("Name: ", Name.childNodes[0].data)
    rate=drink.getElementsByTagName('rate')[0]
    print("Rate: ", rate.childNodes[0].data)
    color=drink.getElementsByTagName('color')[0]
    print("Color: ", color.childNodes[0].data)
    
