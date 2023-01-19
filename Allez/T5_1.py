import random
print('Ohjelma heittää kaikkia arpakuutioita kerran ja tulostaa niiden summan.')
Arpakuutiot = int(input('Anna arpakuutioiden määrä: '))
Luvut = []
for i in range(Arpakuutiot):
    Luvut.append(random.randint(1,6))
Luvut = sum(Luvut)
print('Arpakuutiodien summa on:', Luvut)