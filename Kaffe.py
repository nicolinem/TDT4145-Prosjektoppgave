import sqlite3
from tabulate import tabulate
con = sqlite3.connect("Kaffe.db")
cursor = con.cursor()
# Bruker
# cursor.execute(
#     '''INSERT INTO Bruker (Navn, Epost, Passord) VALUES ('Per Roger', 'perroger@gmail.com', 'PerErBest123')''')
# cursor.execute(
#     '''INSERT INTO Bruker (Navn, Epost, Passord) VALUES ('Marit Lønnemo', 'maritlø@stud.ntnu.no', 'HemmeligPassord54')''')
# cursor.execute(
#     '''INSERT INTO Bruker (Navn, Epost, Passord) VALUES ('KaffeNerden', 'hans@hotmail.com', 'MoccaBønne123')''')

# # Kaffebrenneri
# cursor.execute(
#     '''INSERT INTO Kaffebrenneri VALUES ('Hallstad brenneri')''')
# cursor.execute(
#     '''INSERT INTO Kaffebrenneri VALUES ('Trondheims-brenneriet Jacobsen & Svart')''')
# cursor.execute(
#     '''INSERT INTO Kaffebrenneri VALUES ('Drammens brenneriet')''')


# # KaffeGård
# cursor.execute(
#     '''INSERT INTO Kaffegård (Navn, Land, Region, Moh) VALUES ('Nombre de Dios', 'Santa Ana', 'El Salvador', 1500)''')
# cursor.execute(
#     '''INSERT INTO Kaffegård (Navn, Land, Region, Moh) VALUES ('Alsac Farm', 'Rwanda', 'Bugesera', 360)''')
# cursor.execute(
#     '''INSERT INTO Kaffegård (Navn, Land, Region, Moh) VALUES ('Hibande', 'Colombia', 'Andina', 360)''')

# # Foredlingsmetode
# cursor.execute(
#     '''INSERT INTO Foredlingsmetode (Navn, Beskrivelse) VALUES ('Vasket', 'Vask kaffen')''')
# cursor.execute(
#     '''INSERT INTO Foredlingsmetode (Navn) VALUES ('Bærtørket Bourbon')''')
# cursor.execute(
#     '''INSERT INTO Foredlingsmetode (Navn, Beskrivelse) VALUES ('Soltørket', 'La kaffen tørke ute i sola')''')


# # Kaffeparti
# cursor.execute(
#     '''INSERT INTO Kaffeparti (InnhøstingsÅr, Kilopris, GårdsID, ForedlingID) VALUES (2021, 8, 1, 2)''')
# cursor.execute(
#     '''INSERT INTO Kaffeparti (InnhøstingsÅr, Kilopris, GårdsID, ForedlingID) VALUES (2020, 130, 2, 2)''')

# # Kaffe
# cursor.execute(
#     '''INSERT INTO Kaffe (KaffeNavn, BrenneriNavn, Beskrivelse, Brenningsgrad, BrenningDato, Kilopris, partiID) VALUES ('Vinterkaffe 2022', 'Trondheims-brenneriet Jacobsen & Svart', '«En velsmakende og kompleks kaffe for
# mørketiden', 'lys', '12-12-2021', 600, 1)''')
# cursor.execute(
#     '''INSERT INTO Kaffe (KaffeNavn, BrenneriNavn, Beskrivelse, Brenningsgrad, BrenningDato, Kilopris, partiID) VALUES ('Fin frøken', 'Hallstad brenneri', 'Rund floral kaffe med en svak bitterhet', 'middels', '12-12-2021', 240, 1)''')
# cursor.execute(
#     '''INSERT INTO Kaffe (KaffeNavn, BrenneriNavn, Beskrivelse, Brenningsgrad, BrenningDato, Kilopris, partiID) VALUES ('Lavazza', 'Trondheims brenneri', 'Rund kaffe med en svak bitterhet', 'middels', '12-12-2021', 240, 1)''')


# # Kaffesmaking
# cursor.execute(
#     '''INSERT INTO Kaffesmaking (BrukerID, Beskrivelse, Poeng, KaffeNavn, BrenneriNavn) VALUES (1, 'En meget syel kaffe med sommerlige smaker!', 9, 'Fin frøken', 'Hallstad brenneri')''')
# cursor.execute(
#     '''INSERT INTO Kaffesmaking (BrukerID, Beskrivelse, Poeng, KaffeNavn, BrenneriNavn) VALUES (2, 'Wow – en odyssé for smaksløkene: sitrusskall, melkesjokolade, aprikos!', 10, 'Vinterkaffe 2022', 'Trondheims-brenneriet Jacobsen & Svart')''')

