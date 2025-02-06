import random
import tkinter
c=tkinter.Canvas(height=600, width=1200)
c.pack()

ball_x = 200
ball_y = 10

pad_x = 200
pad_y = 400

# Nakresli loptu
def draw_ball(x, y):
    c.create_oval(x, y, x + 10, y + 10, fill="red", tags = "ball")

# Nakresli palicu
def draw_pad(x, y):
    c.create_line(x, y, x+50, y, fill='blue', width=5, tags="pad")

# Pohybuje palicu podla polohy mysi
# Novu poziciu vzdy zapise do globalnej premennej
def move_pad(event):
    global pad_x, pad_y
    pad_x = event.x
    c.delete("pad")
    draw_pad(event.x, pad_y)

# Pohybuje loptu smerom dole o 10px
# Ked sa dostane na uroven palice, overuje, ci sa nachadza na jej suradniciach.
# Ak ano, prestane padat.
# Ak cyklus neukoncila kolizia s palicou, na 550px sa resetne a zacne padat znovu
def move_ball():
    global ball_y, ball_x, pad_x, pad_y
    ball_y += 10
    c.delete("ball")
    if 410 > ball_y >= 400:
        if pad_x < ball_x < pad_x + 50:
            return
    if ball_y > 550:
        ball_y = 10
        ball_x = random.randint(100, 800)
    draw_ball(ball_x, ball_y)
    c.after(100, move_ball)

# Spusti padanie lopty
move_ball()
# Prekresluje palicu
c.bind("<Motion>", move_pad)
c.mainloop()