a=int(input("enter a value"))

if a<65:
    print("the less value")
elif a>91:
    print("the large value")
else:
    print(chr(a))

a=[]
def name():
    b=input("enter a text")
    a.append(b.lower())
    print(a)

name()
name()
name()
name()
name()

class vechile:
    def route(self,rout):
        print("route is:",rout)

    def colour(self,colou):
        print("colour is:",colou)

class bus(vechile):
    def trip(self,tr):
        print("trip:",tr)


b=bus()
b.route("medavakkam")
b.colour("blue")
b.trip("5")

list1=["m","na","i","ke"]
list2=["y","me","n","lly"]
list3=[1,2,3,4]

for i in range(0,len(list1)):
                    list3[i]=list1[i]+list2[i]
                

    

print(list3)



a=[1,2,3,4,5,6,7]

square_a=[a **2 for a in a]
print(square_a)
























































    
