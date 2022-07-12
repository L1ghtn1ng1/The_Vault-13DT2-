import tkinter as tk
from tkinter import ttk


class page():
    def create(self):
        self.pswdBtnList = []
        self.passwords = []
        try:
            filething = open("PasswordsList.txt", "r")
            for line in filething:
                lineList = line.split(":")
                self.pswdBtnList.append(lineList[0])
                self.passwords.append(lineList[1])
            filething.close()
        except:
            print("No passwords found yet")
            self.Title = ttk.Label(self,
                                   text="Manage Passwords",
                                   font=("Video Cond", 25))
            self.Title.grid(column=1, row=0)

        for element in self.pswdBtnList:
            self.details = ttk.Button(self,
                                      text=element,
                                      command=lambda: self.showsavedPass(element))
            self.details.grid(column=1, row=self.pswdBtnList.index(element) + 1)

        self.addPassword = ttk.Button(self,
                                  text="Add Password",
                                  command=self.changetoAdding)
        self.addPassword.grid(column=1, row=998)

        self.goBack = ttk.Button(
            self,
            text="Cancel", command=self.goBacK)
        self.goBack.grid(column=1, row=999)
