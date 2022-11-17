"""
Write an object-oriented GUI program that calculates a car’s gas mileage.
The program’s window should have Entry widgets that let the user enter
the number of gallons of gas the car holds, and the number of miles it
can be driven on a full tank. When a Calculate MPG button is clicked,
the program should display the number of miles that the car may be
driven per gallon of gas. Use the following formula to calculate miles per gallon:
"""

import tkinter
import tkinter.messagebox


class MilesPerGallon:

    def __init__(self):

        self.main_window = tkinter.Tk()

        # Create variable
        self.mpg_value = tkinter.StringVar()

        # Set up top and bottom frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # widgets for top frame
        self.prompt_gallons_label = tkinter.Label(self.top_frame, text="Enter how many gallons your car holds: ")
        self.gallons_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt_miles_label = tkinter.Label(self.top_frame, text="How many miles have you traveled: ")
        self.miles_entry = tkinter.Entry(self.top_frame, width=10)

        self.calc_label = tkinter.Label(self.top_frame, text="Converted to miles per gallon: ")
        self.mpg_label = tkinter.Label(self.top_frame, textvariable=self.mpg_value)

        # pack top frame stuff
        self.prompt_gallons_label.pack()
        self.gallons_entry.pack()
        self.prompt_miles_label.pack()
        self.miles_entry.pack()
        self.calc_label.pack(side="left")
        self.mpg_label.pack(side="left")

        # widgets for bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame, text="Convert", command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        # pack bottom frame stuff
        self.calc_button.pack(side="left")
        self.quit_button.pack(side="right")

        # pack frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        # get values from user
        gallons = float(self.gallons_entry.get())
        miles = float(self.miles_entry.get())

        # calculate mpg
        self.mpg_value.set(f"{miles/gallons:0.2f}")


my_gui = MilesPerGallon()
