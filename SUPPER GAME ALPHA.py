from random import randrange as rnd, choice, uniform
from tkinter import *
from math import *
import time

root = Tk()
root.geometry('1000x600')
canv = Canvas(root,  bg='DeepSkyBlue')
canv.pack(fill=BOTH, expand=1)

colors = ['blue', 'green', 'red', 'brown']

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






    snow_5 = canv.create_polygon(0, 0, 15, 0, 5, 0, fill='white', outline='white')
    snow_6 = canv.create_polygon(0, 0, 5, 0, 5, 0, fill='white', outline='white')
    snow_7 = canv.create_polygon(10, 0, 5, 0, 5, 0, fill='white', outline='white')

    def create_sun():
        un = canv.create_oval(900, 100, 1100, -100, fill='gold', outline='gold')
        for end_x, end_y in [(795, 25), (835, 50), (810, 80), (860, 90), (875, 130) ,(925, 125), (950, 170), (980, 130)]:
            sunray = canv.create_line(1000, 0, end_x, end_y, width=2, fill='gold')

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
    forest()

    for circle_right, circle_up, circle_left, circle_down in [(-300, 500, 300, 1100),
                                                              (600, 400, 1400, 1200),
                                                              (-50, 425, 950, 1425),
                                                              (600, 300, 3000, 2700)]:
        canv.create_oval(circle_right, circle_up, circle_left, circle_down, fill="ForestGreen", outline='ForestGreen')


create_background()






class ball():
    def __init__(self, balls, x=10, y=10):
        """СОЗДАЕТ ШАРИК В ОПРЕДЕЛЕННОЙ КООРДИНАТЕ, ЗАДАЕТ ЕГО ОСНОВНЫЕ ПАРАМЕТРЫ"""
        self.x = x
        self.y = y
        self.r = 8
        self.color = choice(colors)
        self.points = 3
        self.id = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color)
        self.live = 10
        '''отвечает за скорость исчезновения'''
        self.nature = 1
        """пока хз что это"""
        self.balls = balls
        self.bum_time = 10
        self.bum_on = 0
        self.vx_wind = uniform(-0.05, 0.05)
        self.vy_wind = uniform(-0.01, 0.05)
        self.turn_point_1, self.turn_point_2, self.turn_point_3, self.turn_point_4 = 0, 139, 727, 1000

    def paint(self):
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

        """отвечает за отрисовку шарика в новой коордитате"""

    def move(self):

        if self.turn_point_1 <= self.x <= self.turn_point_2:
            y = 800 - sqrt(300 ** 2 - self.x ** 2)
        elif self.turn_point_2 <= self.x <= self.turn_point_3:
            y = 925 - sqrt(500 ** 2 - (self.x - 450) ** 2)
        elif self.turn_point_3 <= self.x <= self.turn_point_4:
            y = 800 - sqrt(400 ** 2 - (self.x - 1000) ** 2)

        if self.y <= y:
            self.vy += 0.1
            self.y += self.vy + self.vx_wind
            self.x += self.vx
            self.vx *= (0.999-self.vy_wind)
            self.v = (self.vx ** 2 + self.vy ** 2) ** 0.5
            """считает полную скорость шарика"""
            self.an = atan(self.vy / self.vx)
            self.paint()

            """уничтожает шарик"""
        else:
            self.live -= 1
            if self.live < 0:
                self.bum()

            """отвечает за поворот шарика при ударе о стену"""
        if self.x > 1000:
            self.vx = - self.vx / 2
            self.x = 999
        elif self.x < 0:
            self.vx = - self.vx / 2
            self.x = 1





    def kill(self):
        canv.delete(self.id)
        try:
            '''отвечает за удаление шарика для перевода хода'''
            self.balls.pop(self.balls.index(self))

        except:
            pass

    def bum(self):
        if self.nature:
            self.kill()





































