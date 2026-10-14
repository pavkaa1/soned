tekst = input("Sisesta tekst: ")

taishaalikud = "aeiouõäöü"

kokku = len(tekst)
ilma_tuhikuteta = len(tekst.replace(" ", ""))
sonad = len(tekst.split())

taishaalikute_arv = 0
numbrite_arv = 0

for taht in tekst.lower():
    if taht in taishaalikud:
        taishaalikute_arv += 1

for taht in tekst:
    if taht.isdigit():
        numbrite_arv += 1

print()
print("Tähemärke kokku:", kokku)
print("Tähemärke ilma tühikuteta:", ilma_tuhikuteta)
print("Sõnu:", sonad)
print("Täishäälikuid:", taishaalikute_arv)
print("Numbreid:", numbrite_arv)