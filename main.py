from pions import Pion
from tkinter import *



plateau = [[0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0]]

pion1b = Pion("a",7,"black","pion","./assets/b_pawn.png")
pion2b = Pion("b",7,"black","pion","./assets/b_pawn.png")
pion3b = Pion("c",7,"black","pion","./assets/b_pawn.png")
pion4b = Pion("d",7,"black","pion","./assets/b_pawn.png")
pion5b = Pion("e",7,"black","pion","./assets/b_pawn.png")
pion6b = Pion("f",7,"black","pion","./assets/b_pawn.png")
pion7b = Pion("g",7,"black","pion","./assets/b_pawn.png")
pion8b = Pion("h",7,"black","pion","./assets/b_pawn.png")
t1b = Pion("a",8,"black","tour","./assets/b_rook.png")
t2b = Pion("h",8,"black","tour","./assets/b_rook.png")
c1b = Pion("b",8,"black","cavalier","./assets/b_knight.png")
c2b = Pion("g",8,"black","cavalier","./assets/b_knight.png")
f1b = Pion("c",8,"black","fou","./assets/b_fou.png")
f2b = Pion("f",8,"black","fou","./assets/b_fou.png")
reineb = Pion("d",8,"black","reine","./assets/b_queen.png")
roib = Pion("e",8,"black","roi","./assets/b_king.png")

pion1w = Pion("a",2,"white","pion","./assets/w_pawn.png")
pion2w = Pion("b",2,"white","pion","./assets/w_pawn.png")
pion3w = Pion("c",2,"white","pion","./assets/w_pawn.png")
pion4w = Pion("d",2,"white","pion","./assets/w_pawn.png")
pion5w = Pion("e",2,"white","pion","./assets/w_pawn.png")
pion6w = Pion("f",2,"white","pion","./assets/w_pawn.png")
pion7w = Pion("g",2,"white","pion","./assets/w_pawn.png")
pion8w = Pion("h",2,"white","pion","./assets/w_pawn.png")
t1w = Pion("a",1,"white","tour","./assets/w_rook.png")
t2w = Pion("h",1,"white","tour","./assets/w_rook.png")
c1w = Pion("b",1,"white","cavalier","./assets/w_knight.png")
c2w = Pion("g",1,"white","cavalier","./assets/w_knight.png")
f1w = Pion("c",1,"white","fou","./assets/w_fou.png")
f2w = Pion("f",1,"white","fou","./assets/w_fou.png")
reinew = Pion("d",1,"white","reine","./assets/w_queen.png")
roiw = Pion("e",1,"white","roi","./assets/w_king_.png")

l_pion = ( pion1b, pion2b, pion3b, pion4b, pion5b, pion6b, pion7b, pion8b, pion1w, pion2w, pion3w, pion4w, pion5w, pion6w, pion7w, pion8w, t1b, t2b, c1b, c2b, f1b, f2b, reineb, roib, t1w, t2w, c1w, c2w, f1w, f2w, reinew, roiw)

set()

root = Tk()

root.grid()
def places(pion):
    
    Label(root, i = PhotoImage(file = pion.img)).grid(column= pion.xpos, row= pion.ypos)

def set():
    for i in l_pion:
        places(i)
root.geometry("480x480")

bgimg= PhotoImage(file = "./assets/chessboard.png")

label1 = Label( root, image = bgimg)
label1.place(x = 0, y = 0)
aea = PhotoImage(file=roiw.img)
Label(root, image= aea).grid(column= 1, row= 1)
root.mainloop()

if piece == "p":
        if selected_piece[0] == 1:
            if dest_row > 3:
                return False
        if selected_piece[0] != 1:
            if dest_row - 1 != selected_piece[0]:
                return False
        if dest_col != selected_piece[1]:
            if board[dest_row][dest_col] == ' ' or board[dest_row][dest_col].isupper() == False:
                return False
            if dest_col > selected_piece[1] + 1 or dest_col < selected_piece[1] - 1:
                return False
        if selected_piece[0] > dest_row:
            return False
        if board[dest_row][dest_col] != ' ' and dest_col == selected_piece[1]:
                return False
        if selected_piece[0] == dest_row :
            return False
    if piece == "P":
        if selected_piece[0] == 6:
            if dest_row < 4:
                return False
        if selected_piece[0] != 6:
            if dest_row + 1 != selected_piece[0]:
                return False
        if dest_col != selected_piece[1]:
            if board[dest_row][dest_col] == ' ' or board[dest_row][dest_col].isupper() == True:
                return False
            if dest_col > selected_piece[1] + 1 or dest_col < selected_piece[1] - 1:
                return False
        if selected_piece[0] < dest_row:
            return False
        if board[dest_row][dest_col] != ' ' and dest_col == selected_piece[1]:
                return False
    # If all validation rules pass, return True
    return Trueb