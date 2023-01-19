Nimet = set()
while True:
    Nimi = input('Anna nimi, Enter lopettaa: ')
    if Nimi == '':
        break
    if Nimi in Nimet:
        print('Aiemmin syötetty nimi.')

    else:
        print('Uusi nimi.')
        Nimet.add(Nimi)
print('Ohjelmaan on syötetty seuraavat nimet:')
for i in Nimet:
    print(i)