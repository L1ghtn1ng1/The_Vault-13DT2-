from tkinter import *

tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('Button Background Example')

button = Button(tkWindow, text='Submit', bg='blue', fg='white')
button.pack()

tkWindow.mainloop()