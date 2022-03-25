import sqlite3
from tabulate import tabulate
con = sqlite3.connect("Kaffe.db")
cursor = con.cursor()
# Bruker
cursor.execute(
    '''INSERT INTO Bruker (Navn, Epost, Passord) VALUES ('Per Roger', 'perroger@gmail.com', 'PerErBest123')''')
cursor.execute(
    '''INSERT INTO Bruker (Navn, Epost, Passord) VALUES ('Marit Lønnemo', 'maritlø@stud.ntnu.no', 'HemmeligPassord54')''')
cursor.execute(
    '''INSERT INTO Bruker (Navn, Epost, Passord) VALUES ('KaffeNerden', 'hans@hotmail.com', 'MoccaBønne123')''')

# Kaffebrenneri
cursor.execute(
    '''INSERT INTO Kaffebrenneri VALUES ('Hallstad brenneri')''')
cursor.execute(
    '''INSERT INTO Kaffebrenneri VALUES ('Trondheims-brenneriet Jacobsen & Svart')''')
cursor.execute(
    '''INSERT INTO Kaffebrenneri VALUES ('Drammens brenneriet')''')


# KaffeGård
cursor.execute(
    '''INSERT INTO Kaffegård (Navn, Land, Region, Moh) VALUES ('Nombre de Dios', 'Santa Ana', 'El Salvador', 1500)''')
cursor.execute(
    '''INSERT INTO Kaffegård (Navn, Land, Region, Moh) VALUES ('Alsac Farm', 'Rwanda', 'Bugesera', 400)''')
cursor.execute(
    '''INSERT INTO Kaffegård (Navn, Land, Region, Moh) VALUES ('Hibande', 'Colombia', 'Andina', 963)''')
cursor.execute(
    '''INSERT INTO Kaffegård (Navn, Land, Region, Moh) VALUES ('La Granja', 'Colombia', 'Amazonas', 360)''')
cursor.execute(
    '''INSERT INTO Kaffegård (Navn, Land, Region, Moh) VALUES ('Bø Gård', 'Norge', 'Viken', 500)''')


# Foredlingsmetode
cursor.execute(
    '''INSERT INTO Foredlingsmetode (Navn, Beskrivelse) VALUES ('Vasket', 'Vask kaffen')''')
cursor.execute(
    '''INSERT INTO Foredlingsmetode (Navn) VALUES ('Bærtørket Bourbon')''')
cursor.execute(
    '''INSERT INTO Foredlingsmetode (Navn, Beskrivelse) VALUES ('Soltørket', 'La kaffen tørke ute i sola')''')


# Kaffeparti
cursor.execute(
    '''INSERT INTO Kaffeparti (InnhøstingsÅr, Kilopris, GårdID, ForedlingID) VALUES (2022, 8, 1, 1)''')
cursor.execute(
    '''INSERT INTO Kaffeparti (InnhøstingsÅr, Kilopris, GårdID, ForedlingID) VALUES (2021, 8, 2, 2)''')
cursor.execute(
    '''INSERT INTO Kaffeparti (InnhøstingsÅr, Kilopris, GårdID, ForedlingID) VALUES (2021, 32, 3, 3)''')
cursor.execute(
    '''INSERT INTO Kaffeparti (InnhøstingsÅr, Kilopris, GårdID, ForedlingID) VALUES (2020, 120, 4, 1)''')
cursor.execute(
    '''INSERT INTO Kaffeparti (InnhøstingsÅr, Kilopris, GårdID, ForedlingID) VALUES (2020, 56, 5, 2)''')

# Kaffe
cursor.execute(
    '''INSERT INTO Kaffe (KaffeNavn, BrenneriNavn, Beskrivelse, Brenningsgrad, BrenningDato, Kilopris, partiID) VALUES ('Vinterkaffe 2022', 'Trondheims-brenneriet Jacobsen & Svart', 'En velsmakende og kompleks kaffe for mørketiden', 'lys', '12-12-2021', 600, 2)''')
cursor.execute(
    '''INSERT INTO Kaffe (KaffeNavn, BrenneriNavn, Beskrivelse, Brenningsgrad, BrenningDato, Kilopris, partiID) VALUES ('Fin frøken', 'Hallstad brenneri', 'En meget floral kaffe', 'lys', '12-12-2021', 240, 2)''')
cursor.execute(
    '''INSERT INTO Kaffe (KaffeNavn, BrenneriNavn, Beskrivelse, Brenningsgrad, BrenningDato, Kilopris, partiID) VALUES ('Lavazza', 'Trondheims brenneri', 'Rund kaffe med en svak bitterhet', 'middels', '12-12-2021', 240, 1)''')
cursor.execute(
    '''INSERT INTO Kaffe (KaffeNavn, BrenneriNavn, Beskrivelse, Brenningsgrad, BrenningDato, Kilopris, partiID) VALUES ('Fin frøken', 'Drammens Brenneri', 'Sommerlig og floral', 'mørk', '12-12-2021', 240, 2)''')
cursor.execute(
    '''INSERT INTO Kaffe (KaffeNavn, BrenneriNavn, Beskrivelse, Brenningsgrad, BrenningDato, Kilopris, partiID) VALUES ('Mor Monsen', 'Trondheims brenneri', 'Fyldig', 'middels', '12-12-2021', 240, 1)''')


# Kaffesmaking
cursor.execute(
    '''INSERT INTO Kaffesmaking (BrukerID, Beskrivelse, Poeng, KaffeNavn, BrenneriNavn) VALUES (1, 'En meget god kaffe med sommerlige smaker!', 9, 'Fin frøken', 'Hallstad brenneri')''')
cursor.execute(
    '''INSERT INTO Kaffesmaking (BrukerID, Beskrivelse, Poeng, KaffeNavn, BrenneriNavn) VALUES (2, 'Wow – en odyssé for smaksløkene: sitrusskall, melkesjokolade, aprikos!', 10, 'Vinterkaffe 2022', 'Trondheims-brenneriet Jacobsen & Svart')''')

# Kaffebønne
cursor.execute(
    '''INSERT INTO Kaffebønne (Artsnavn) VALUES ('Arabica')''')
cursor.execute(
    '''INSERT INTO Kaffebønne (Artsnavn) VALUES ('Robusta')''')
cursor.execute(
    '''INSERT INTO Kaffebønne (Artsnavn) VALUES ('Liberica')''')

# PartiBestårAv
cursor.execute(
    '''INSERT INTO PartiBestårAv VALUES (1, 1)''')
cursor.execute(
    '''INSERT INTO PartiBestårAv VALUES (2, 1)''')

# BønneDyrketPåGård
cursor.execute(
    '''INSERT INTO BønneDyrketPåGård VALUES (1, 1)''')


cursor.execute("SELECT * FROM Bruker")
rows = cursor.fetchall()
print("All rows in the table bruker:")
print(rows)

cursor.execute("SELECT * FROM Kaffebrenneri")
rows = cursor.fetchall()
print("All rows in the table Kaffebrenneri:")
print(rows)

cursor.execute("SELECT * FROM Kaffegård")
rows = cursor.fetchall()
print("All rows in the table Kaffegård:")
print(rows)

cursor.execute("SELECT * FROM Kaffeparti")
rows = cursor.fetchall()
print("All rows in the table Kaffeparti:")
print(rows)

cursor.execute("SELECT * FROM Kaffe")
rows = cursor.fetchall()
print("All rows in the table Kaffe:")
print(rows)

con.commit()

con.close()
