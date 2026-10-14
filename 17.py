sona = input("Sisesta sõna: ")

sona = sona.lower()

if sona == sona[::-1]:
    print("Tegemist on palindroomiga.")
else:
    print("Tegemist ei ole palindroomiga.")