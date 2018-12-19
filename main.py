from random import randrange as rnd, choice
from tkinter import *
import math
import time

root = Tk()
fr = Frame(root)
root.geometry('800x600+600+100')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

colors = ['blue', 'green', 'red', 'brown']


class ball():
    def __init__(self, balls, x=40, y=450):
        self.x = x
        self.y = y
        self.r = 8
        self.color = choice(colors)
        self.points = 3
        self.id = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color)
        # self.id_points = canv.create_text(self.x,self.y,text = self.points)
        self.live = 200
        self.nature = 1
        self.balls = balls
        self.bum_time = 100
        self.bum_on = 0
        self.surprize = 0
        self.surprize_time = 0

    def paint(self):
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        # canv.coords(self.id_points,self.x,self.y)
        # canv.itemconfig(self.id_points,text = self.points)

    def move(self):
        if self.y <= 500:
            self.vy += 0.07
            self.y += self.vy
            self.x += self.vx
            self.vx *= 0.999
            self.v = (self.vx ** 2 + self.vy ** 2) ** 0.5
            self.an = math.atan(self.vy / self.vx)
            self.paint()
        else:
            if self.vx ** 2 + self.vy ** 2 > 10:
                self.vy = -self.vy * 0.7
                self.vx = self.vx * 0.7
                self.y = 499
            if self.live < 0:
                self.kill()
            else:
                self.live -= 1
        if self.x > 780:
            self.vx = - self.vx / 2
            self.x = 779
        if self.bum_on and self.nature:
            self.bum_time -= 1
            if self.bum_time <= 0:
                self.bum()
        if not self.nature:
            self.live -= 0.1
            if self.r > 0.1:
                self.r -= 0.1
            else:
                self.kill()
            self.vy += 0.2
            if self.live < 0:
                self.kill()
        if self.surprize:
            self.surprize_time += 1
            if self.surprize_time > 13:
                self.surprize_time = 0
                self.fire()

    def hittest(self, ob):
        if abs(ob.x - self.x) <= (self.r + ob.r) and abs(ob.y - self.y) <= (self.r + ob.r):
            return True
        else:
            return False

    def ricochet(self, w):
        self.v = (self.vx ** 2 + self.vy ** 2) ** 0.5
        self.an = math.atan(self.vy / self.vx)

        if self.x == w.x:
            self.x += 1

        if w.x - (self.x + self.vx):
            an_rad = math.atan((w.y - (self.y + self.vy)) / (w.x - (self.x + self.vx)))
            an_res = an_rad - (self.an - an_rad)

            vx2 = 0.8 * self.v * math.cos(an_res)
            vy2 = 0.8 * self.v * math.sin(an_res)
            if self.an > 0 and self.vx < 0 and self.vy < 0 or self.an < 0 and self.vx < 0:
                vx2 = -vx2
                vy2 = -vy2
            self.vx = -vx2
            self.vy = -vy2
            self.move()
            self.points += 1

    def kill(self):
        canv.delete(self.id)
        # canv.delete(self.id_points)
        try:
            self.balls.pop(self.balls.index(self))
        except:
            pass

    def fire(self):
        n = 5
        for z in range(1, n + 1):
            new_ball = ball(self.balls)
            new_ball.r = 5
            v = 5 + rnd(5)
            an = z * 2 * math.pi / n + rnd(-2, 3) / 7
            new_ball.vx = v * math.cos(an)
            new_ball.vy = v * math.sin(an)
            new_ball.x = self.x + new_ball.vx * 3
            new_ball.y = self.y + new_ball.vy * 3
            new_ball.nature = 0
            new_ball.points = 1
            new_ball.live = rnd(10) + 30
            new_ball.color = choice(colors)
            self.balls += [new_ball]

    def bum(self):
        self.fire()
        self.kill()


class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.on = 1
        self.an = 1
        self.points = 0
        self.id = canv.create_line(20, 450, 50, 420, width=7, smooth=1)
        self.id_points = canv.create_text(30, 30, text=self.points, font='28')

        self.balls = []
        self.bullet = 0
        self.targets = []
        self.walls = []

    def fire2_start(self, event):
        self.f2_on = 1

    def stop(self):
        self.f2_on = 0
        self.on = 0

    def fire2_end(self, event):
        self.bullet += 1
        new_ball = ball(self.balls)
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an) / 7
        new_ball.vy = self.f2_power * math.sin(self.an) / 7
        if not rnd(12):
            new_ball.surprize = 1
        self.balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 35

    def targetting(self, event=0):
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450, 20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an))

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')

    def bum(self, event=0):
        for b in self.balls[::-1]:
            if b.nature:
                b.bum()
                break


