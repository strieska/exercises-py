# f = open("qwertz.txt")
# file = f.read()
import  tkinter

c = tkinter.Canvas()
c.pack()

vstupne_pole = tkinter.Entry()
vstupne_pole.pack()
file = vstupne_pole.get()
file.replace("z","@")
file.replace("y","z")
file.replace("@","y")
# f.close()
# g = open("qwerty.txt")
# g.write(file)

def print_something():
    global vstupne_pole
    t = vstupne_pole.get()
    t = t.replace("z","@")
    t = t.replace("y","z")
    t = t.replace("@","y")
    c.create_text(100,10, text=t)

b1 = tkinter.Button(text = "Something", command=print_something)
b1.pack()

c.mainloop()