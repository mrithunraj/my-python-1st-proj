'''a=[]
def low(s):
    return s.lower()
for i in range(1,6):
    inp=low(input("enter your name"))
    a.append(inp)
print(a)


b=[2,3,4,5,6,7]

for i in range(len(b)):
    b[i]=b[i]**2

print(b)



a=[1,2,3,4,5,6,7]

square=[b **2 for b in a]
print(square)
    
    
    
list1=["m","na","i","ke"]
list2=["y","me","n","lly"]
list3=[]

for i in range(len(list1)):
                    list3.append(list1[i]+list2[i])


print(list3)


tab=int(input("enter a table name"))

for i in range(1,21):
    print(i,"*",tab,"=",i*tab)'''

import _thread

class mango:
    def tax(self,name,a,b):
        print("starts:",name)
        for i in range(a,b+1):
              print(i)

a=mango()
b=mango()

_thread.start_new_thread(a.tax,('thread1',100,201))
_thread.start_new_thread(b.tax,('thread2',500,601))




































































                
