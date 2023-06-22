crsp = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}

class Pion:
    def __init__(self, xpos, ypos, col, type, img):
        self.xpos = crsp[xpos] - 1
        self.ypos = ypos - 1
        self.col = col
        self.type = type
        self.img = img

    def move(self, xpos, ypos):
        if self.type == "pion":
            if self.col == "black":
                if self.ypos == 7:
                    if ypos == 6 or 5 and self.xpos == xpos:

                        self.xpos = xpos
                        self.ypos = ypos