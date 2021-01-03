from threading import Thread
from time import sleep


class Santa(Thread):

    def __init__(self, gui, image):
        Thread.__init__(self)

        # Creating Santa Image / Variables
        self.canvas= gui.main_canvas
        self.santa_id = self.canvas.create_image(500, 460, image=image)
        self.vel = 0

        # Binding Keys
        self.root = gui.root
        self.root.bind("<Left>", self.__set_neg_vel)
        self.root.bind("<Right>", self.__set_pos_vel)

        # Mainthread
        self.start()

    def __set_neg_vel(self, event):
        self.vel = -4

    def __set_pos_vel(self, event):
        self.vel = 4

    def run(self):
        while True:
            # Checking for Collision with Snowflake
            

            # Moving Santa
            sleep(0.01)
            self.canvas.move(self.santa_id, self.vel, 0)

            # Transition from Left to Right Screen Edge
            if self.canvas.coords(self.santa_id)[0] < -20:
                self.canvas.coords(self.santa_id, 1100, 460)

            # Transition from Right to Left Screen Edge
            if self.canvas.coords(self.santa_id)[0] > 1100:
                self.canvas.coords(self.santa_id, -20, 460)
