'''
The main class is designed to JUST create 
the different objects needed for the game 
and therefore hide as much of the source 
code (src folder) as possible when executing 
the program. 
'''


from src import gui, player, obstacle


class Main:
    
    def __init__(self):
        # Gui Instance
        self.gui = gui.Gui()

        # Santa Instance
        self.player = player.Player(self.gui, self.gui.santa_img)

        # obstacleInstances inside playersers List
        for _ in range(10):
            self.player.obstacles.append(
                obstacle.Obstacle(self.gui, self.gui.obstacle_img)
            )

        # Mainloop
        self.gui.root.mainloop()


if __name__ == "__main__":
    Main()
