print('Tämä ohjelma kysyy käyttäjältä hyttiluokan ja antaa siitä kuvauksen.')
Hyttiluokka = input('Anna hyttiluokka: ')
Hyttiluokka = Hyttiluokka.upper()
if Hyttiluokka == 'LUX':
    print('LUX on parvekkeellinen hytti yläkannella.')
elif Hyttiluokka == 'A':
    print('A on ikkunallinen hytti autokannen yläpuolella.')
elif Hyttiluokka == 'B':
    print('B on ikkunaton hytti autokannen yläpuolella.')
elif Hyttiluokka == 'C':
    print('C on ikkunaton hytti autokannen alapuolella')
else:
    print('Virheellinen hyttiluokka.')
print('Kiitos ohjelman käytöstä.')