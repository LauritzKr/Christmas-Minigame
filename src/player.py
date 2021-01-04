'''
The player class controls the movement
of the player acros the 2D screen and
also checks for collisions and when the
game is over.
'''


from threading import Thread
from time import sleep


class Player(Thread):

    def __init__(self, gui, image):
        Thread.__init__(self)

        # Creating Santa Image and its Variables
        self.canvas = gui.main_canvas
        self.player_id = self.canvas.create_image(500, 460, image=image)
        self.x_vel = 0
        self.y_vel = 0
        self.obstacles = []

        # Binding Keys
        self.root = gui.root
        self.root.bind("<Left>", lambda event: self.set_x_vel(event, -4))
        self.root.bind("<Right>", lambda event: self.set_x_vel(event, 4))

        # Mainthread
        self.start()

    def set_x_vel(self, event, x_vel):
        self.x_vel = x_vel

    def set_y_vel(self, event, y_vel):
        self.x_vel = y_vel

    def run(self):
        while True:
            sleep(0.01)
            self.check_edge_collision()
            self.check_obs_collision()
            self.canvas.move(self.player_id, self.x_vel, self.y_vel)

    def check_edge_collision(self):
        # Transition from Left to Right Screen Edge
        if self.canvas.coords(self.player_id)[0] < -20:
            self.canvas.coords(self.player_id, 1100, 460)

        # Transition from Right to Left Screen Edge
        if self.canvas.coords(self.player_id)[0] > 1100:
            self.canvas.coords(self.player_id, -20, 460)

    def check_obs_collision(self):
        # Player's Hitbox (4-Tupel with x1, y1, x2, y2)
        player_hb = self.canvas.bbox(self.player_id)

        # Collision Detection
        for obstacle in self.obstacles:
            obs_hb = self.canvas.bbox(obstacle.obstacle_id)

            if (player_hb[0] < obs_hb[2] < player_hb[2] and 
                player_hb[1] < obs_hb[1] < player_hb[3] or 
                player_hb[0] < obs_hb[0] < player_hb[2] and 
                player_hb[1] < obs_hb[3] < player_hb[3]):
                self.game_over()

    def game_over(self):
        self.canvas.create_text(250, 100, text="GAME OVER!", font=("Times", 50))
        sleep(3)
        self.root.destroy()
