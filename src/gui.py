'''
The GUI class is exclusivly made to create
and configure the graphical elements of the 
game (tkinter widgets).
'''


from tkinter import *


class Gui:

    def __init__(self):
        self.root = Tk()
        self.root.title("Collisions Game by Lauritz Kremzow")

        # Loading Images
        self.bg_img = PhotoImage(file="assets\\bg.gif")
        self.player_img = PhotoImage(file="assets\\player.gif")
        self.obstacle_img = PhotoImage(file="assets\\obstacle.gif")
        
        # Creating Background on Canvas
        self.main_canvas = Canvas(width="1080", height="500")
        self.main_canvas.create_image(0, 0, anchor=NW, image=self.bg_img)
        self.main_canvas.pack()
