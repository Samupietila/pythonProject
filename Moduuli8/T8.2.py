import mysql.connector
yhteys = mysql.connector.connect(host='127.0.0.1', port= 3306, database= 'lentopeli', user = 'Pythonuser', password = 'SaLaSaNa', autocommit = True)
def haeMaakoodi(kehote):
    sql = "SELECT type, count(*) from airport"
    sql += " WHERE iso_country = '" + kehote + "' group by type;"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0:
        for rivi in tulos:
            print(f"Lentokentän tyyppi on '{rivi[0]}' ja niitä oli yhteensä '{rivi[1]}'.")
print('Tämä ohjelma pyytää käyttäjältä maan maakoodin, ja tulostaa sen maan lentokenttä tyypit ja niiden lukumäärät.')
Maakoodi = input('Anna haluamasi maan maakoodi: ')
haeMaakoodi(Maakoodi)