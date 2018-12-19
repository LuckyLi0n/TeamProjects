from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk


def start_callback():
    return


def help_callback():
    help_window = Toplevel(root)
    help_window.geometry("400x400")
    text = Text(help_window, width=100, height=100, font=Font(family='Helvetica', size=10))
    text.pack(expand='yes', fill='both')

    with open("game_rules.txt", mode="r", encoding="utf-8") as f:
        text.insert(END, f.read())

    Button(help_window, text='OK', command=help_window.destroy).pack(side=BOTTOM, pady=30)
    return


root = Tk()
root.geometry('1000x600')
canv = Canvas(root,  bg='green')
canv.pack(fill=BOTH, expand=1)

canv.create_text(500, 200, text="Добро пожаловать в игру ТАНКИ",
                 font=("Times New Roman", 30),
                 fill="yellow")


img = Image.open("StartButton.png")
img = img.resize((200, 200), Image.ANTIALIAS)
img_photo = ImageTk.PhotoImage(img)

start_button = Button(canv, image=img_photo, command=start_callback).pack(pady=50, side=BOTTOM)
help_button = Button(canv, text="Правила игры", command=help_callback).pack(pady=30, side=TOP)

root.mainloop()
