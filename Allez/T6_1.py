import random
print('Tämä ohjelma heittää noppaa niin kauan, kunnes silmäluvuksi tulee 6.')
def arpakuutio():
    kehote = random.randint(1,6)
    print('Heiton silmäluku on', kehote)
    return kehote
def paaohjelma():
    while True:
        silmaluku = arpakuutio()
        if silmaluku == 6:
            print('Silmäluku oli 6! Onnea!')
            break
        else:
            print('Silmäluku ei ollut tarpeeksi iso, yritetään uudestaan.')


paaohjelma()
