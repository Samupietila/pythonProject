Kala = float(input('Anna Kuhan mitta senttimetreinä: '))
if Kala < 37:
    print('Kala alamittainen, laske kala takaisin järveen.')
    Tarvittava_pituus = 37 - Kala
    Tarvittava_pituus = int(Tarvittava_pituus)
    print('Kalan pituudesta jäi', Tarvittava_pituus, 'senttimetriä.' )
else:
    print('Kalan pituus on riittävä.')

print('Kiitos ohjelman käytöstä.')