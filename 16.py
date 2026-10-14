kasutajanimi = input("Kasutajanimi: ")

if not (5 <= len(kasutajanimi) <= 15):
    print("Viga: kasutajanimi peab olema 5–15 tähemärki pikk.")
elif not kasutajanimi.isalnum() or not kasutajanimi.isascii():
    print("Viga: kasutada tohib ainult ladina tähti ja numbreid.")
elif not kasutajanimi[0].isalpha():
    print("Viga: kasutajanimi peab algama tähega.")
else:
    print("Kasutajanimi sobib.")