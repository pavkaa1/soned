import tkinter as tk

aken = tk.Tk()
aken.title("Värvilised ruudud")

tahvel = tk.Canvas(aken, width=490, height=60, bg="white")
tahvel.pack()

for i in range(10):
    x = i * 50

    if i % 2 == 0:
        varv = "red"
    else:
        varv = "blue"

    tahvel.create_rectangle(x, 10, x + 40, 50, fill=varv)

aken.mainloop()