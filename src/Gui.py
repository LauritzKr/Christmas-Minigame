from tkinter import *


class Gui:

    def __init__(self):
        self.root = Tk()

        # Loading Images
        self.bg_img = PhotoImage(file="images\\bg.gif")
        self.santa_img = PhotoImage(file="images\\santa.gif")
        self.snowflake_img = PhotoImage(file="images\\snowflake.gif")
        
        # Creating Background on Canvas
        self.canvas = Canvas(width="1080", height="500")
        self.canvas.create_image(0, 0, anchor=NW, image=self.bg_img)
        self.canvas.pack()
