Luku = int(input('Anna jokin kokonaisluku ja ohjelma ilmoittaa onko kyseessä alkuluku: '))
Alkuluku = True
for i in range(2,Luku):
    if Luku % i == 0:
        Alkuluku = False
        break
if Alkuluku == True:
    print('Luku on alkuluku.')
else:
    print('Luku ei ole alkuluku.')