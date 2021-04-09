import pymysql

database=pymysql.connect(host='localhost',user='root',password='',database='word')

if database:
    print("connect")

cur=database.cursor()

'''d="CREATE DATABASE word"

cur.execute(d)'''

def insertt():
    name1=input("enter name")
    address1=input("enter adress")
    age1=input("enter age")
    mark1=input("enter mark")

    cur.execute("INSERT INTO ramsir(name,age,mark,address) VALUES(%s,%s,%s,%s)",(name1,age1,mark1,address1))
    database.commit()
    again=input("Do you want to continue")

    if again=='continue':
        insertt()


def uppdate():
    name=input("enter name")
    address=input("enter address")
        
        
    cur.execute("UPDATE ramsir SET address='"+address+"' WHERE name='"+name+"'")
    database.commit()

             
op=input("Do you want to insert/ update")

if op=='insert':
    insertt()

elif op=='update':
    uppdate()














    








    
    

