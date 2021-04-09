import pymysql

db=pymysql.connect(host='localhost',user='root',password="",database='apple')

if db:
    print("connected")

cur=db.cursor()

tab="CREATE TABLE mrithun(name VARCHAR(200),mob INT,mail TEXT,address TEXT,gender TEXT,course TEXT)"
cur.execute(tab)
