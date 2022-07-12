# Import Base Libs
import tkinter as tk
from tkinter import ttk

"""
Make a class for every new page you want to create, this is to better organize your TK pages.
In the class make a function called create which contains widgets(Labels, Images, TextFeilds)
that you want to on that page.
When making widgets ensure to always use 'self.' before the naming the var.
Always use grid, not pack or place
"""
########################## - Program - ##########################


class page():  # Home page class
    def create(self):  # Function will create widgets when invoked
        self.mainTitle = ttk.Label(
            self,
            text="Password Manager",
            font=("Video Cond", 25))
        self.mainTitle.grid(column=1,row=1)

        self.entryKey = ttk.Label(
            self, text="Enter your 4 digit key!",
            font=("Video Cond", 20))
        self.entryKey.grid(column=1,row=2)

        self.pinEntry = ttk.Entry(self)
        self.pinEntry.grid(column=1,row=3)

        self.loginButton = ttk.Button(
            self,
            text="LOGIN",
            command = self.getPin)
        self.loginButton.grid(column=1,row=4)

        self.error = tk.StringVar()
        self.errorMessage = ttk.Label(
            self,
            textvariable=self.error)
        self.errorMessage.grid(column=1,row=5)