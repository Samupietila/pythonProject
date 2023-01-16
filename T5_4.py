print('Ohjelma pyytää viiden kaupungin nimeä ja tulostaa ne.')
Kaupungit = []
for i in range(5):
    Kaupungit.append(input('Anna kaupungin nimi: '))
print('Annoit seuraavat kaupungit:')
for i in Kaupungit:
    print(i)