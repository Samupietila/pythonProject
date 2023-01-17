def Muuntaja(kehote):
    kehote = kehote / 3.785
    return kehote
def paaohjelma():
    print('Tämä ohjelma muuttaa annetun nestegallonamäärän litroiksi.')
    while True:
        lm = float(input('Anna bensiinin määrä nestegallonoina (negatiivinen arvo lopettaa): '))
        if lm > 0:
            lm = Muuntaja(lm)
            lm = round(lm, 3)
            print('Bensiin määrä litroissa on', lm)
        else:
            print('Kiitos ohjelman käytöstä.')
            break

paaohjelma()