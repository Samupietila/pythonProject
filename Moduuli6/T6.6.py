import math
def muuntaja(kehote1, kehote2):
    pa = (kehote1/2)**2*math.pi
    pa = pa / 1000
    yhinta = kehote2 / pa
    return yhinta
def paaohjelma():
    print('Tämä ohjelma kysyy käyttäjältä kahden pizzan halkaisijan senttimetreinä ja niiden hinnat.\nLopussa se ilmoittaa kummassa pizzassa on parempi vastine rahalle.')
    Pizza1 = muuntaja(float(input('Anna ensimmäisen pizzan halkaisija senttimetreinä: ')), float(input('Anna ensimmäisen pizzan hinta: ')))
    Pizza2 = muuntaja(float(input('Anna toisen pizzan halkaisija senttimetreinä: ')), float(input('Anna toisen pizzan hinta: ')))
    if Pizza1 < Pizza2:
        print('Ensimmäisessä pizzassa on enemmän rahalle vastinetta.')
    else:
        print('Toisessa pizzassa on enemmä rahalle vastinetta.')
    print('Kiitos ohjelman käytöstä.')
paaohjelma()