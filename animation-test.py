# test of animating something using tkinter

import tkinter as tk
import math

class App(tk.Frame):

    def __init__(self):
        super().__init__(tk.Tk())
        self.pack()
        self.window = tk.Canvas(self, width=1100, height=500)
        self.window.pack()

        #self.draw_sine(250, 0.01)

        for i in range(1, 20):
            self.draw_sine(i, i*math.cos(math.sqrt(i**-2/270) * math.pi)**-1)

    def draw_sine(self, amp, f):

        # draw a sine wave
        # math.sin(i/180 * pi)
        '''
        for i in range(720): # for each value of x
            self.window.create_line(i, (math.sin(i/180 * math.pi) * 250) + 250,
             i, (math.sin(i/180 * math.pi) * 250 + 1) + 250)
        '''

        for i in range(1080): # for each value of x
            self.window.create_line(i, (math.sin(i * f) * amp) + 250,
             i, (math.tan((i+1) * f) * amp) + 250)



'''
class AnimatedThing:

    def __init__(self):
        self.root = Tk()
        self.window = Canvas(self.root, width=360, height=500)
        self.window.pack()

    def drawLine(self):

        # this will loop through each value of x,
        # setting the value of y to the sine value of
        # whatever x is currently, amplified by 250
        # to make it visible
'''








def main():

    #newThing = AnimatedThing()
    app = App()

    tk.mainloop()

main()