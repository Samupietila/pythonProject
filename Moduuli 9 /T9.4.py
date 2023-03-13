import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, thNopeus, kuljettuMatka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.thNopeus = thNopeus
        self.kuljettuMatka = kuljettuMatka

    def kiihdyta(self):
        while True:
            muutos = random.randint(-10,15)
            kiihdytys = muutos
            if self.thNopeus + kiihdytys < 0:
                self.thNopeus = 0
                break
            elif self.thNopeus + kiihdytys > self.huippunopeus:
                self.thNopeus = self.huippunopeus
                break
            else:
                self.thNopeus = self.thNopeus + kiihdytys
                break
        return self.thNopeus

    def kulje(self, tunnit):
        pituus = self.thNopeus * tunnit
        if pituus < 0:
            pituus = 0
        self.kuljettuMatka += pituus



def paaohjelma():
    Autot = []
    for i in range(11):
        i = Auto('ABC-'+str(i), random.randint(100,200), 0, 0)
        Autot.append(i)
    while i.kuljettuMatka <= 10000:
        for i in Autot:
            i.kiihdyta()
            i.kulje(1)
            if i.kuljettuMatka >= 10000:
                print(f'{i.rekisteritunnus}  kulki ensimmäisenä 10000km.')
                print(f'Matkaa kertyi yhteensä: {i.kuljettuMatka}km')
                break
    print()
    print('Tässä kaikkien autojen tulokset:')
    for i in Autot:
        print(f'{i.rekisteritunnus} ajoi yhteensä {i.kuljettuMatka} kilometriä.')
        print(f'Auton huippunopeus on {i.huippunopeus}km/h,')
        print(f'nopeus kisan päättyessä oli {i.thNopeus}km/h.')
        print()


paaohjelma()