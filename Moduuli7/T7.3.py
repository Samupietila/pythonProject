LK = {"LIPE":"Bolognan Guglielmo Marconi"}
Valinta = 1
while Valinta != 0:
    print('Valitse haluamasi toiminto:')
    print('1) Lisää lentokenttä.')
    print('2) Hae lentokenttää.')
    print('0) Lopeta')
    Syote = input('Anna valintasi: ')
    Valinta = int(Syote)

    if Valinta == 1:
        ICAO = input('Anna uuden lentokentän ICAO-koodi: ')
        NIMI = input('Anna uuden lentokentän nimi: ')
        LK[ICAO] = NIMI
    elif Valinta == 2:
        ICAO = input('Anna haettavan lentokentän ICAO-koodi: ')
        if ICAO in LK:
            print('Lentokenttä löytyi:')
            print(f'{LK[ICAO]}')
        else:
            print('Haku ei tuottanut yhtään tulosta, tarkista koodi.')
    elif Valinta == 0:
        print('Lopetetaan.')
        print('Kiitos ohjelman käytöstä.')
        break
    else:
        print('Tuntematon valinta, yritä uudestaan.')
