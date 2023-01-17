print('Tämä ohjelma kysyy lukuja ja kertoo lopuksi niistä suurimman.')
print('Tyhjä vastaus lopettaa ohjelman.')
Luku = 0
Isoin = 0
while True:
    Luku = input('Anna luku: ')
    if Luku == '':
        print('Isoin annettu luku oli', Isoin)
        break
    else:
        Luku = float(Luku)
        if Luku > Isoin:
            Isoin = round(Luku)
        else:
            Isoin = Isoin
print('Kiitos ohjelman käytöstä.')
