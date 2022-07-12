import tkinter as tk
from tkinter import ttk

class page():
    def create(self):
        self.Title = ttk.Label(self,
                               text="Password Saved!",
                               font=("Video Cond", 25))
        self.Title.grid(column=1, row=1)

        self.goBack = ttk.Button(
            self,
            text="Return", command=self.goBacK)
        self.goBack.grid(column=1, row=2)
