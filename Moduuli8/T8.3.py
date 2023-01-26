from geopy import distance
import mysql.connector
yhteys = mysql.connector.connect(host='127.0.0.1', port= 3306, database= 'lentopeli', user = 'Pythonuser', password = 'SaLaSaNa', autocommit = True)
def haeLentoasema():
    kehote = input('Anna ICAO-koodi: ')
    sql = "SELECT latitude_deg, longitude_deg from airport"
    sql += " WHERE ident='" + kehote + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    tulos = tulos[0]
    return tulos
print('Tämä ohjelma pyytää käyttäjältä kahden lentokentän ICAO-koodit ja tulostaa niiden välimatkan kilometreinä.')
Lentokentta1 = haeLentoasema()
Lentokentta2 = haeLentoasema()
Pituus = round(distance.distance(Lentokentta1, Lentokentta2).km, 1)
print('Lentokenttien välimatka on', Pituus, 'kilometriä.')