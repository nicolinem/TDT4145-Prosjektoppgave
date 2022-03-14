CREATE TABLE Bruker (
    BrukerID INTEGER NOT NULL,
    Navn       VARCHAR(30) NOT NULL,
    Epost      VARCHAR(50) NOT NULL,
    Passord    VARCHAR(30) NOT NULL,
    CONSTRAINT Bruker_PK PRIMARY KEY (BrukerID));

CREATE TABLE Kaffebrenneri (
    BrenneriNavn VARCHAR(30) NOT NULL,
    CONSTRAINT Kaffebrenneri_PK PRIMARY KEY (BrenneriID));

CREATE TABLE Kaffegård(
    GårdID INTEGER NOT NULL,
    Navn     VARCHAR(30) NOT NULL,
    Land     VARCHAR(30) NOT NULL,
    Region   VARCHAR(30) NOT NULL,
    Moh       INTEGER,
    CONSTRAINT Kaffegård_PK PRIMARY KEY (GårdID)
);

CREATE TABLE Foredlingsmetode(
    ForedlingID INTEGER NOT NULL,
    Navn     VARCHAR(30) NOT NULL,
    Beskrivelse VARCHAR(100),
    CONSTRAINT Foredlingsmetode_PK PRIMARY KEY (ForedlingID)
);

CREATE TABLE  Kaffeparti (
    PartiID       INTEGER NOT NULL,
    InnhøstingsÅr INTEGER NOT NULL,
    Kilopris      INTEGER NOT NULL,
    GårdsID       INTEGER NOT NULL,
    ForedlingID   INTEGER NOT NULL,
    CONSTRAINT Kaffeparti_PK PRIMARY KEY (PartiID),
    CONSTRAINT Kaffeparti_FK1 FOREIGN KEY (ForedlingID) REFERENCES Foredlingsmetode(ForedlingID)
      ON UPDATE CASCADE
      ON DELETE CASCADE,
    CONSTRAINT Kaffeparti_FK2 FOREIGN KEY (GårdsID) REFERENCES Kaffegård(GårdID)
      ON UPDATE CASCADE
      ON DELETE CASCADE);


CREATE TABLE Kaffe (
  KaffeNavn     VARCHAR(30) NOT NULL,
  Navn          VARCHAR(30) NOT NULL,
  Beskrivelse   VARCHAR(100),
  Brenningsgrad VARCHAR(10) CHECK (Brenningsgrad = 'lys' OR Brenningsgrad = 'middels' OR Brenningsgrad = 'mørk'),
  BrenningDato DATE NOT NULL,
  Kilopris      INTEGER NOT NULL,
  BrenneriID    INTEGER NOT NULL,
  PartiID       INTEGER NOT NULL,
  CONSTRAINT Kaffe_PK PRIMARY KEY (KaffeNavn, BrenneriNavn),
  CONSTRAINT Kaffe_FK1 FOREIGN KEY (BrenneriID) REFERENCES Kaffebrenneri(BrenneriNavn)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
  CONSTRAINT Kaffe_FK2 FOREIGN KEY (PartiID) REFERENCES Kaffeparti(PartiID)
    ON UPDATE CASCADE
    ON DELETE CASCADE);

CREATE TABLE Kaffesmaking (
  SmakID      INTEGER NOT NULL,
  BrukerID    INTEGER NOT NULL,
  KaffeNavn   VARCHAR(30) NOT NULL,
  Beskrivelse VARCHAR(100),
  Poeng INTEGER CHECK (Poeng >= 0 AND Poeng <= 10),
  Dato DATE NOT NULL,
  CONSTRAINT Kaffesmaking_PK PRIMARY KEY (SmakID, BrukerID),
  CONSTRAINT Kaffesmaking_FK1 FOREIGN KEY (BrukerID) REFERENCES Bruker(BrukerID)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
  CONSTRAINT Kaffesmaking_FK2 FOREIGN KEY (KaffeNavn) REFERENCES Kaffe(KaffeNavn)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);


CREATE TABLE Kaffebønne(
    BønneID INTEGER NOT NULL,
    Artsnavn     VARCHAR(30) NOT NULL,
    CONSTRAINT Kaffegård_PK PRIMARY KEY (BønneID)
);

CREATE TABLE PartiBestårAv(
    PartiID    INTEGER NOT NULL,
    BønneID    INTEGER NOT NULL,
    CONSTRAINT PartiBestårAv_FK1 FOREIGN KEY (PartiID) REFERENCES Kaffeparti(PartiID) 
      ON UPDATE CASCADE
      ON DELETE CASCADE,
    CONSTRAINT PartiBestårAv_FK2 FOREIGN KEY (BønneID) REFERENCES Kaffebønne(BønneID) 
      ON UPDATE CASCADE
      ON DELETE CASCADE
);



CREATE TABLE BønneDyrketPåGård(
    BønneID    INTEGER NOT NULL,
    GårdID     INTEGER NOT NULL,
    CONSTRAINT BønneDyrketPåGård_FK1 FOREIGN KEY (BønneID) REFERENCES Kaffebønne(BønneID) 
      ON UPDATE CASCADE
      ON DELETE CASCADE,
    CONSTRAINT BønneDyrketPåGård_FK1 FOREIGN KEY (GårdID) REFERENCES Kaffegård(GårdID) 
      ON UPDATE CASCADE
      ON DELETE CASCADE
);

INSERT INTO Kaffebønne VALUES (1, "God bønne");
INSERT INTO Kaffegård VALUES (1, "Møller gård", "Norge", "Trøndelag", 142);
INSERT INTO Foredlingsmetode VALUES(1, "Røyket", "Helt crazy foredling!");
INSERT INTO Kaffebrenneri VALUES (1, "Trondheims brenneri");
INSERT INTO Kaffeparti VALUES (1, 2020, 3, 1, 1);
INSERT INTO Kaffe VALUES (1, "Svart kaffe", "SVART", "mørk", 142, 1, 1);
INSERT INTO Bruker VALUES (1, "Ola", "ola@gmail.com", "kryptertpassord");
INSERT INTO Kaffesmaking VALUES (1, 1, 1, "Heftig svart kaffe", 13);
INSERT INTO BønneDyrketPåGård VALUES (1, 1);
INSERT INTO PartiBestårAv VALUES (1, 1);