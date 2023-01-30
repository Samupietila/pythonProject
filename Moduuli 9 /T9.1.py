class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, thNopeus, kuljettuMatka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.thNopeus = thNopeus
        self.kuljettuMatka = kuljettuMatka

def paaohjelma():
    uusiAuto = Auto(input('Anna auton rekisteritunnus: '), input('Anna auton huippunopeus: '), 0, 0)
    print(f'Auton ominaisuudet:\nRekisteritunnus: {uusiAuto.rekisteritunnus}\nHuippunopeus: {uusiAuto.huippunopeus}\nTämänhetkinen nopeus: {uusiAuto.thNopeus}\nKuljettu matka: {uusiAuto.kuljettuMatka}')
    return None
paaohjelma()