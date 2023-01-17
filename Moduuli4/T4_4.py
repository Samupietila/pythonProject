import random
print('Tämä ohjelma arpoo numeron 1-10 ja käyttäjän täytyy yrittää arvata mikä numero on kyseessä.')
Luku = random.randint(1, 10)
print('Numero on arvottu.')
while True:
    Arvaus = int(input('Arvaa arvottu kokonaisluku: '))
    if Arvaus == Luku:
        print('Onnea! Arvasit numeron oikein!')
        print('Oikea vastaus oli:', Luku)
        break
    else:
        print('Arvasit väärin. Yritä uudestaan!')
print('Kiitos ohjelman käytöstä')