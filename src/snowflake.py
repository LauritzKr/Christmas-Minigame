from threading import Thread
from random import randint
from time import sleep
import Santa


class Snowflake(Thread):

    def __init__(self, gui, image):
        Thread.__init__(self)
        Santa.Santa.snow.append(self)

        # Creating Snowflake Image
        self.canvas = gui.main_canvas
        self.snow_id = self.canvas.create_image(0, 0, image=image)

        # Placing It Randomly
        self.__set_rand_pos()

        # Mainthread
        self.start()

    def __set_rand_pos(self):
        self.canvas.coords(self.snow_id, randint(0, 1080), -randint(50, 100))
        self.x_vel = randint(-2, 2)
        self.y_vel = randint(2, 4)

    def run(self):
        while True:
            # Moving Snowflake
            sleep(0.01)
            self.canvas.move(self.snow_id, self.x_vel, self.y_vel)

            # Transition from Bottom to Top Screen Edge
            if self.canvas.coords(self.snow_id)[1] > 600:
                self.__set_rand_pos()
