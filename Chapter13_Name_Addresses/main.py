"""
Write a GUI program that displays your name and address when a button is
clicked (you can use the address of the school). The program’s window
should resemble the sketch on the far left side of figure 13-26 when it runs.
When the user clicks the Show Info button, the program should display your name
and address as shown in the sketch on the right of the figure.
"""

import tkinter
import tkinter.messagebox


class MyGUI:

    def __init__(self):
        self.main_window = tkinter.Tk()

        # Create variables
        self.name_value = tkinter.StringVar()
        self.street_value = tkinter.StringVar()
        self.csz_value = tkinter.StringVar()

        # create top and bottom frame
        self.info_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Create label widgets
        self.name_label = tkinter.Label(self.info_frame, textvariable=self.name_value)
        self.street_label = tkinter.Label(self.info_frame, textvariable=self.street_value)
        self.csz_label = tkinter.Label(self.info_frame, textvariable=self.csz_value)

        # Pack the labels
        self.name_label.pack()
        self.street_label.pack()
        self.csz_label.pack()

        # Create the button widgets
        self.show_info_button = tkinter.Button(self.button_frame, text="Show Info", command=self.show)
        self.quit_button = tkinter.Button(self.button_frame, text="Quit", command=self.main_window.destroy)

        # Pack buttons
        self.show_info_button.pack(side="left")
        self.quit_button.pack(side="right")

        # Pack the frames
        self.info_frame.pack()
        self.button_frame.pack()

        # Enter loop
        tkinter.mainloop()

    def show(self):
        self.name_value.set("McHenry Community College")
        self.street_value.set("8900 US Hwy 14")
        self.csz_value.set("Crystal Lake, Illinois, 60014")


# Create instance of MyGUI class
my_gui = MyGUI()
