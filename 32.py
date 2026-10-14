import tkinter as tk

aken = tk.Tk()
aken.title("Koordinaatide harjutus")

tahvel = tk.Canvas(aken, width=500, height=500, bg="white")
tahvel.pack()

for x in range(0, 501, 50):
    tahvel.create_line(x, 0, x, 500, fill="gray")
    tahvel.create_text(x + 10, 10, text=str(x), fill="black")

for y in range(0, 501, 50):
    tahvel.create_line(0, y, 500, y, fill="gray")
    tahvel.create_text(25, y + 10, text=str(y), fill="black")