Sukupuoli = input('Ilmoita sukupuolesi (M/N): ')
Mies = None
Nainen = None
if Sukupuoli == 'M':
    Sukupuoli = Mies
    Hemoglobiini = int(input('Anna hemoglobiiniarvosi kokonaislukuna: '))
elif Sukupuoli == 'N':
    Sukupuoli = Nainen
    Hemoglobiini = int(input('Anna hemoglobiiniarvosi kokonaislukuna: '))
else:
    print('Tuntematon valinta.')
if Sukupuoli == Mies:
    if Hemoglobiini > 175:
        print('Hemoglobiiniarvosi on korkea.')
    elif Hemoglobiini < 117:
        print('Hemoglobiiniarvosi on alhainen.')
    else:
        print('Hemoglobiiniarvosi on normaali.')
elif Sukupuoli == Nainen:
    if Hemoglobiini > 195:
        print('Hemoglobiiniarvosi on korkea.')
    elif Hemoglobiini < 134:
        print('Hemoglobiiniarvosi on alhainen.')
    else:
        print('Hemoglobiiniarvosi on normaali.')
print('Kiitos ohjelman käytöstä.')