class target():
    def __init__(self, targets):
        self.points = 1
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 500)
        r = self.r = rnd(10, 40)
        self.live = 5 + rnd(5)
        self.change_color = 0
        color = self.color = 'red'
        self.id = canv.create_oval(x - r, y - r, x + r, y + r, fill=self.color)
        self.id_live = canv.create_text(x, y, text=self.live)
        self.targets = targets

    def hit(self, points=1):
        self.live -= points
        canv.itemconfig(self.id_live, text=self.live)
        canv.itemconfig(self.id, fill='orange')
        self.change_color = 10
        if self.live < 1:
            self.kill()

    def kill(self):
        self.targets.pop(self.targets.index(self))
        canv.delete(self.id)
        canv.delete(self.id_live)


g1 = gun()

while 1:
    balls = g1.balls
    targets = g1.targets
    walls = g1.walls
    g1.on = 1
    for z in range(rnd(3, 7)):
        targets += [target(targets)]

    for z in range(rnd(1, 8)):
        walls += [target(walls)]
        walls[-1].x = rnd(200, 600)
        walls[-1].y = rnd(100, 400)
        walls[-1].r = rnd(20, 50)
        canv.delete(walls[-1].id_live)
        canv.itemconfig(walls[-1].id, fill='gray', width=0)
        canv.coords(walls[-1].id, walls[-1].x - walls[-1].r, walls[-1].y - walls[-1].r, walls[-1].x + walls[-1].r,
                    walls[-1].y + walls[-1].r)

    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<Button-3>', g1.bum)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    result = canv.create_text(400, 300, text='', font="28")
    z = 0.03
    while targets or balls:
        for b in balls:
            b.move()
            for w in walls:
                if b.hittest(w):
                    b.ricochet(w)

            for b_test in balls:
                if b != b_test and b.hittest(b_test):
                    if b.nature:
                        b_test.ricochet(b)
                        if b_test.nature:
                            b.ricochet(b_test)
                            b_test.bum()

            for t in targets:
                if b.hittest(t):
                    b.kill()
                    t.hit(b.points)
                    g1.points += 1
                    canv.itemconfig(g1.id_points, text=g1.points)

        if not targets and g1.on:
            canv.bind('<Button-1>', '')
            canv.bind('<ButtonRelease-1>', '')
            g1.stop()
            canv.itemconfig(result, text='Вы уничтожили все цели за ' + str(g1.bullet) + ' выстрелов')
            for b in balls:
                b.bum_time = 20
                b.bum_on = 1

        for t in targets:
            if t.change_color <= 0:
                canv.itemconfig(t.id, fill=t.color)
            else:
                t.change_color -= 1
        canv.update()

        t = 0.008 - (len(balls) - 5) * 0.0001
        t = max(t, 0)
        time.sleep(t)
        g1.targetting()
        g1.power_up()
    canv.update()
    time.sleep(0.1)
    canv.delete(result)
from random import randrange as rnd, choice
from tkinter import *
import math
import time

root = Tk()
fr = Frame(root)
root.geometry('800x600+600+100')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

colors = ['blue', 'green', 'red', 'brown']


class ball():
    def __init__(self, balls, x=40, y=450):
        self.x = x
        self.y = y
        self.r = 8
        self.color = choice(colors)
        self.points = 3
        self.id = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color)
        # self.id_points = canv.create_text(self.x,self.y,text = self.points)
        self.live = 200
        self.nature = 1
        self.balls = balls
        self.bum_time = 100
        self.bum_on = 0
        self.surprize = 0
        self.surprize_time = 0

    def paint(self):
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        # canv.coords(self.id_points,self.x,self.y)
        # canv.itemconfig(self.id_points,text = self.points)

    def move(self):
        if self.y <= 500:
            self.vy += 0.07
            self.y += self.vy
            self.x += self.vx
            self.vx *= 0.999
            self.v = (self.vx ** 2 + self.vy ** 2) ** 0.5
            self.an = math.atan(self.vy / self.vx)
            self.paint()
        else:
            if self.vx ** 2 + self.vy ** 2 > 10:
                self.vy = -self.vy * 0.7
                self.vx = self.vx * 0.7
                self.y = 499
            if self.live < 0:
                self.kill()
            else:
                self.live -= 1
        if self.x > 780:
            self.vx = - self.vx / 2
            self.x = 779
        if self.bum_on and self.nature:
            self.bum_time -= 1
            if self.bum_time <= 0:
                self.bum()
        if not self.nature:
            self.live -= 0.1
            if self.r > 0.1:
                self.r -= 0.1
            else:
                self.kill()
            self.vy += 0.2
            if self.live < 0:
                self.kill()
        if self.surprize:
            self.surprize_time += 1
            if self.surprize_time > 13:
                self.surprize_time = 0
                self.fire()

    def hittest(self, ob):
        if abs(ob.x - self.x) <= (self.r + ob.r) and abs(ob.y - self.y) <= (self.r + ob.r):
            return True
        else:
            return False

    def ricochet(self, w):
        self.v = (self.vx ** 2 + self.vy ** 2) ** 0.5
        self.an = math.atan(self.vy / self.vx)

        if self.x == w.x:
            self.x += 1

        if w.x - (self.x + self.vx):
            an_rad = math.atan((w.y - (self.y + self.vy)) / (w.x - (self.x + self.vx)))
            an_res = an_rad - (self.an - an_rad)

            vx2 = 0.8 * self.v * math.cos(an_res)
            vy2 = 0.8 * self.v * math.sin(an_res)
            if self.an > 0 and self.vx < 0 and self.vy < 0 or self.an < 0 and self.vx < 0:
                vx2 = -vx2
                vy2 = -vy2
            self.vx = -vx2
            self.vy = -vy2
            self.move()
            self.points += 1

    def kill(self):
        canv.delete(self.id)
        # canv.delete(self.id_points)
        try:
            self.balls.pop(self.balls.index(self))
        except:
            pass

    def fire(self):
        n = 5
        for z in range(1, n + 1):
            new_ball = ball(self.balls)
            new_ball.r = 5
            v = 5 + rnd(5)
            an = z * 2 * math.pi / n + rnd(-2, 3) / 7
            new_ball.vx = v * math.cos(an)
            new_ball.vy = v * math.sin(an)
            new_ball.x = self.x + new_ball.vx * 3
            new_ball.y = self.y + new_ball.vy * 3
            new_ball.nature = 0
            new_ball.points = 1
            new_ball.live = rnd(10) + 30
            new_ball.color = choice(colors)
            self.balls += [new_ball]

    def bum(self):
        self.fire()
        self.kill()


