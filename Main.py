from src import Gui, Snowflake, Santa


class Main:
    
    def __init__(self):
        # Gui Instance
        self.gui = Gui.Gui()

        # Snowflake / Santa Instances
        for _ in range(10):
            Snowflake.Snowflake(self.gui, self.gui.snowflake_img) 
        
        Santa.Santa(self.gui, self.gui.santa_img)

        # Mainloop
        self.gui.root.mainloop()


if __name__ == "__main__":
    Main()
