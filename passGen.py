import tkinter as tk
from tkinter import ttk

class page():
    def create(self):

        self.Title = ttk.Label(self,
                               text = "Password Generator",
                               font = ("Video Cond", 25))
        self.Title.grid(column = 1, row = 1)

        self.details = ttk.Button(self,
                                  text = "Generate Password!",
                                  command= self.displayrandomPass)
        self.details.grid(column = 1, row = 2)

        self.goBack = ttk.Button(
            self,
            text="Cancel", command=self.goBacK)
        self.goBack.grid(column=1, row=3)




