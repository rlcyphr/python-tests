# tests for stuff

import Tkinter as tk

class App(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.createButton()

    def createButton(self):
        newButton = tk.Button(self, text="This is a button.")
        newButton.pack()

root = tk.Tk()

newthing = App(root)