import tkinter
import random

c=tkinter.Canvas(height=250, width=800)
c.pack()

def draw_circle(center):
    offset = random.randint(50,100)
    color = random.choice(["red", "green", "blue", "yellow", "orange"])
    c.create_oval(center-offset, 120-offset, center+offset, 120+offset, outline=color, width=4)

def generate_circles():
    for i in range(20):
        draw_circle(100 + i * 30)

generate_circles()
c.mainloop()
