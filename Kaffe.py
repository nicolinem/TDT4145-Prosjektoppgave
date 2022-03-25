import sqlite3
from tabulate import tabulate
con = sqlite3.connect("Kaffe.db")
cursor = con.cursor()


navn = "Vinterkaffe 2022"
brenneri = " Trondheims-brenneriet Jacobsen & Svart"

# Setter inn en ny rad i Kaffesmaking og printer ut informasjonen om den oppgidde kaffen


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

    # Finner kaffeparti og foredlingsmetode fra PartiID i kaffen vi fant
    cursor.execute('SELECT Foredlingsmetode.Navn, InnhøstingsÅr, Kilopris, GårdID FROM Foredlingsmetode inner join (SELECT * FROM Kaffeparti WHERE PartiID= ?) using(ForedlingID)',
                   (kaffepartiID,))
    kaffeparti = cursor.fetchone()
    # for k in kaffeparti:
    #     print(k)
    foredlingNavn, innhøstingår, partiKgPris, gårdID = [
        kaffeparti[i] for i in (0, 1, 2, 3)]

    cursor.execute('SELECT Artsnavn FROM Kaffebønne INNER JOIN (SELECT * FROM PartiBestårAv WHERE PartiID = ?) USING (BønneID)',
                   (kaffepartiID,))
    kaffebønner = cursor.fetchall()

    # Finner kaffegården fra GårdID vi fikk fra partiet
    cursor.execute(
        'SELECT gårdID, Navn, Region, Land, ifnull(Moh, "") FROM Kaffegård WHERE GårdID = ?', (gårdID,))
    kaffegård = cursor.fetchone()

    gårdsNavn, gårdsLand, gårdsRegion, moh = [
        kaffegård[i] for i in (1, 2, 3, 4)]

    returnString = (
        f'Kaffen er  {brentGrad}brent, {foredlingNavn} {kaffebønner} kommer fra gården {gårdsNavn}')
    if(moh != ""):
        returnString += f'({moh} moh)'
    returnString += f'i  {gårdsLand}, {gårdsRegion}, har en kilopris på {kiloprisKaffe} kr '
    if (kaffeBeskrivelse != ""):
        returnString += f'og er i følge brenneriet "{kaffeBeskrivelse}" '
    returnString += f"Kaffen ble høstet i {innhøstingår} og gården fikk utbetalt {partiKgPris} USD per kg kaffe."
    print()
    print(returnString)


def getMostCoffeDrinkingUsers():
    cursor.execute('SELECT Navn, COUNT(*) AS Kaffesmakinger FROM(SELECT BrukerID, KaffeNavn, BrenneriNavn, Dato, Bruker.Navn AS Navn FROM Kaffesmaking INNER JOIN Bruker USING (BrukerID) GROUP BY BrukerID, KaffeNavn, BrenneriNavn) WHERE strftime("%Y", Dato)="2022" GROUP BY BrukerID ORDER BY Kaffesmakinger DESC')
    kaffesmakinger = cursor.fetchall()
    print()
    print(tabulate(kaffesmakinger, headers=["Navn", "Antall", ]))


def getCoffeeWithMostValue():
    cursor.execute('SELECT KaffeNavn, Brennerinavn, AVG(Poeng), Kilopris FROM Kaffesmaking Kaffesmaking INNER JOIN Kaffe USING(KaffeNavn, BrenneriNavn) GROUP BY KaffeNavn, BrenneriNavn ORDER BY (avg(Poeng)/Kilopris) DESC')
    kaffer = cursor.fetchall()
    print()
    print(tabulate(kaffer, headers=["Kaffenavn",
          "Brenneri", "Avg score", "Kilopris"]))


def getCoffeeDescription(beskrivelse):
    cursor.execute('SELECT Kaffe.KaffeNavn, Kaffe.BrenneriNavn FROM Kaffesmaking INNER JOIN Kaffe USING (KaffeNavn, BrenneriNavn) WHERE Kaffesmaking.Beskrivelse LIKE ? UNION SELECT KaffeNavn, BrenneriNavn FROM Kaffe WHERE Beskrivelse LIKE ?', (str(
        '%'+beskrivelse+'%'), str('%'+beskrivelse+'%')))
    kaffer = cursor.fetchall()
    print()
    print(tabulate(kaffer, headers=["Kaffenavn", "Brenneri"]))


def getCoffeByCountryAndProcess():
    cursor.execute('SELECT Kaffenavn, BrenneriNavn FROM (SELECT PartiID FROM Kaffeparti INNER JOIN (SELECT * FROM Kaffegård WHERE Land = "Rwanda" OR Land="Colombia") USING (GårdID) INTERSECT SELECT PartiID FROM Kaffeparti INNER JOIN (SELECT * FROM Foredlingsmetode  WHERE  NOT Navn="Vasket" ) USING (ForedlingID)) INNER JOIN Kaffe USING (PartiID)')
    kaffer = cursor.fetchall()
    print()
    print(tabulate(kaffer, headers=["Kaffenavn", "Brenneri"]))


def main():
    print("""Velkommen til Kaffe.db! Hva ønsker du å gjøre?")
    1 | Opprette en ny kaffesmaking og få informasjon om denne kaffen
    2 | Se hvem som har smakt flest unike kaffer i år
    3 | Se hvilke kaffer som gir mest for pengene
    4 | Søke etter et nøkkelord i beskrivelsen av en kaffe
    5 | Finne kaffer fra Rwanda og Columbia som ikke er vasket
    6 | Avslutte programmet\n""")
    while (True):
        print()
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
            print("Kaffer fra Rwanda og Columbia som ikke er vasket: ")
            getCoffeByCountryAndProcess()

        if (inputChoice == "6"):
            print("Avslutter programmet.\n\n")
            break
        print()

    con.close()

    # getCoffeInformation(kaffenavn, brennerinavn)
    # con.commit()


main()
