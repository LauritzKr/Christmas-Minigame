from src import Gui, Santa, Snowflake


class Main:
    
    def __init__(self):
        # Gui Instance
        self.gui = Gui.Gui()

        # Santa / Snowflake Instances
        Santa.Santa(self.gui, self.gui.santa_img)
        for _ in range(10):
            Snowflake.Snowflake(self.gui, self.gui.snowflake_img) 
        
        # Mainloop
        self.gui.root.mainloop()


if __name__ == "__main__":
    Main()
