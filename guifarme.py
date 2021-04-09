from tkinter import *

root=Tk()
root.title("gui")
root.geometry("1000x500")

tframe=Frame(root)
tframe.pack()
bframe=Frame(root)
bframe.pack(side=BOTTOM)


Button(bframe,text='click',bg='blue').pack(side='right')
Button(tframe,text='click',bg='pink').pack(side='right')
Button(bframe,text='click',bg='black').pack()
Button(tframe,text='click',bg='brown').pack()


root.mainloop()

