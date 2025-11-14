# Jonathan Sonnek
# November 13 2025
# Personal information
import tkinter

class PersonalInformationGUI:
    def __init__(self):
        # Create main window
        self.main_window = tkinter.Tk()
        # Create separate frames
        self.frame_top = tkinter.Frame(self.main_window)
        self.frame_bottom = tkinter.Frame(self.main_window)
        # Create empty label
        self.value = tkinter.StringVar()
        self.address = tkinter.Label(self.frame_top, textvariable=self.value)
        # Create buttons
        self.showinfo = tkinter.Button(self.frame_bottom, text = "Show Information", command = self.showinfo)
        self.quit = tkinter.Button(self.frame_bottom, text = "Quit", command = self.main_window.destroy)
        # Pack the label
        self.address.pack()
        # Pack the Buttons
        self.showinfo.pack(side = "left")
        self.quit.pack(side = "left")
        # Pack the frames
        self.frame_top.pack()
        self.frame_bottom.pack()
        # Enter the tkinter main loop.
        tkinter.mainloop()
    # Define the showinfo function
    def showinfo(self):
        self.value.set("Jonathan Sonnek\n 2170 County Road 127\n Delano, MN 55328")

if __name__ == "__main__":
    personal_information = PersonalInformationGUI()