print('Tämä ohjelma muuntaa annetut tuumat senttimetreiksi.')
print('Negatiivinen luku lopettaa ohjelman.')
while True:
    Luku = float(input('Anna senttimetreiksi muunnettavat tuumat: '))
    if Luku > 0:
        Luku = Luku * 2.54
        print('Annettu määrä tuumia on', round(Luku, 1), 'senttimetriä.')
    else:
        print('Annoit negatiivisen luvun, ohjelma päättyy.')
        break