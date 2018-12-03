from tkinter import *
from math import *
import random

root = Tk()
root.geometry('1000x600')
canv = Canvas(root,  bg='white')
canv.pack(fill=BOTH, expand=1)

for circle_right, circle_up, circle_left, circle_down in [(-300, 500, 300, 1100),
                                                          (600, 400, 1400, 1200),
                                                          (-50, 425, 950, 1425)]:
    canv.create_oval(circle_right, circle_up, circle_left, circle_down, fill="green", outline='green')


turn_point_1, turn_point_2, turn_point_3, turn_point_4 = 0, 139, 727, 1000

global x, y, dx, dy, oval, coordinate_now, coordinate_desired

coordinate_now = random.randint(0, 1000)
coordinate_desired = random.randint(0, 1000)
dx = 1
dy = 1
x = coordinate_now
y = 0


def find_y():
    global x, y
    if turn_point_1 <= x <= turn_point_2:
        y = 800 - sqrt(300 ** 2 - x ** 2)
    elif turn_point_2 <= x <= turn_point_3:
        y = 925 - sqrt(500 ** 2 - (x - 450) ** 2)
    elif turn_point_3 <= x <= turn_point_4:
        y = 800 - sqrt(400 ** 2 - (x - 1000) ** 2)


def coordination():
    global x, y, dx, coordinate_now, coordinate_desired, line, max, min
    if coordinate_now >= coordinate_desired:
        dx = -dx
        canv.delete(line)
        line = canv.create_line(x, y, x - 30, y - 20, width=5, fill="red")
        max = coordinate_now
        min = coordinate_desired
    else:
        dx = dx
        max = coordinate_desired
        min = coordinate_now


def move():
    def run():
        global x, y, dx, dy, oval, coordinate_now, coordinate_desired
        if min <= x <= max:
            x = x + dx
            if turn_point_1 <= x <= turn_point_2:
                f = 800 - sqrt(300 ** 2 - x ** 2)
                dy = f - y
                y = y + dy
                canv.move(oval, dx, dy)
                canv.move(line, dx, dy)
            elif turn_point_2 <= x <= turn_point_3:
                f = 925 - sqrt(500 ** 2 - (x - 450) ** 2)
                dy = f - y
                y = y + dy
                canv.move(oval, dx, dy)
                canv.move(line, dx, dy)
            elif turn_point_3 <= x <= turn_point_4:
                f = 800 - sqrt(400 ** 2 - (x - 1000) ** 2)
                dy = f - y
                y = y + dy
                canv.move(oval, dx, dy)
                canv.move(line, dx, dy)

        root.after(30, run)
    root.after(20, run())


find_y()
oval = canv.create_oval(x - 20, y - 20, x + 20, y + 20, fill="red", outline='red')
line = canv.create_line(x, y, x + 30, y - 20, width=5, fill="red")
coordination()
move()

root.mainloop()