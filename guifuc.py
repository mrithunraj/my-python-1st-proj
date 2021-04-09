from tkinter import *

root=Tk()
root.title("gui")
root.geometry("1000x500")


def calls():
    print("welcome mrithun")

Label(root,text="welcome gui",bg='blue',fg='white',font=('Algerian',10),height=5,width=60).pack()


Button(root,text='click',command=calls,bg='blue').pack(side=RIGHT)
Button(root,text='click',command=calls,bg='orange').pack(side=LEFT)
Button(root,text='click',command=calls,bg='green').pack(side=BOTTOM)
Button(root,text='click',command=calls,bg='pink').place(x=100,y=50)

root.mainloop()
