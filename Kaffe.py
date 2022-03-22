import sqlite3
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
    kaffe = cursor.fetch()
    kaffeBeskrivelse = kaffe[2]
    brentGrad = kaffe[3]
    kiloprisKaffe = kaffe[5]
    kaffepartiID = kaffe[6]

    # finner kaffeparti fra PartiID i kaffen vi fant
    cursor.execute('SELECT * FROM Kaffeparti WHERE PartiID= ?',
                   (kaffepartiID,))
    kaffeparti = cursor.fetch()
    innhøstingår = kaffeparti[1]
    partiKgPris = kaffeparti[2]
    gårdID = kaffeparti[3]

    cursor.execute(
        'SELECT gårdID, Navn, Region, Land, ifnull(Moh, "") FROM Kaffegård WHERE GårdID = ?', (gårdID,))
    kaffegård = cursor.fetch()
    gårdsNavn = kaffegård[1]
    gårdsLand = kaffegård[2]
    gårdsRegion = kaffegård[3]
    moh = kaffegård[4]

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
    # print(kaffeparti)
    # print(kaffe)
    # print(f'Kaffen er  {brentGrad}brent, kommer fra gården {gårdsNavn} ({moh} moh) i  {gårdsLand}, {gårdsRegion}, har en kilopris på {kiloprisKaffe} kr og er i følge brenneriet "{kaffeBeskrivelse}"')
    # print(
    #     f"Kaffen ble høstet i {innhøstingår} og gården fikk utbetalt {partiKgPris} USD per kg kaffe.")


def getCoffeeDescription(beskrivelse):
    cursor.execute('Select Kaffe.KaffeNavn, BrenneriNavn from Kaffesmaking inner join Kaffe on Kaffesmaking.KaffeNavn = Kaffe.KaffeNavn where Kaffesmaking.Beskrivelse like %?% UNION select KaffeNavn, BrenneriNavn from Kaffe where Beskrivelse like %?%', (beskrivelse,))


def main():
    while (True):
        print("Hei! Hva ønsker du å gjøre?")
        print('"1" for å legge til en ny kaffesmaking')
        print('"2" for å søke etter en kaffe')
        print('3 for å fe en ')
        print('"4", for å søke etter nøkkelord i en beskrivelse av en kaffe')
        inputChoice = input("Hva velger du? ")
        if (inputChoice == "1"):
            kaffenavn = input("Hvilken kaffe har du smakt? ")
            brennerinavn = input("Fra hvilket brenneri? ")
            score = int(input("Hvilken score vil du gi kaffen? "))
            beskrivelse = input("Hvordan vil du beskrive kaffen? ")
            nyKaffeSmaking(kaffenavn, brennerinavn, score, beskrivelse)
        if (inputChoice == "4"):
            beskrivelse = input("Skriv inn et nøkkelord å søke etter")
            getCoffeeDescription(beskrivelse)

    con.close()

    # getCoffeInformation(kaffenavn, brennerinavn)
    # con.commit()


main()
