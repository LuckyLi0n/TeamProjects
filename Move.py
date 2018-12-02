from tkinter import *
from math import *
import time

root = Tk()
root.geometry('1000x600')
canv = Canvas(root,  bg='white')
canv.pack(fill=BOTH, expand=1)



for circle_right, circle_up, circle_left, circle_down in [(-300, 500, 300, 1100),
                                                          (600, 400, 1400, 1200), (-50, 425, 950, 1425)]:
    canv.create_oval(circle_right, circle_up, circle_left, circle_down, fill="green", outline='green')



global x, y, dx, dy
dx = 1
dy = 1
y = 500
x = 0
oval = canv.create_oval(x - 20, y - 20, x + 20, y + 20, fill="red", outline='red')
line = canv.create_line(x , y, x + 30, y - 20, width=5, fill="red")


def move():
    def flight():
        global x, y, dx, dy
        if x in range(0, 400):
            """Вторая координата определяется по нажатию мышки"""
            x = x + dx
            if x in range(0, 138):
                f = 800 - sqrt(300 ** 2 - x ** 2)
                dy = f - y
                y = y + dy
                canv.move(oval, dx, dy)
                canv.move(line, dx, dy)
            elif x in range(138, 727):
                f = 925 - sqrt(500 ** 2 - (x - 450) ** 2)
                dy = f - y
                y = y + dy
                canv.move(oval, dx, dy)
                canv.move(line, dx, dy)
            elif x in range(727, 1000):
                f = 800 - sqrt(400 ** 2 - (x - 1000) ** 2)
                dy = f - y
                y = y + dy
                canv.move(oval, dx, dy)
                canv.move(line, dx, dy)

        root.after(20, flight)
    root.after(20, flight())


move()

root.mainloop()
