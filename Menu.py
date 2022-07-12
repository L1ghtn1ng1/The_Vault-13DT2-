import tkinter as tk
from tkinter import ttk

class page():
    def create(self):
        self.Title = ttk.Label(
            self,
            text="Menu",
            font=("Video Cond", 25))
        self.Title.grid(column=1, row=1)

        self.welcomeLabel = ttk.Label(self, text="Welcome Back!", font=("Video Cond", 20))
        self.welcomeLabel.grid(column=1, row=2)
        #
        self.instructionsLabel = ttk.Label(
            self,
            text="Please select one of the options.",
            font=("Video Cond", 20))
        self.instructionsLabel.grid(column=1, row=3)

        self.manageLabel = ttk.Button(
            self,
            text="Manage Passwords", command= self.changetoManage)
        self.manageLabel.grid(column=1, row=4)

        self.passGenerator = ttk.Button(
            self,
            text="Password Generator", command= self.changetopassGen)
        self.passGenerator.grid(column=1, row=5)

        self.logoff = ttk.Button(
            self,
            text="Log Out", command=self.logout)
        self.logoff.grid(column=1, row=6)