class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.on = 1
        self.an = 1
        self.points = 0
        self.id = canv.create_line(20, 450, 50, 420, width=7, smooth=1)
        self.id_points = canv.create_text(30, 30, text=self.points, font='28')

        self.balls = []
        self.bullet = 0
        self.targets = []
        self.walls = []

    def fire2_start(self, event):
        self.f2_on = 1

    def stop(self):
        self.f2_on = 0
        self.on = 0

    def fire2_end(self, event):
        self.bullet += 1
        new_ball = ball(self.balls)
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an) / 7
        new_ball.vy = self.f2_power * math.sin(self.an) / 7
        if not rnd(12):
            new_ball.surprize = 1
        self.balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 35

    def targetting(self, event=0):
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450, 20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an))

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')

    def bum(self, event=0):
        for b in self.balls[::-1]:
            if b.nature:
                b.bum()
                break


class target():
    def __init__(self, targets):
        self.points = 1
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 500)
        r = self.r = rnd(10, 40)
        self.live = 5 + rnd(5)
        self.change_color = 0
        color = self.color = 'red'
        self.id = canv.create_oval(x - r, y - r, x + r, y + r, fill=self.color)
        self.id_live = canv.create_text(x, y, text=self.live)
        self.targets = targets

    def hit(self, points=1):
        self.live -= points
        canv.itemconfig(self.id_live, text=self.live)
        canv.itemconfig(self.id, fill='orange')
        self.change_color = 10
        if self.live < 1:
            self.kill()

    def kill(self):
        self.targets.pop(self.targets.index(self))
        canv.delete(self.id)
        canv.delete(self.id_live)


g1 = gun()

while 1:
    balls = g1.balls
    targets = g1.targets
    walls = g1.walls
    g1.on = 1
    for z in range(rnd(3, 7)):
        targets += [target(targets)]

    for z in range(rnd(1, 8)):
        walls += [target(walls)]
        walls[-1].x = rnd(200, 600)
        walls[-1].y = rnd(100, 400)
        walls[-1].r = rnd(20, 50)
        canv.delete(walls[-1].id_live)
        canv.itemconfig(walls[-1].id, fill='gray', width=0)
        canv.coords(walls[-1].id, walls[-1].x - walls[-1].r, walls[-1].y - walls[-1].r, walls[-1].x + walls[-1].r,
                    walls[-1].y + walls[-1].r)

    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<Button-3>', g1.bum)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    result = canv.create_text(400, 300, text='', font="28")
    z = 0.03
    while targets or balls:
        for b in balls:
            b.move()
            for w in walls:
                if b.hittest(w):
                    b.ricochet(w)

            for b_test in balls:
                if b != b_test and b.hittest(b_test):
                    if b.nature:
                        b_test.ricochet(b)
                        if b_test.nature:
                            b.ricochet(b_test)
                            b_test.bum()

            for t in targets:
                if b.hittest(t):
                    b.kill()
                    t.hit(b.points)
                    g1.points += 1
                    canv.itemconfig(g1.id_points, text=g1.points)

        if not targets and g1.on:
            canv.bind('<Button-1>', '')
            canv.bind('<ButtonRelease-1>', '')
            g1.stop()
            canv.itemconfig(result, text='Вы уничтожили все цели за ' + str(g1.bullet) + ' выстрелов')
            for b in balls:
                b.bum_time = 20
                b.bum_on = 1

        for t in targets:
            if t.change_color <= 0:
                canv.itemconfig(t.id, fill=t.color)
            else:
                t.change_color -= 1
        canv.update()

        t = 0.008 - (len(balls) - 5) * 0.0001
        t = max(t, 0)
        time.sleep(t)
        g1.targetting()
        g1.power_up()
    canv.update()
    time.sleep(0.1)
    canv.delete(result)

