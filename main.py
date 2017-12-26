import os
import tkinter as tk
#import overdrive

#game = overdrive.Overdrive
root = tk.Tk()
def car_accelerate(event):
    #game.changeSpeed(3000, 500)
    print('up')
def car_break(event):
    #game.changeSpeed(0, 1000)
    print('down')


def car_right(event):
    #game.changeLaneRight(500, 500)
    print('right')

def car_left(event):
    #game.changeLaneLeft(500, 500)
    print('left')
def car_turbo(event):
    #game.changeLaneLeft(500, 500)
    print('turboooooo')


def ready():
    #game.turnOnSdkMode()
    root.bind('<Up>', car_accelerate)
    root.bind('<Down>', car_break)
    root.bind('<Right>', car_right)
    root.bind('<Left>', car_left)
    root.bind('<space>', car_turbo)

    root.focus_set()
    root.mainloop()


ready()
