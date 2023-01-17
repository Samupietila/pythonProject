print('Tämä ohjelma kysyy lukuja ja kertoo lopuksi niistä suurimman ja pienimmän.')
print('Tyhjä vastaus lopettaa ohjelman.')
Luku = 0
Isoin = 0
Pienin = 9999999999999999999999999999999999
while True:
    Luku = input('Anna luku: ')
    if Luku == '':
        print('Isoin annettu luku oli', Isoin, 'ja pienin oli', Pienin)
        break
    else:
        Luku = float(Luku)
        if Luku > Isoin:
            Isoin = round(Luku)
        else:
            Isoin = Isoin
    if Luku < Pienin:
        Pienin = round(Luku)
    else:
        Pienin = Pienin
print('Kiitos ohjelman käytöstä.')