# # Kaffebønne
# cursor.execute(
#     '''INSERT INTO Kaffebønne (Artsnavn) VALUES ('Arabica')''')
# cursor.execute(
#     '''INSERT INTO Kaffebønne (Artsnavn) VALUES ('Robusta')''')
# cursor.execute(
#     '''INSERT INTO Kaffebønne (Artsnavn) VALUES ('Liberica')''')

# # PartiBestårAv
# cursor.execute(
#     '''INSERT INTO PartiBestårAv VALUES (1, 1)''')
# cursor.execute(
#     '''INSERT INTO PartiBestårAv VALUES (2, 2)''')

# # BønneDyrketPåGård
# cursor.execute(
#     '''INSERT INTO BønneDyrketPåGård VALUES (1, 1)''')
# cursor.execute(
#     '''INSERT INTO PartiBestårAv VALUES (2, 2)''')


# cursor.execute("SELECT * FROM Bruker")
# rows = cursor.fetchall()
# print("All rows in the table bruker:")
# print(rows)

# cursor.execute("SELECT * FROM Kaffebrenneri")
# rows = cursor.fetchall()
# print("All rows in the table Kaffebrenneri:")
# print(rows)

# cursor.execute("SELECT * FROM Kaffegård")
# rows = cursor.fetchall()
# print("All rows in the table Kaffegård:")
# print(rows)

# cursor.execute("SELECT * FROM Kaffeparti")
# rows = cursor.fetchall()
# print("All rows in the table Kaffeparti:")
# print(rows)

# cursor.execute("SELECT * FROM Kaffe")
# rows = cursor.fetchall()
# print("All rows in the table Kaffe:")
# print(rows)

# con.commit()

navn = "Vinterkaffe 2022"
brenneri = " Trondheims-brenneriet Jacobsen & Svart"


def nyKaffeSmaking(kaffenavn, brennerinavn, score, beskrivelse):
    cursor.execute(
        '''INSERT INTO Kaffesmaking (BrukerID, Beskrivelse, Poeng, KaffeNavn, BrenneriNavn) VALUES (1, ?, ?, ?, ?)''', (beskrivelse, score, kaffenavn, brennerinavn))  # TODO legg til kaffebrenneri i sqlfila!
    con.commit()
    getCoffeInformation(kaffenavn, brennerinavn)


def getCoffeInformation(kaffenavn, brennerinavn):
    # finner kaffe på kaffenavn og brennerinav som bruker putter inn
    cursor.execute(
        'SELECT * FROM Kaffe WHERE KaffeNavn =? AND BrenneriNavn =?', (kaffenavn, brennerinavn))
    kaffe = cursor.fetchone()
    kaffeBeskrivelse, brentGrad, kiloprisKaffe, kaffepartiID = [
        kaffe[i] for i in (2, 3, 5, 6)]

    # finner kaffeparti fra PartiID i kaffen vi fant
    cursor.execute('SELECT * FROM Kaffeparti WHERE PartiID= ?',
                   (kaffepartiID,))
    kaffeparti = cursor.fetchone()
    innhøstingår, partiKgPris, gårdID = [kaffeparti[i] for i in (1, 2, 3)]

    cursor.execute(
        'SELECT gårdID, Navn, Region, Land, ifnull(Moh, "") FROM Kaffegård WHERE GårdID = ?', (gårdID,))
    kaffegård = cursor.fetchone()
    gårdsNavn, gårdsLand, gårdsRegion, moh = [
        kaffegård[i] for i in (1, 2, 3, 4)]

    returnString = (
        f'Kaffen er  {brentGrad}brent, kommer fra gården {gårdsNavn}')
    if(moh != ""):
        returnString += f'({moh} moh)'
    returnString += f'i  {gårdsLand}, {gårdsRegion}, har en kilopris på {kiloprisKaffe} kr '
    if (kaffeBeskrivelse != ""):
        returnString += f'og er i følge brenneriet "{kaffeBeskrivelse}" '
    returnString += f"Kaffen ble høstet i {innhøstingår} og gården fikk utbetalt {partiKgPris} USD per kg kaffe."

    print(returnString)
    print()


