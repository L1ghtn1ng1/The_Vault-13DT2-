# Base libraries
import tkinter as tk
from tkinter import ttk
import os
# Import pages
import loginpage
import Menu
import addingPass
import passGen
import managePass
import displaygeneratedPass
import disppassSaved
import buttonshowPass

class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)  # initialize the superclass(frame)

        # Page list
        # ADD NEW CLASSES YOU MAKE TO LIST!  (pages will be indexed chronologically)
        self.availablePages = [
            loginpage.page,
            Menu.page,
            managePass.page,
            addingPass.page,
            passGen.page,
            displaygeneratedPass.page,
            disppassSaved.page,
            buttonshowPass.page
        ]
        #
        #
        # Split into 3 columns
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)
        self.columnconfigure(index=2, weight=1)

        # Show first page on list at start up
        self.availablePages[0].create(self)

    # Function to change between pages
    def changePage(self, number):
        for widget in self.winfo_children():  # For each widget on scren
            widget.destroy()  # Destroy each widget found
        #
        #
        # Run the create function on the desired page
        self.availablePages[number].create(self)

    def getPin(self):
        self.file = open("topsecret.txt", 'r+')
        self.mainPin = self.file.read()
        try:
            self.pin = self.pinEntry.get()
            if len(self.pin) == 4:
                if self.pin == self.mainPin:
                    print("works")
                    self.changePage(1)
                else:
                    self.error.set("Password is not correct")
                print(int(self.pin))
            else:
                raise Exception
        except:
            self.error.set("Error: Please type in 4 digits!")
    def goBacK(self):
        self.changePage(1)

    def changetoAdding(self):
        self.changePage(3)

    def changetoManage(self):
        self.changePage(2)

    def changetopassGen(self):
        self.changePage(4)
    def logout(self):
        self.changePage(0)
    def gobacktoManage(self):
        self.changePage(2)
    def displayrandomPass(self):
        self.changePage(5)

    def showsavedPass(self,wanted):
        pswds = open("PasswordsList.txt","r")
        for line in pswds:
            lineSplit = line.split(":")
            if wanted == lineSplit[0]:
                self.thePassword = lineSplit[1]
                self.theName = lineSplit[0]
        pswds.close()
        self.changePage(7)

    def SavePass(self):
        passwordsfile = open("PasswordsList.txt","a")
        passwordsfile.write(self.passwordnameEntry.get() +":"+ self.passwordEntry.get()+"\n") #Encrypts password to file
        passwordsfile.close()
        self.changePage(6)



if __name__ == "__main__":  # If this file is run directly, run the following code
    breakOut = 0
    while breakOut == 0:
        if(not os.path.exists("topsecret.txt")):
                newPin = input("New Pin")
                if len(newPin) == 4:
                    confirmPin = input("Confirm Pin")
                    if (confirmPin == newPin):
                            file = open("topsecret.txt", 'a')
                            file.write(newPin)
                            file.close()
                            filething = open("PasswordsList.txt", "w")
                            filething.close()
                            print("Done")
                            breakOut = 1
                elif " " in newPin:
                    print("Please re-enter your pin without spaces!")
                else:
                    print("Please enter 4 digits")
        else:
            breakOut = 1



    root = tk.Tk()  # Create a window
    root.title("The Vault")  # Add title
    app = App(root)  # Link the App and window we made
    app.pack(fill="both", expand=True)  # Allow resizing
    root.mainloop()  # Run the app

    ## TODO
    #Start working on how to use styles

