import mysql.connector
yhteys = mysql.connector.connect(host='127.0.0.1', port= 3306, database= 'lentopeli', user = 'Pythonuser', password = 'SaLaSaNa', autocommit = True)
def haeLentoasema(ICAO):
    sql = "SELECT name, municipality from airport "
    sql += "WHERE ident='" + ICAO + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0:
        for rivi in tulos:
            print(f"Lentokentän nimi on '{rivi[0]}' ja sen sijaintikunta on '{rivi[1]}'.")

ICAO = input('Anna etsimäsi lentokentän ICAO-koodi: ')
haeLentoasema(ICAO)