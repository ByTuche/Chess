
from tkinter import *

root = Tk()


bgimg= PhotoImage(file = "./assets/chessboard.png")
bg = Label(root, i = bgimg)

bg.pack()
root.mainloop()