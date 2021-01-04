from src import gui, santa, snowflake


class Main:
    
    def __init__(self):
        # Gui Instance
        self.gui = gui.Gui()

        # Santa / Snowflake Instances
        self.santa = santa.Santa(self.gui, self.gui.santa_img)
        for _ in range(10):
            self.snowflake = snowflake.Snowflake(self.gui, self.gui.snowflake_img)
            self.santa.snow.append(self.snowflake)

        # Mainloop
        self.gui.root.mainloop()


if __name__ == "__main__":
    Main()
