lause = input("Sisesta lause: ")

taishaalikud = "aeiouõäöü"
kokku = 0

for taht in taishaalikud:
    arv = lause.lower().count(taht)
    kokku += arv
    print(f"Tähte {taht} esineb {arv} korda")

print()
print("Täishäälikuid kokku:", kokku)