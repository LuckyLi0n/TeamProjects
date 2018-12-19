from tkinter import *
from math import *
import random

root = Tk()
root.geometry('1000x600')
canv = Canvas(root,  bg='DeepSkyBlue')
canv.pack(fill=BOTH, expand=1)


def create_background():
    big_hill = canv.create_oval(325, 275, 1800, 1000, fill='DarkGreen', outline='DarkGreen')

    def mount():
        mount_11 = canv.create_polygon(100, 350, 175, 150, 175, 600, fill='gray42', outline='gray42')
        mount_12 = canv.create_polygon(175, 600, 175, 150, 250, 350, fill='gray45', outline='gray45')
        snow_1 = canv.create_polygon(137, 250, 175, 150, 220, 250, 185, 221, 175, 250, 159, 224, fill='white', outline='white')

        mount_21 = canv.create_polygon(300, 375, 450, 175, 450, 600, fill='gray41', outline='gray41')
        mount_22 = canv.create_polygon(450, 600, 450, 175, 725, 550, fill='gray45', outline='gray45')
        snow_2 = canv.create_polygon(393, 250, 450, 175, 505, 250, 465, 235, 450, 250, 425, 237, fill='white', outline='white')

        mount_31 = canv.create_polygon(100, 400, 300, 75, 300, 600, fill='gray40', outline='gray40')
        mount_32 = canv.create_polygon(300, 600, 300, 75, 550, 525, fill='gray45', outline='gray45')
        snow_3 = canv.create_polygon(223, 200, 300, 75, 370, 200, 330, 170,  300, 200, 275, 165, fill='white', outline='white')

        mount_41 = canv.create_polygon(-50, 500, 100, 200, 100, 600, fill='gray41', outline='gray41')
        mount_42 = canv.create_polygon(100, 600, 100, 200, 250, 525, fill='gray45', outline='gray45')
        snow_4 = canv.create_polygon(62, 275, 100, 200, 137, 275, 115, 257, 100, 275, 85, 255, fill='white', outline='white')

    def forest():
        tree1 = canv.create_polygon(587, 350, 600, 300, 613, 350, fill='SpringGreen4', outline='SpringGreen4')
        canv.create_line(600, 350, 600, 363, width=4, fill='Sienna')


        tree2 = canv.create_polygon(587, 350, 600, 300, 613, 350, fill='SpringGreen4', outline='SpringGreen4')
        canv.create_line(600, 350, 600, 363, width=4, fill='Sienna')

        canv.create_line(775, 425, 775, 450, width=4, fill='Sienna')
        tree3 = canv.create_polygon(750, 425, 775, 350, 800, 425, fill='SpringGreen4', outline='SpringGreen4')

        canv.create_line(900, 375, 900, 392, width=4, fill='Sienna')
        tree4 = canv.create_polygon(880, 375, 900, 315, 920, 375, fill='SpringGreen4', outline='SpringGreen4')

        tree5 = canv.create_polygon(587, 350, 600, 300, 613, 350, fill='SpringGreen4', outline='SpringGreen4')
        canv.create_line(600, 350, 600, 363, width=4, fill='Sienna')

        canv.create_line(975, 300, 975, 312, width=4, fill='Sienna')
        tree6 = canv.create_polygon(963, 300, 975, 250, 988, 300, fill='SpringGreen4', outline='SpringGreen4')

        tree_snow_1 = canv.create_polygon(596, 313, 600, 300, 604, 313, fill='white', outline='white')
        tree_snow_2 = canv.create_polygon(971, 263, 975, 250, 979, 263, fill='white', outline='white')

    forest()


    """!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""

    snow_5 = canv.create_polygon(0, 0, 15, 0, 5, 0, fill='white', outline='white')
    snow_6 = canv.create_polygon(0, 0, 5, 0, 5, 0, fill='white', outline='white')
    snow_7 = canv.create_polygon(10, 0, 5, 0, 5, 0, fill='white', outline='white')


    def create_sun():

        sun = canv.create_oval(900, 100, 1100, -100, fill='gold', outline='gold')

        sunray_1 = canv.create_line(1000, 0, 795, 25, width=2, fill='gold')
        sunray_2 = canv.create_line(1000, 0, 835, 50, width=2, fill='gold')
        sunray_3 = canv.create_line(1000, 0, 810, 80, width=2, fill='gold')
        sunray_4 = canv.create_line(1000, 0, 860, 90, width=2, fill='gold')
        sunray_5 = canv.create_line(1000, 0, 875, 130, width=2, fill='gold')
        sunray_6 = canv.create_line(1000, 0, 925, 125, width=2, fill='gold')
        sunray_7 = canv.create_line(1000, 0, 950, 170, width=2, fill='gold')
        sunray_8 = canv.create_line(1000, 0, 980, 130, width=2, fill='gold')


    def create_cloud():
        coord_clouds = [(30, 60), (200, 110), (400, 60), (600, 160), (800, 200)]
        for x, y in coord_clouds:
            centers = [(x, y), (x+20, y), (x+40, y), (x+10, y-20), (x+30, y-20)]
            for circle_x, circle_y in centers:
                r = 20
                Cloud = canv.create_oval(circle_x-r, circle_y-r, circle_x+r, circle_y+r, fill='white', outline='white')



    create_cloud()
    create_sun()
    mount()

    for circle_right, circle_up, circle_left, circle_down in [(-300, 500, 300, 1100),
                                                              (600, 400, 1400, 1200),
                                                              (-50, 425, 950, 1425),
                                                              (600, 300, 3000, 2700)]:
        canv.create_oval(circle_right, circle_up, circle_left, circle_down, fill="ForestGreen", outline='ForestGreen')


turn_point_1, turn_point_2, turn_point_3, turn_point_4 = 0, 139, 727, 1000

global x, y, dx, dy, oval, coordinate_now, coordinate_desired

coordinate_now = random.randint(0, 1000)
"""Сюда должна передавать нынешняя координата цента пушки"""
coordinate_desired = random.randint(0, 1000)
"""Сюда должна передавваться координата X от нажатия правой кнопки мышки"""
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
    """Сравнивает нынешнее положение пушки с тем, в котором пушка хочет оказаться.
    В зависимость от этого пересчитывает dx"""
    global x, y, dx, coordinate_now, coordinate_desired, line, max, min
    if coordinate_now >= coordinate_desired:
        dx = -dx
        canv.delete(line)
        line = canv.create_line(x, y, x - 30, y - 20, width=5, fill="purple")
        max = coordinate_now
        min = coordinate_desired
    else:
        dx = dx
        max = coordinate_desired
        min = coordinate_now


def move():
    """"Двигает пушку в нужную координату"""
    def run():
        global x, y, dx, dy, oval, coordinate_now, coordinate_desired, max, min
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


create_background()
find_y()
oval = canv.create_oval(x - 20, y - 20, x + 20, y + 20, fill="pink", outline='purple')
line = canv.create_line(x, y, x + 30, y - 20, width=5, fill="purple")
coordination()
move()

root.mainloop()
