import tkinter as tk
from tkinter import ttk
import random
import string

class page():
    def create(self):
        self.letter_digit_list = list(string.digits + string.ascii_letters)
        # shuffle random source of letters and digits
        random.shuffle(self.letter_digit_list)

        # first generate 4 random digits
        self.sample_str = ''.join((random.choice(string.digits) for i in range(7)))

        # Now create random string of length 6 which is a combination of letters and digits
        # Next, concatenate it with sample_str
        self.sample_str += ''.join((random.choice(self.letter_digit_list) for i in range(8)))
        self.aList = list(self.sample_str)
        random.shuffle(self.aList)

        self.final_str = ''.join(self.aList)

        # Output ~ 81OYQ6D430'''

        self.Title = ttk.Label(self,
                               text = "Here is your password!",
                               font = ("Video Cond", 25))
        self.Title.grid(column = 1, row = 1)

        self.generatedPass = ttk.Label(self,
                                       text = self.final_str,
                                       font=("Video Cont", 25))
        self.generatedPass.grid(column = 1, row = 2)



        self.goBack = ttk.Button(
            self,
            text="Return", command=self.goBacK)
        self.goBack.grid(column=1, row=3)

