import pymysql

db=pymysql.connect(host='localhost',user='root',password='',database='com1')

if db:
    print("connect")

cur=db.cursor()

#d="CREATE DATABASE com1"

#cur.execute(d)

tab="CREATE TABLE mrithun(name VARCHAR(200),age INT,mark INT,address TEXT)"

cur.execute(tab)
