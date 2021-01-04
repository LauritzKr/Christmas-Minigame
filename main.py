'''
The main class is designed to JUST create 
the different objects needed for the game 
and therefore hide as much of the source 
code (src folder) as possible when executing 
the program. 
'''


from src import gui, santa, snowflake


class Main:
    
    def __init__(self):
        # Gui Instance
        self.gui = gui.Gui()

        # Santa Instance
        self.santa = santa.Santa(self.gui, self.gui.santa_img)

        # Snowflake Instances inside Snow List
        for _ in range(10):
            self.santa.snow.append(
                snowflake.Snowflake(self.gui, self.gui.snowflake_img)
            )

        # Mainloop
        self.gui.root.mainloop()


if __name__ == "__main__":
    Main()
