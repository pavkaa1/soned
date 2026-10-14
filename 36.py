import tkinter as tk

aken = tk.Tk()
aken.title("Ringide muster")

tahvel = tk.Canvas(aken, width=500, height=500, bg="white")
tahvel.pack()

ringide_arv = 20  #Peaks muuta seda arve, et muuta ringide hulka

for i in range(ringide_arv):
    suurus = 10 + i * 2

    x = 250 - suurus
    y = 250 - suurus
    x2 = 250 + suurus
    y2 = 250 + suurus

    if i % 2 == 0:
        varv = "red"
    else:
        varv = "blue"

    tahvel.create_oval(x, y, x2, y2, outline=varv, width=2)

aken.mainloop()