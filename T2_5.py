
Leivat = float(input('Anna Leiviskät: '))
Naulat = float(input('Anna Naulat: '))
Luodit = float(input('Anna Luodit: '))
Luoti = 13.3 * Luodit
Naula = 13.3 * 32 * Naulat
Leiviska = 20 * 32 * 13.3 * Leivat
Yhteensa = Naula + Leiviska + Luoti
Kilogrammat = Yhteensa / 1000
Grammat = Kilogrammat - int(Kilogrammat)
Grammat = Grammat * 1000
Grammat = round(Grammat, 2)
Kilogrammat = int(Kilogrammat)
print('Massa nykymittojen mukaan:')
print(Kilogrammat, 'kilogrammaa ja', Grammat, 'grammaa.')


