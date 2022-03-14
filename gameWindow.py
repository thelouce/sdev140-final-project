"""
Cat Game by Aubree Craft
This is the character creation itself.
"""
import tkinter as tk
from tkinter import *
import tkinter.font as font


class gameRun:
    def __init__(self):
        """calls the game window, initializes things, also has the various cats that will appear."""
        self.gameWindow = tk.Toplevel()
        self.gameWindow.geometry('500x400+100+75')
        self.gameWindow.configure(bg="#363636")
        self.catPicture = Canvas(
            self.gameWindow, height=150, width=500, highlightthickness=0, bg="#363636")
        self.cat1 = PhotoImage(file='final_project/white.png')
        self.cat2 = PhotoImage(file='final_project/black-cat.png')
        self.cat3 = PhotoImage(file='final_project/havana-brown.png')
        self.cat4 = PhotoImage(file='final_project/orange-tabby.png')
        self.cat5 = PhotoImage(file='final_project/russian-blue.png')
        self.cat6 = PhotoImage(file='final_project/seal-point.png')
        self.cat7 = PhotoImage(file='final_project/tuxedo.png')
        self.catPicture.create_image(
            250, 75, anchor=CENTER, image=self.cat1)
        self.catPicture.grid(row=0, column=0, columnspan=2)

        self.textFrame = Frame(
            self.gameWindow, width=500, height=300, bg="#363636")
        self.textFrame.grid(row=1, column=0, columnspan=2)

        textFont = font.Font(size=12, weight='bold')
        self.gameText = "Welcome, mortal. I see you have chosen to shed your mortal form for a more agreeable one. I am here to help you. Above, you can see the hints of your new life."
        self.gameLabel = Label(
            self.textFrame, text=self.gameText, bg="#363636", anchor=W, fg="white", wraplength=450, highlightthickness=0, bd=0)
        self.gameLabel['font'] = textFont
        self.gameLabel.grid(row=0, column=0, columnspan=2)

        def Line2():
            """Player Name Entry"""
            self.gameLabel['text'] = "But first, as your demonic advisor, I must know your name. Please, enter it."
            self.nameInput = Text(
                self.textFrame, bg="black", fg="white", height=1, width=30)
            self.nameInput.grid(row=1, column=0)
            self.nextButton['command'] = Line3

        def Line3():
            """Player Name Validation and reactions"""
            global playerName
            playerName = self.nameInput.get(1.0, "end-1c")
            self.nameInput.destroy()
            if len(playerName) == 0:
                self.gameLabel['text'] = "No, you should tell me your name."
                self.nextButton['command'] = Line2
            else:
                if playerName == "Kili":
                    nameResponse = "Is that a joke? " + \
                        playerName + "? Dare you take the name of that which gave you life? Fine. I'm flattered, honestly. You can keep it."
                else:
                    nameResponse = "%s. What an interesting name. Not one that inspires the spirit of destruction, but acceptable." % playerName
                self.gameLabel['text'] = nameResponse
                self.nextButton['command'] = Line4

        def Line4():
            """Player Age Entry"""
            self.gameLabel['text'] = "Very well. I'm curious, though. How old were you in your human form? In numbers, please."
            self.ageInput = Text(
                self.textFrame, bg="black", fg="white", height=1, width=30)
            self.ageInput.grid(row=1, column=0)
            self.nextButton['command'] = Line5

        def Line5():
            """Player Age choice, with some added validation that sends you back a page if you do not enter the proper data"""
            global playerAge
            playerAge = self.ageInput.get(1.0, "end-1c")
            self.ageInput.destroy()
            if len(playerAge) == 0:
                self.gameLabel['text'] = "Embarrassed? You could just lie about it, you know."
                self.nextButton['command'] = Line4
            try:
                if int(playerAge) < 0:
                    self.gameLabel['text'] = "How can you be younger than zero? That doesn't make any sense."
                elif int(playerAge) < 35 and int(playerAge) > 0:
                    self.gameLabel['text'] = "Ah. Young for a human. No wonder you feel so much ambition."
                elif int(playerAge) > 34 and int(playerAge) < 70:
                    self.gameLabel['text'] = "Ah. You have seen the world for what it is. You will soon have the power to change it."
                elif int(playerAge) > 69 and int(playerAge) < 100:
                    self.gameLabel['text'] = "The twilight of your years is upon you. But fear not, I can reverse that."
                else:
                    self.gameLabel['text'] = "I believe you're lying. No mere mortal is that old."
                self.nextButton['command'] = Line6
            except:
                self.gameLabel['text'] = "I said to use the arabic digits. Do you not comprehend?"
                self.nextButton['command'] = Line4

        def Line6():
            """Character Selection Screen: pick a kitten color"""
            self.gameLabel['text'] = "Now you may select your mortal form. Pick from the colors below."
            global catColors
            catColors = ['White', 'Black', 'Tuxedo', 'Blue',
                         'Orange Tabby', 'Brown', 'Seal Point']
            global variable
            variable = StringVar()
            variable.set(catColors[6])
            self.catSelect = OptionMenu(
                self.textFrame, variable, *catColors, command=changeColor)
            self.catSelect.grid(row=1, column=0)
            self.nextButton['command'] = Line7

        def changeColor(catChoice):
            """Updates and changes the cat pictures, which are uploaded earlier on in the file."""
            """Deleting the cats keeps them from clogging data."""
            catChoice = variable.get()
            if catChoice == "White":
                self.catPicture.delete("all")
                self.catPicture.create_image(
                    250, 75, anchor=CENTER, image=self.cat1)
            elif catChoice == "Black":
                self.catPicture.delete("all")
                self.catPicture.create_image(
                    250, 75, anchor=CENTER, image=self.cat2)
            elif catChoice == "Brown":
                self.catPicture.delete("all")
                self.catPicture.create_image(
                    250, 75, anchor=CENTER, image=self.cat3)
            elif catChoice == "Orange Tabby":
                self.catPicture.delete("all")
                self.catPicture.create_image(
                    250, 75, anchor=CENTER, image=self.cat4)
            elif catChoice == "Blue":
                self.catPicture.delete("all")
                self.catPicture.create_image(
                    250, 75, anchor=CENTER, image=self.cat5)
            elif catChoice == "Seal Point":
                self.catPicture.delete("all")
                self.catPicture.create_image(
                    250, 75, anchor=CENTER, image=self.cat6)
            elif catChoice == "Tuxedo":
                self.catPicture.delete("all")
                self.catPicture.create_image(
                    250, 75, anchor=CENTER, image=self.cat7)

        def Line7():
            """Confirms data, It's awesome and even keeps the cat picture properly!"""
            self.catSelect.destroy()
            self.nextButton.destroy()
            self.gameLabel['text'] = "You have chosen your demonic form and will walk the world accordingly."
            nameText = "%s is your name." % playerName
            self.nameLabel = Label(self.textFrame, text=nameText, bg="#363636",
                                   anchor=W, fg="white", wraplength=450, highlightthickness=0, bd=0)
            self.nameLabel['font'] = textFont
            self.nameLabel.grid(row=1, column=0, columnspan=2)
            ageText = "%s is your age." % playerAge
            self.ageLabel = Label(self.textFrame, text=ageText, bg="#363636", anchor=W,
                                  fg="white", wraplength=450, highlightthickness=0, bd=0)
            self.ageLabel['font'] = textFont
            self.ageLabel.grid(row=2, column=0, columnspan=2)
            catConfirm = "%s is your coat's color." % variable.get()
            self.catLabel = Label(self.textFrame, text=catConfirm, bg="#363636",
                                  anchor=W, fg="white", wraplength=450, highlightthickness=0, bd=0)
            self.catLabel['font'] = textFont
            self.catLabel.grid(row=3, column=0, columnspan=2)
            finalMessage = "With your character created, you'd be able to play the game. However, the game is still in progress. Thank you for creating a cat."
            self.final = Label(self.textFrame, text=finalMessage, bg="#363636",
                               anchor=W, fg="white", wraplength=450, highlightthickness=0, bd=0)
            self.final['font'] = textFont
            self.final.grid(row=4, column=0, columnspan=2)
            self.quitButton = Button(self.textFrame, text="Quit", fg="white", bg="black",
                                     width=20, anchor=CENTER, command=quit, highlightthickness=0, bd=0)
            self.quitButton.grid(row=5, column=0, columnspan=2)

        self.nextButton = Button(
            self.textFrame, text="Next", fg="white", bg="black", width=10, anchor=CENTER, command=Line2, highlightthickness=0, bd=0)
        self.nextButton.grid(row=8, column=1)
        self.nextButton['font'] = textFont
