from tkinter import *

root=Tk()
root.title("Gui")
root.geometry("1000x700")

Label(root,text="hello Gui",bg='black',fg='white',font=('Algerian',10),height=5).pack(fill=X)
Label(root,text="hello Gui",bg='yellow',fg='white',font=('Algerian',10),width=30).pack(side='left',fill=Y)
Label(root,text="hello Gui",bg='pink',fg='white',font=('Algerian',10),width=30).pack(side='right',fill=Y)
Label(root,text="hello Gui",bg='blue',fg='white',font=('Algerian',10),height=100).pack(side='left',fill=X)

root.mainloop()
