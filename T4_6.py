import random
print('Tämä ohjelma toteuttaa algoritmin π lukuarvon laskemiseksi.')
N = int(input('Anna arvottavien pisteiden määrä: '))
arvotut_pisteet = 0
n = 0
while arvotut_pisteet != N:
    X = random.uniform(-1, 1)
    Y = random.uniform(-1, 1)
    if (X ** 2) + (Y ** 2) < 1:
        n = n + 1
    else:
        n = n
    arvotut_pisteet = arvotut_pisteet + 1
Likiarvo = 4 * n / N
print('Piin likiarvo algoritmilla laskettuna on:', Likiarvo)
print('Kiitos ohjelman käytöstä.')