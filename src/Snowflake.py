from threading import Thread
from random import randint
from time import sleep


class Snowflake(Thread):

    def __init__(self, gui, image):
        Thread.__init__(self)

        # Creating Snowflake Image
        self.background = gui.canvas
        self.image_id = self.background.create_image(0, 0, image=image)

        # Placing It Randomly
        self.__set_rand_pos()

        # Mainthread
        self.start()

    def __set_rand_pos(self):
        self.background.coords(self.image_id, randint(0, 1080), -randint(50, 100))
        self.x_vel = randint(-2, 2)
        self.y_vel = randint(2, 4)

    def run(self):
        while True:
            # Moving Snowflake
            sleep(0.01)
            self.background.move(self.image_id, self.x_vel, self.y_vel)

            # Transition from Bottom to Top Screen Edge
            if self.background.coords(self.image_id)[1] > 600:
                self.__set_rand_pos()