def getMostCoffeDrinkingUsers():
    cursor.execute('SELECT Navn, COUNT(*) AS Kaffesmakinger FROM(SELECT BrukerID, KaffeNavn, BrenneriNavn, Dato, Bruker.Navn AS Navn FROM Kaffesmaking NATURAL JOIN Bruker) WHERE strftime("%Y", Dato)="2022" GROUP BY BrukerID ORDER BY Kaffesmakinger DESC')
    kaffesmakinger = cursor.fetchall()
    print(tabulate(kaffesmakinger, headers=["Navn", "Antall", ]))


def getCoffeeWithMostValue():
    cursor.execute('SELECT  (AVG(Poeng)/Kilopris), KaffeNavn, AVG(Poeng), Kilopris FROM Kaffesmaking Kaffesmaking INNER JOIN Kaffe USING(KaffeNavn, BrenneriNavn) GROUP BY KaffeNavn, BrenneriNavn ORDER BY (avg(Poeng)/Kilopris) DESC')
    kaffer = cursor.fetchall()
    print(tabulate(kaffer, headers=[
          "Avg score", "Kaffenavn", "Avg score", "Kilopris"]))


def getCoffeeDescription(beskrivelse):
    cursor.execute('SELECT Kaffe.KaffeNavn, Kaffe.BrenneriNavn FROM Kaffesmaking INNER JOIN Kaffe ON Kaffesmaking.KaffeNavn = Kaffe.KaffeNavn WHERE Kaffesmaking.Beskrivelse LIKE ? UNION SELECT KaffeNavn, BrenneriNavn FROM Kaffe WHERE Beskrivelse LIKE ?', (str(
        '%'+beskrivelse+'%'), str('%'+beskrivelse+'%')))
    kaffer = cursor.fetchall()
    for k in kaffer:
        print(k)


def getCoffeByCountryAndProcess():
    cursor.execute('SELECT Kaffenavn, BrenneriNavn FROM (SELECT PartiID FROM Kaffeparti INNER JOIN (SELECT * FROM Kaffegård WHERE Land = "Rwanda" OR Land="Colombia") USING (GårdID) INTERSECT SELECT PartiID FROM Kaffeparti INNER JOIN (SELECT * FROM Foredlingsmetode  WHERE  NOT Navn="Vasket" ) USING (ForedlingID)) INNER JOIN Kaffe USING (PartiID)')
    kaffer = cursor.fetchall()
    for k in kaffer:
        print(k)


def main():
    print("""Velkommen til Kaffe.db! Hva ønsker du å gjøre?")
    1 | Opprette en ny kaffesmaking
    2 | Se hvem som har smakt flest unike kaffer i år
    3 | Se hvilke kaffer som gir mest for pengene
    4 | Søke etter et nøkkelord i beskrivelsen av en kaffe
    5 | Finne kaffer fra Rwanda og Columbia som ikke er vasket
    6 | Avslutte programmet\n""")
    while (True):
        inputChoice = input("Skriv inn tall: ")
        if (inputChoice == "1"):
            kaffenavn = input("Hvilken kaffe har du smakt? ")
            brennerinavn = input("Fra hvilket brenneri? ")
            score = int(input("Hvilken score vil du gi kaffen? "))
            beskrivelse = input("Hvordan vil du beskrive kaffen? ")
            nyKaffeSmaking(kaffenavn, brennerinavn, score, beskrivelse)

        if(inputChoice == "2"):
            print("Brukere som har smakt flest unike kaffer i år:")
            getMostCoffeDrinkingUsers()

        if (inputChoice == "3"):
            print("Kaffer med høyest gjennomsnittlig score kontra pris:")
            getCoffeeWithMostValue()

        if (inputChoice == "4"):
            beskrivelse = input("Skriv inn et nøkkelord å søke etter: ")
            getCoffeeDescription(beskrivelse)

        if (inputChoice == "5"):
            beskrivelse = input("Kaffer fra Rwanda og Columbia som ikke er vasket: ")
            getCoffeByCountryAndProcess()

        if (inputChoice == "6"):
            print("Avslutter programmet.\n\n")
            break

    con.close()

    # getCoffeInformation(kaffenavn, brennerinavn)
    # con.commit()


main()
