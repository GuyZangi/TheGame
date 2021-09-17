from tkinter import *
from tkinter.ttk import *

root = Tk()



root.geometry('500x500')
root.title("The Game - Main Menu")
# new window (the game)
def openNewWindow():
    Game = Toplevel(root)
    Game.title("The Game.")
    Game.geometry("500x500")

     

    

topFrame = Frame(root)
topFrame.pack()

botFrame = Frame(root)
botFrame.pack(side=BOTTOM)
# main menu

theText = Label(root, text="The Game.")
theText.config(font=('Calibri',50))
theText.pack()

bt1 = Button(None, text = "Start!", command=openNewWindow)
bt1.pack()

bt = Button(botFrame, text = "Exit", command=root.destroy)
bt.pack()



root.mainloop()