from tkinter import *

root=Tk()
root.title("gui")
root.geometry("1000x500")

name=StringVar()
mob=IntVar()
mail=StringVar()

import pymysql
def add():
    Name=name.get()
    Mob=mob.get()
    Mail=mail.get()

    print(Name,Mob,Mail)
    db=pymysql.connect(host="localhost",user="root",password="",database="mrithun")

    cur=db.cursor()

    ins="INSERT INTO raj(name,mob,mail)VALUES(%s,%s,%s)"
    val=(Name,Mob,Mail)
    cur.execute(ins,val)
    db.commit()

Label(root,text="enter your name:").grid(row=0,column=0)
Label(root,text="enter your mob:").grid(row=1,column=0)
Label(root,text="enter your mail:").grid(row=2,column=0)

Entry(root,textvar=name).grid(row=0,column=1)
Entry(root,textvar=mob).grid(row=1,column=1)
Entry(root,textvar=mail).grid(row=2,column=1)

Button(root,text='submit',command=add).grid(row=3,column=0)

root.mainloop()
