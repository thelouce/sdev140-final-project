"""
Cat Game by Aubree Craft
A little game about cats. Currently only runs character creation.
Name your cat, pick its age, and pick its coat color. The cat picture updates for every cat you pick.
This is the title screen. To keep the code as neat as possible, I split the character creation and the title screen.
"""
import tkinter as tk
from tkinter import *
import tkinter.font as font
from gameWindow import gameRun


class TitleScreen:
    """creates the title screen"""

    def __init__(self, master):
        self.master = master
        master.title("Cat Game")
        master.geometry('500x400+100+75')
        master.configure(bg="#363636")

        self.titleImg = PhotoImage(file='final_project/intro-graphic.gif')
        self.canvas = Canvas(self.master, height=300, width=500,
                             highlightthickness=0, bg="#363636")
        self.canvas.grid(row=0, column=0)
        self.canvas.create_image(
            250, 300/2, anchor=CENTER, image=self.titleImg)

        startFont = font.Font(size=20, weight='bold')
        self.StartButton = tk.Button(
            text="Start", bg="black", fg="white", width=10, anchor=CENTER, command=gameRun)
        self.StartButton['font'] = startFont
        self.StartButton.grid(row=1, column=0)


root = Tk()
title = TitleScreen(root)
root.mainloop()
