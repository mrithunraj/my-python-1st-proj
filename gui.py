from tkinter import *

root=Tk()
root.title("gui")
root.geometry("1000x500")


Label(root,text="welcome gui",bg='blue',fg='white',font=('Algerian',10),height=5,width=60).pack()
Label(root,text="welcome gui",bg='blue',fg='white',font=('Algerian',10),height=5,width=60).pack(side=LEFT)
Label(root,text="welcome gui",bg='blue',fg='white',font=('Algerian',10),height=5,width=60).pack(side=RIGHT)
Label(root,text="welcome gui",bg='blue',fg='white',font=('Algerian',10),height=5,width=60).pack(side=BOTTOM)

root.mainloop()
