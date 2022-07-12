import tkinter as tk
from tkinter import ttk


class page():
    def create(self):
        self.Title = ttk.Label(self,
                               text="Here are your details.",
                               font=("Video Cond", 25))
        self.Title.grid(column=1, row=1)

        self.passwordName = ttk.Label(self,
                                      text="Password Name:" + "\n" + self.theName,
                                      font=("Video Cond", 18), justify='center')
        self.passwordName.grid(column=1, row=2)

        self.passwordName = ttk.Label(self,
                                      text="Password:" + "\n" + self.thePassword,
                                      font=("Video Cond", 18), justify='center')
        self.passwordName.grid(column=1, row=3)

        self.goBack = ttk.Button(
            self,
            text="Return", command=lambda: self.changePage(1))
        self.goBack.grid(column=1, row=5)
