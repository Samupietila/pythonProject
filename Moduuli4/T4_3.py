print('Tämä ohjelma kysyy lukuja ja kertoo lopuksi niistä suurimman ja pienimmän.')
print('Tyhjä vastaus lopettaa ohjelman.')
Luku = 0
Isoin = 0
Pienin = None
while True:
    Luku = input('Anna luku: ')
    if Pienin == None:
        Pienin = float(Luku)
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
        Pienin = int(Luku)
    else:
        Pienin = Pienin
print('Kiitos ohjelman käytöstä.')
