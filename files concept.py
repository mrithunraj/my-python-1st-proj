cnt=int(input("enter a student detail count"))

tot=0

for i in range(1,cnt+1):
    print("enter",i,"student")

    a=input("enter school name")
    b=input("enter a student name")
    c=int(input("enter a student marks"))
    d=input("enter a subject name")
    e=input("enter a student address")
    f=open(b+'.txt','w')
    f.write("\n school name:"+a)
    f.write("\n student name:"+b)
    f.write("\n student marks "+b+":"+str(c))
    f.write("\n subject name")
    f.write("\n student address")

    f.close()

  
