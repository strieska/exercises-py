import tkinter

c = tkinter.Canvas(height=600, width=800)
c.pack()

entry = tkinter.Entry()
entry.pack()

def draw_person(x, y, color):
    c.create_oval(x-20, y-40, x+20, y)
    c.create_rectangle(x-20, y, x+20, y+40, fill=color)
    c.create_text(x, y+50, text=entry.get())

def draw_green(event):
    if event.num == 1:
       draw_person(event.x, event.y, "green")
    else:
        draw_person(event.x, event.y, "yellow")

c.bind("<Button>", draw_green)
c.mainloop()