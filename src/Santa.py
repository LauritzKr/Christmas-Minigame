from threading import Thread
from time import sleep


class Santa(Thread):

    def __init__(self, gui, image):
        Thread.__init__(self)

        # Creating Santa Image and its Variables
        self.canvas = gui.main_canvas
        self.santa_id = self.canvas.create_image(500, 460, image=image)
        self.vel = 0
        self.snow = []

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
            sleep(0.01)
            self.check_snow_collision()
            self.check_edge_collision()
            self.canvas.move(self.santa_id, self.vel, 0)

    def check_snow_collision(self):
        # Santa's Hitbox (4-Tupel with x1, y1, x2, y2)
        santa_hb = self.canvas.bbox(self.santa_id)

        # Collision Detection
        for snowflake in self.snow:
            snow_hb = self.canvas.bbox(snowflake.snow_id)

            if (santa_hb[0] < snow_hb[2] < santa_hb[2] and 
                santa_hb[1] < snow_hb[1] < santa_hb[3] or 
                santa_hb[0] < snow_hb[0] < santa_hb[2] and 
                santa_hb[1] < snow_hb[3] < santa_hb[3]):
                sleep(2)

        '''
        add respawn
        add score maybe highscore
        '''

    def check_edge_collision(self):
        # Transition from Left to Right Screen Edge
        if self.canvas.coords(self.santa_id)[0] < -20:
            self.canvas.coords(self.santa_id, 1100, 460)

        # Transition from Right to Left Screen Edge
        if self.canvas.coords(self.santa_id)[0] > 1100:
            self.canvas.coords(self.santa_id, -20, 460)
