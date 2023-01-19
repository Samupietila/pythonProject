print('Tämä ohjelma kysyy käyttäjältä vuosiluvun ja kertoo onko kyseessä karkausvuosi.')
Vuosiluku = int(input('Anna vuosiluku: '))
if Vuosiluku % 4 == 0:
    if Vuosiluku % 100 == 0:
        if Vuosiluku % 400 == 0:
            print('Vuosi on karkausvuosi.')
        else:
            print('Vuosi ei ole karkausvuosi.')
    else:
        print('Vuosi on karkausvuosi.')
else:
    print('Vuosi ei ole karkausvuosi.')

