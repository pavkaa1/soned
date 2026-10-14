import tkinter as tk

laius = 600
korgus = 400
taust = "white"

aken = tk.Tk()
aken.title("Minu esimene graafika")

tahvel = tk.Canvas(
    aken,
    width=laius,
    height=korgus,
    bg=taust
)

tahvel.pack()

aken.mainloop()