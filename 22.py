epost = input("Sisesta e-post: ")

if (
    epost.count("@") == 1
    and epost.index("@") > 0
    and "." in epost.split("@")[1]
    and not epost.split("@")[1].startswith(".")
    and not epost.split("@")[1].endswith(".")
    and " " not in epost
):
    print("Aadressi kuju on sobiv.")
else:
    print("Aadressi kuju ei ole sobiv.")