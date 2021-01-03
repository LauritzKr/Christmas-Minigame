from threading import Thread
from time import sleep


class Santa(Thread):

    def __init__(self, gui, image):
        Thread.__init__(self)

        # Creating Santa Image / Variables
        self.background = gui.canvas
        self.image_id = self.background.create_image(500, 460, image=image)
        self.velocity = 0

        # Binding Keys
        self.root = gui.root
        self.root.bind("<Left>", self.__set_neg_vel)
        self.root.bind("<Right>", self.__set_pos_vel)

        # Mainthread
        self.start()

    def __set_neg_vel(self, event):
        self.velocity = -4

    def __set_pos_vel(self, event):
        self.velocity = 4

    def run(self):
        while True:
            # Moving Santa
            sleep(0.01)
            self.background.move(self.image_id, self.velocity, 0)

            # Transition from Left to Right Screen Edge
            if self.background.coords(self.image_id)[0] < -20:
                self.background.coords(self.image_id, 1100, 460)

            # Transition from Right to Left Screen Edge
            if self.background.coords(self.image_id)[0] > 1100:
                self.background.coords(self.image_id, -20, 460)
