class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, thNopeus, kuljettuMatka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.thNopeus = thNopeus
        self.kuljettuMatka = kuljettuMatka

    def kiihdyta(self):
        while True:
            kiihdytys = float(input('Anna kiihtyvyyden arvo: '))
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
    uusiAuto = Auto('ABC-123', float(input('Anna auton huippunopeus: ')), 0, 0)
    kerroin = 0
    while kerroin < 3:
        uusiAuto.kiihdyta()
        uusiAuto.kulje(1)
        kerroin += 1
    print(f'Nopeutesi on nyt {uusiAuto.thNopeus} km/h')
    print(f'Olet kulkenut {uusiAuto.kuljettuMatka} kilometriä')
    uusiAuto.kiihdyta()
    uusiAuto.kulje(1)
    print(f'Nopeutesi on nyt {uusiAuto.thNopeus} km/h')
    print(f'Olet kulkenut {uusiAuto.kuljettuMatka} kilometriä')

paaohjelma()