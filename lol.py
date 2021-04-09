from tkinter import *

groot=Tk()
groot.title("gui")
groot.geometry("1000x600")

def cal():
    print("welcome")

Label(groot,text="welcome GUI",bg='blue',fg='orange',font=('Algerian',10),height=5,width=50).pack()
Button(groot,text='click',command=cal,bg='black').pack(side='left')

groot.mainloop()
