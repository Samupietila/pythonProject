def numeroparsija(kehote):
    lista = []
    for i in kehote:
        lasku = i % 2
        if lasku == 0:
            lista.append(i)
    return lista
def paaohjelma():
    alista = [1, 2, 3, 4, 5, 7, 8, 9, 9, 12, 23, 35, 46, 34, 75, 45]
    blista = numeroparsija(alista)
    print('Tulostettuna ensimmäisenä lista kaikilla numeroilla ja toisena listan parilliset luvut.')
    print(alista)
    print(blista)

paaohjelma()