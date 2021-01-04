'''
The obstacle class controls the movement
of the different obstacles across the screen.
'''


from threading import Thread
from random import randint
from time import sleep


class Obstacle(Thread):

    def __init__(self, gui, image):
        Thread.__init__(self)

        # Creating Obstacle Image
        self.canvas = gui.main_canvas
        self.obstacle_id = self.canvas.create_image(0, 0, image=image)

        # Placing It Randomly
        self.reset_pos()

        # Mainthread
        self.start()

    def reset_pos(self):
        self.canvas.coords(self.obstacle_id, randint(0, 1080), -randint(50, 150))
        self.x_vel = randint(-1, 1)
        self.y_vel = randint(2, 3)

    def run(self):
        while True:
            sleep(0.01)
            self.check_edge_collision()
            self.canvas.move(self.obstacle_id, self.x_vel, self.y_vel)

    def check_edge_collision(self):
        # Transition from Bottom to Top Screen Edge
        if self.canvas.coords(self.obstacle_id)[1] > 600:
            self.reset_pos()
