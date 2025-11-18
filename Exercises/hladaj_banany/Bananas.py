import math
import random
import tkinter

c = tkinter.Canvas(height=600, width=800)
c.pack()

#--------- pociatocne suradnice opice a bananu
m_x = 500
m_y = 300
b_x = random.randint(300, 700)
b_y = random.randint(100, 400)
# inicilizacia obrazkov
scientist = tkinter.PhotoImage(file="vysk0.png")
monkey = tkinter.PhotoImage(file="opica.png")
banana = tkinter.PhotoImage(file="banany.png")
c.create_image(50, 550, image = scientist, anchor="sw", tags = "sc")
c.create_image(m_x, m_y, image= monkey, anchor="c", tags = "monkey")
# obrazok pre banany sa nevykresluje, je skryty


def move_monkey(event):
    global m_x, m_y, scientist, banana
    old_dist = measure_distance(m_x, m_y)
    # kontrola stlaenej klavesy
    movement = event.keysym
    if movement == "Left":
        m_x -=30
    elif movement == "Right":
        m_x +=30
    elif movement == "Up":
        m_y -=30
    elif movement == "Down":
        m_y +=30
    # posun a prekreslenie opice
    c.delete("monkey")
    c.create_image(m_x, m_y, image= monkey, anchor="c", tags = "monkey")
    new_dist = measure_distance(m_x, m_y)
    # feedback na pohyb
    if new_dist < old_dist:
        scientist = tkinter.PhotoImage(file="vysk3.png")
    else:
        scientist = tkinter.PhotoImage(file="vysk1.png")
    if new_dist < 50:
        # pri uspesnom najdeni sa nakresli banan a pochvala
        scientist = tkinter.PhotoImage(file="vysk4.png")
        c.create_image(b_x, b_y, image=banana, anchor="c")
    c.delete("sc")
    c.create_image(50, 550, image=scientist, anchor="sw", tags = "sc")

def measure_distance(mx, my):
    global b_x, b_y
    return math.sqrt( (mx - b_x)**2 + (my - b_y)**2 )

c.bind_all("<Key>", move_monkey)
c.mainloop()