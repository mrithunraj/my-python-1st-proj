import pymysql

db=pymysql.connect(host='localhost',user='root',password="",database='mrithun')

if db:
    print("connect")

cur=db.cursor()

tab="CREATE TABLE raj(name VARCHAR(100),mob INT,mail TEXT)"
cur.execute(tab)
