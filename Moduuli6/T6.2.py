import random
print('Tämä ohjelma heittää noppaa niin kauan, kunnes silmäluvuksi tulee nopan suurin silmäluku.')
tahkot = int(input('Anna arpakuution suurin silmäluku: '))
def arpakuutio(tahkot):
    kehote = random.randint(1,tahkot)
    print('Heiton silmäluku on', kehote)
    return kehote
def paaohjelma():
    while True:
        silmaluku = arpakuutio(tahkot)
        if silmaluku == tahkot:
            print('Silmäluku oli isoin mahdollinen! Onnea!')
            break
        else:
            print('Silmäluku ei ollut tarpeeksi iso, yritetään uudestaan.')


paaohjelma()