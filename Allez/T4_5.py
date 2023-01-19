print('Tämä ohjelma kysyy käyttäjältä käyttäjätunnuksen ja salasanan.')
Kayttajanimi = 'python'
Salasana = 'rules'
Yritykset = 0
while Yritykset < 5:
    Annettu_kn = input('Anna käyttäjänimi: ')
    Annettu_ss = input('Anna salasana: ')

    if Annettu_kn == Kayttajanimi and Annettu_ss == Salasana:
        print('Tervetuloa!')
        break
    else:
        print('Pääsy evätty.')
    Yritykset = Yritykset + 1