class gun():
    def __init__(self):
        self.f2_power = 10
        self.x = 10
        self.y = 500
        self.f2_on = 0
        self.on = 1
        self.an = 1
        self.points = 0
        self.dx = 1
        self.dy = 1
        self.min = 0
        self.max = 0
        self.vx = 0
        self.f = 0

        self.id = canv.create_line(self.x, self.y, self.x + 30, self.y - 20, width=5, fill="purple")
        self.oval = canv.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill="pink", outline='purple')
        self.id_points = canv.create_text(30, 30, text=self.points, font='28')
        self.turn_point_1, self.turn_point_2, self.turn_point_3, self.turn_point_4 = 0, 139, 727, 1000

        self.bullet = 0

    def fire_start(self, event):
        if self.on:
            self.f2_on = 1

    def stop(self):
        self.f2_on = 0
        self.on = 0

    def fire_end(self, event):
        if self.on:
            self.bullet += 1
            new_ball = ball(self.balls)
            new_ball.r += 5
            new_ball.x = self.x
            new_ball.y = self.y
            new_ball.vx = self.f2_power * cos(self.an) / 9
            new_ball.vy = self.f2_power * sin(self.an) / 9
            self.balls += [new_ball]
            self.f2_on = 0
            self.f2_power = 35

    def moved(self, event):
        print('Hello')

        print()

        def find_y():
            if self.turn_point_1 <= self.x <= self.turn_point_2:
                self.y = 800 - sqrt(300 ** 2 - self.x ** 2)
            elif self.turn_point_2 <= self.x <= self.turn_point_3:
                self.y = 925 - sqrt(500 ** 2 - (self.x - 450) ** 2)
            elif self.turn_point_3 <= self.x <= self.turn_point_4:
                self.y = 800 - sqrt(400 ** 2 - (self.x - 1000) ** 2)

        def coordination():

            """Сравнивает нынешнее положение пушки с тем, в котором пушка хочет оказаться.
            В зависимость от этого пересчитывает dx"""
            if self.x >= event.x:
                self.dx = - self.dx
                canv.delete(self.oval)
                canv.delete(self.id)

                self.oval = canv.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill="pink",
                                             outline='purple')
                self.id = canv.create_line(self.x, self.y, self.x - 30, self.y - 20, width=5, fill="purple")

                self.max = self.x
                self.min = event.x
            else:
                self.dx = self.dx
                self.max = event.x
                self.min = self.x

        def run():
            if self.min <= self.x <= self.max:
                self.x = self.x + self.dx
                if self.turn_point_1 <= self.x <= self.turn_point_2:
                    self.f = 800 - sqrt(300 ** 2 - self.x ** 2)
                    self.dy = self.f - self.y
                    self.y = self.y + self.dy
                    canv.move(self.oval, self.dx, self.dy)
                    canv.move(self.id, self.dx, self.dy)
                elif self.turn_point_2 <= self.x <= self.turn_point_3:
                    self.f = 925 - sqrt(500 ** 2 - (self.x - 450) ** 2)
                    self.dy = self.f - self.y
                    self.y = self.y + self.dy
                    canv.move(self.oval, self.dx, self.dy)
                    canv.move(self.id, self.dx, self.dy)
                elif self.turn_point_3 <= self.x <= self.turn_point_4:
                    self.f = 800 - sqrt(400 ** 2 - (self.x - 1000) ** 2)
                    self.dy = self.f - self.y
                    self.y = self.y + self.dy
                    canv.move(self.oval, self.dx, self.dy)
                    canv.move(self.id, self.dx, self.dy)

            root.after(40, run)

        find_y()
        coordination()
        run()
        root.after(40, run())








    def aiming(self, event=0):
        if event:
            if abs(event.x - self.x) < 0.0001:
                event.x += 0.1
            self.an = atan((event.y - self.y) / (event.x - self.x))
            if event.x < self.x:
                self.an += pi

        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            pass

        canv.coords(self.id, self.x, self.y, self.x + 30 * cos(self.an), self.y + 30 * sin(self.an))

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='purple')

    def bum(self, event=0):
        for b in self.balls[::-1]:
            if b.nature:
                b.bum()
                break




class game():
    def __init__(self):
        self.moving = []
        self.gamer1 = gun()
        self.gamer2 = gun()
        self.gamer1.x = 10
        self.gamer1.y = 500
        self.gamer2.x = 990
        self.gamer2.y = 400
        self.gamer1.balls = self.moving
        self.gamer2.balls = self.moving
        self.active_gamer = self.gamer1

        canv.bind('<Button-1>', self.fire_start)
        canv.bind('<Button-3>', self.moved)
        canv.bind('<ButtonRelease-1>', self.fire_end)
        canv.bind('<Motion>', self.aiming)

        self.go = 1


    def fire_start(self, event):
        self.active_gamer.fire_start(event)

    def fire_end(self, event):
        self.active_gamer.fire_end(event)
        self.active_gamer.stop()

    def aiming(self, event):
        self.active_gamer.aiming(event)

    def power_up(self, event):
        self.active_gamer.power_up(event)

    def move(self, event):
        self.active_gamer.move(event)

    def moved(self, event):
        self.active_gamer.moved(event)

    def round(self):
        if self.active_gamer == self.gamer1:
            self.active_gamer = self.gamer2
            print('g1')
        else:
            self.active_gamer = self.gamer1
            print('g2')

        self.active_gamer.on = 1

        while self.active_gamer.on or self.moving:
            for m in self.moving:
                m.move()
            self.active_gamer.aiming()
            self.active_gamer.power_up()
            canv.update()
            time.sleep(0.007)


game1 = game()
while 1:
    game1.round()
