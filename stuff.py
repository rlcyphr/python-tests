# tests for stuff

import tkinter as tk

class Window(tk.Frame):

    # the frame object - create the main frame that all other
    # things will be kept within

    _canvList = {}

    def __init__(self, master=None):

        super().__init__(master) 
        # the instance of tkinter ^^ 
        self.pack() # create the window instance

        mainCanvas = self.createCanvas(100, 100)

        Window._canvList['main'] = mainCanvas

        self.setInput()



    def createCanvas(self, x, y, bk=None):

        # make a new canvas 

        canvas = tk.Canvas(self, width=x, height=y, bg=bk)
        canvas.pack()
        return canvas



    @classmethod
    def showCanvas(self):
        
        for i in Window._canvList: # get a list of all the canvases in this window
            print(i, Window._canvList[i])


    
    def callback_func(self, event):

        # enters the event value automatically when this is called

        print("The new value of the watched variable is: {s}".format(s=self.inVar.get())) 
        # get() the contents of the variable now that the user has entered 
        # a new value 






    def setInput(self):

        self.inVar = tk.StringVar() # a subclass of a variable, to which entry boxes and the like can read and write data
        self.inVar.contents = "This is a string."
        print(self.inVar.contents)

        self.enterBox = tk.Entry() # the entry point for text
        self.enterBox.pack()

        self.enterBox['textvariable'] = self.inVar # set the entry box to read/write to the inVar variable that we just created above


        self.enterBox.bind('<Key-Return>', self.callback_func)






root = tk.Tk()

app = Window(root)

canvas = tk.Canvas(app, width=100, height=100, bg="#bf00bf") # make a 100x100 canvas with an orange background
canvas.pack()

canvas.create_line(0, 0, 100, 100) # make a line

Window._canvList['main'].configure(bg="red")
Window._canvList['main'].create_line(50, 50, 100, 100)

Window.showCanvas()

app.mainloop()