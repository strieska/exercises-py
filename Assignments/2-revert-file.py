import tkinter
c=tkinter.Canvas()
c.pack()
def otocenie(words):
    reversed_words = []
    for w in words:
        reversed_words.append(w[::-1])
    return " ".join(reversed_words)

f = open("2-revert-file.txt")
file_content = f.read()
of = open("2-output.txt", "w+")
new_text = otocenie(file_content.split(" "))
of.write(new_text)
print(file_content)

c.create_text(100, 100, text=new_text)
c.mainloop()