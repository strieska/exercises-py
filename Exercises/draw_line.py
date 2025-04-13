from tkinter import Canvas

def set_points(event):
    global points
    points.append(event.x)
    points.append(event.y)
    # this redraws all line again which is not
    # optimal, there is room for improvements
    c.create_line(points)

def clear(event):
    global points
    c.delete("all")
    points = []

c = Canvas(height=600, width=800)
c.pack()
points = []

c.bind("<Button-1>", set_points)
c.bind_all("a", clear)
c.mainloop()