from tkinter import *

root=Tk()
root.title("gui")
root.geometry("1000x500")

name=StringVar()
mob=IntVar()
mail=StringVar()
address=StringVar()
gender=StringVar()

import pymysql
def sub():
    Name=name.get()
    Mob=mob.get()
    Mail=mail.get()
    Address=address.get()
    Gender=gender.get()
    COURSE=Course.get()

    print(Name,Mob,Mail,Address,Gender,COURSE)
    db=pymysql.connect(host="localhost",user="root",password="",database="apple")



    cur=db.cursor()

    ins="INSERT INTO mrithun(name,mob,mail,address,gender,course)VALUES(%s,%s,%s,%s,%s,%s)"
    VAL=(Name,Mob,Mail,Address,Gender,COURSE)
    cur.execute(ins,VAL)
    db.commit()




Label(root,text="enter your name:").grid(row=0,column=0)
Label(root,text="enter your mob:").grid(row=1,column=0)
Label(root,text="enter your mail:").grid(row=2,column=0)
Label(root,text="enter your address:").grid(row=3,column=0)


Entry(root,textvar=name).grid(row=0,column=1)
Entry(root,textvar=mob).grid(row=1,column=1)
Entry(root,textvar=mail).grid(row=2,column=1)
Entry(root,textvar=address).grid(row=3,column=1)


Label(root,text="enter your gender:").grid(row=4,column=0)

Radiobutton(root,text="Male",variable=gender,value="male").grid(row=4,column=1)
Radiobutton(root,text="Female",variable=gender,value="Female").grid(row=4,column=2)

Label(root,text="enter your hobbies:").grid(row=5,column=0)

Checkbutton(root,text="cricket").grid(row=5,column=1)
Checkbutton(root,text="football").grid(row=5,column=2)

Label(root,text="choose course:").grid(row=6,column=0)

Course=StringVar()

op=['c','c++','java','python','datascience']
ops=OptionMenu(root,Course,*op)
ops.config(width=40)
Course.set("choose course")
ops.grid(row=6,column=1)


Button(root,text='submit',command=sub).grid(row=7,column=0)

root.mainloop()
print(name)
      
      


































