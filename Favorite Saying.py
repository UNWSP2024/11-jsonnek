# Jonathan Sonnek
# November 13 2025
# Favorite Saying

import tkinter
class Favorite_SayingGUI():
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()
        # Create frame
        self.frame = tkinter.Frame(self.main_window)
        # Create labels
        self.label1 = tkinter.Label(self.frame, text = '"Therefore do not worry about tomorrow,')
        self.label2 = tkinter.Label(self.frame, text = "for tomorrow will worry about itself.")
        self.label3 = tkinter.Label(self.frame, text = 'Each day has enough trouble of its own"')
        self.label4 = tkinter.Label(self.frame, text = "Matthew 6:34")
        # Pack Labels
        self.label1.pack(side = 'top')
        self.label2.pack(side = 'top')
        self.label3.pack(side = 'top')
        self.label4.pack(side = 'top')
        # Pack Frame
        self.frame.pack()
        # Enter the tkinter mainloop
        tkinter.mainloop()
if __name__ == "__main__":
    saying = Favorite_SayingGUI()