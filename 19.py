taishaalikud = "aeiouõäöü"
kaashaalikud = "bcdfghjklmnpqrsšzžtvwx y".replace(" ", "")

taht = input("Sisesta tähemärk: ")

if len(taht) != 1:
    print("Viga! Sisesta täpselt üks tähemärk.")
elif taht.lower() in taishaalikud:
    print("Tegemist on täishäälikuga.")
elif taht.lower() in kaashaalikud:
    print("Tegemist on kaashäälikuga.")
elif taht.isdigit():
    print("Tegemist on numbriga.")
else:
    print("Tegemist on muu sümboliga.")