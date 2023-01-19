Talvi = ("joulukuu", "tammikuu", "helmikuu")
Kevat = ('maaliskuu', 'huhtikuu', 'toukokuu')
Kesa = ('kesäkuu','heinäkuu','elokuu')
Syksy = ('syyskuu','lokakuu','marraskuu')
print('Tämä ohjelma kysyy käyttäjältä kuukauden ja antaa hänelle vastaukseksi vuodenajan, johon kuukausi kuuluu.')
Kuukausi = input('Anna kuukausi: ')
Kuukausi = Kuukausi.lower()
if Kuukausi in Talvi:
    print(Kuukausi, 'on talvella.')
elif Kuukausi in Kevat:
    print(Kuukausi, 'on keväällä.')
elif Kuukausi in Kesa:
    print(Kuukausi,' on kesällä.')
elif Kuukausi in Syksy:
    print(Kuukausi, 'on syksyllä.')
else:
    print('Virheellinen kuukausi.')
print('Kiitos ohjelman käytöstä.')