import tkinter as tk

aken = tk.Tk()
aken.title("Minu kujundid")

tahvel = tk.Canvas(aken, width=600, height=400, bg="white")
tahvel.pack()
# Punane ristkülik
tahvel.create_rectangle(50, 50, 200, 130, fill="red")
# Sinine ring
tahvel.create_oval(300, 40, 400, 140, fill="blue")
# Roheline joon
tahvel.create_line(50, 200, 250, 200, fill="green", width=4)
# Kollane ovaal
tahvel.create_oval(300, 180, 500, 270, fill="yellow")
# Tekst
tahvel.create_text(300, 330, text="Minu kujundid", font=("Arial", 20))

aken.mainloop()