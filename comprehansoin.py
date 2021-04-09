
import pymysql
db=pymysql.connect(host='localhost',user='root',password='',database='com1')
cur=db.cursor()
r=int(input("enter no of student"))
for i in range(1,r+1): 
     a=input("enter "+str(i)+" student name")
     b=input("enter a student age")
     c=input("enter a student mark")
     d=input("enter a student address")
 
     ins="INSERT INTO mrithun(name,age,mark,address)VALUES(%s,%s,%s,%s)"
     val=(a,b,c,d)
     cur.execute(ins,val)
     db.commit()
#print("enter",i,"value")



'''ins="INSTER INTO detail(name,age,mark,address)VALUES(%s,%s,%s,%s)"
cur.execute(ins,val)
db.commit()'''




