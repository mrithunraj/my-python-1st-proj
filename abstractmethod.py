import pymysql

database=pymysql.connect(host='localhost',user='root',password='',database='king')

if database:
    print("connected")

cur=database.cursor()

'''d="CREATE DATABASE king"

cur.execute(d)'''

tab="CREATE TABLE phone(name VARCHAR(100),price INT,quantity TEXT)"

cur.execute(tab)


m=int(input("enter no of products"))

for i in range(1,m+1):
    a=input("enter a product name")
    b=input("enter a product price")
    c=input("enter a product quantity")

ins="INSERT INTO phone(name,price,quantity) VALUES(%s,%s,%s)"

val=(a,b,c)
cur.execute(ins,val)
database.commit()
