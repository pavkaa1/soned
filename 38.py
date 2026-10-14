parool = input("Sisesta parool: ")

punktid = 0
puudused = []

if len(parool) >= 8:
    punktid += 1
else:
    puudused.append("Parool peab sisaldama vähemalt 8 tähemärki.")

if any(taht.isupper() for taht in parool):
    punktid += 1
else:
    puudused.append("Puudub suurtäht.")

if any(taht.islower() for taht in parool):
    punktid += 1
else:
    puudused.append("Puudub väiketäht.")

if any(taht.isdigit() for taht in parool):
    punktid += 1
else:
    puudused.append("Puudub number.")

if any(not taht.isalnum() for taht in parool):
    punktid += 1
else:
    puudused.append("Puudub erimärk.")

print(f"\nTulemus: {punktid}/5")

if punktid <= 2:
    print("Hinnang: Nõrk parool")
elif punktid <= 4:
    print("Hinnang: Keskmine parool")
else:
    print("Hinnang: Kõik nõuded täidetud")

for puudus in puudused:
    print(puudus)