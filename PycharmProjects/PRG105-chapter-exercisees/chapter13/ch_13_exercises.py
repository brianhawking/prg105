"""
    Starting Out with Python by Tony Gaddis, fifth edition
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free (green checkmark upper right)
    Submit your completed file
"""
import tkinter
import tkinter.messagebox

# TODO 13.2 Using the tkinter Module
print("=" * 10, "Section 13.2 using tkinter", "=" * 10)


# Write the code from program 13-2 to display an empty window, no need
# to re-import tkinter. Use the class name MyGUI2


class MyGUI2:
    def __init__(self):
        # create the main window widget
        self.main_window = tkinter.Tk()

        # Create label with hello world text
        self.label = tkinter.Label(self.main_window, text='Hello World')

        # Call label's pack method (whatever this does)
        self.label.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()


# Create an instance of the MyGUI2 class
# if __name__ == '__main__':
#     my_gui = MyGUI2()

# TODO 13.3 Adding a label widget
print("=" * 10, "Section 13.3 adding a label widget", "=" * 10)
# Add a label to MyGUI2 (above) that prints your first and last name; pack the label
# Create an instance of MyGUI2

# if __name__ == '__main__':
#     my_gui2 = MyGUI2()

# TODO 13.4 Organizing Widgets with Frames
print("=" * 10, "Section 13.4 using frames", "=" * 10)


# Create a MyGUI3 class that creates a window with two frames
# In the top Frame add labels with your name and major
# In the bottom frame add labels with the classes you are taking this semester
# Create an instance of MyGUI3


class MyGUI3:
    def __init__(self):
        # Create main window widget
        self.main_window = tkinter.Tk()

        # Create two frames, oen for top of window and other for bottom
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Add labels to top frame
        self.nameLabel = tkinter.Label(self.top_frame, text='Brian Veitch')
        self.majorLabel = tkinter.Label(self.top_frame, text='AAS in Mobile Design and Development')

        # Add labels to bottom frame
        self.class1Label = tkinter.Label(self.bottom_frame, text='DBM 100')
        self.class2Label = tkinter.Label(self.bottom_frame, text='PRG 105')
        self.class3Label = tkinter.Label(self.bottom_frame, text='MAD 155')

        # Pack the labels
        self.nameLabel.pack(side='top')
        self.majorLabel.pack(side='top')

        self.class1Label.pack(side='left')
        self.class2Label.pack(side='left')
        self.class3Label.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        # Enter main loop
        tkinter.mainloop()


#
# if __name__ == '__main__':
#     my_gui3 = MyGUI3()


# TODO 13.5 Button Widgets and info Dialog Boxes
print("=" * 10, "Section 13.5 button widgets and info dialogs", "=" * 10)


# Create a GUI that will tell a joke
# Use a button to show the punch line, which should appear in a dialog box
# Create an instance of the GUI

class MyGUI4:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.button = tkinter.Button(self.main_window, text="What does a baby computer call his father? ",
                                     command=self.do_something)

        self.button.pack()

        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo('Response', 'Data!')


# if __name__ == '__main__':
#     my_gui4 = MyGUI4()

# TODO 13.6 getting input / 13.7 Using Labels as output fields
print("=" * 10, "Section 13.6-13.7 input and output using Entry and Label", "=" * 10)


# Using the program in 13.10 kilo converter as a sample,
# create a program to convert inches to centimeters


class MyInchesConverter:

    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # widget for top frame
        self.prompt_label = tkinter.Label(self.top_frame, text="Enter a value in inches: ")
        self.inches_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt_label.pack(side="left")
        self.inches_entry.pack(side="left")

        # widget for bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame, text="Convert!", command=self.convert)

        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit!", command=self.main_window.destroy)

        # pack stuff
        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")

        # pack frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    # convert function
    def convert(self):
        # get value from user
        inches = float(self.inches_entry.get())

        # convert to centimeters
        centimeters = inches * 2.54

        tkinter.messagebox.showinfo("Results",
                                    str(inches) + ' inches is equal to ' + str(centimeters) + ' centimeters.')


if __name__ == '__main__':
    my_gui5 = MyInchesConverter()
