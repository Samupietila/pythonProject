Luvut = []

Luku = input("Anna ensimmäinen luku tai lopeta painamalla Enter: ")
while Luku!="":
    Luku = int(Luku)
    Luvut.append(Luku)
    Luku = input("Anna seuraava luku tai lopeta painamalla Enter: ")
Luvut.sort(reverse=True)
Luvut = Luvut[:5]
for i in Luvut:
    print(i)
