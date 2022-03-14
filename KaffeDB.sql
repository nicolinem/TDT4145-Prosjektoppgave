CREATE TABLE Bruker (
    BrukerID   INTEGER NOT NULL,
    Navn       VARCHAR(30) NOT NULL,
    Epost      VARCHAR(50) NOT NULL,
    Passord    VARCHAR(30) NOT NULL,
  PRIMARY KEY (BrukerID));

CREATE TABLE Kaffebrenneri (
    BrenneriNavn VARCHAR(30) NOT NULL,
    PRIMARY KEY (BrenneriNavn));

CREATE TABLE Kaffegård(
    GårdID INTEGER NOT NULL,
    Navn     VARCHAR(30) NOT NULL,
    Land     VARCHAR(30) NOT NULL,
    Region   VARCHAR(30) NOT NULL,
    Moh      INTEGER,
   PRIMARY KEY (GårdID));


CREATE TABLE Foredlingsmetode(
    ForedlingID INTEGER NOT NULL ,
    Navn     VARCHAR(30) NOT NULL,
    Beskrivelse VARCHAR(100),
    PRIMARY KEY (ForedlingID)
);

CREATE TABLE  Kaffeparti (
    PartiID       INTEGER NOT NULL ,
    InnhøstingsÅr INTEGER NOT NULL,
    Kilopris      INTEGER NOT NULL,
    GårdsID       INTEGER NOT NULL,
    ForedlingID   INTEGER NOT NULL,
    PRIMARY KEY (PartiID),
    CONSTRAINT Kaffeparti_FK1 FOREIGN KEY (ForedlingID) REFERENCES Foredlingsmetode(ForedlingID)
      ON UPDATE CASCADE
      ON DELETE CASCADE,
    CONSTRAINT Kaffeparti_FK2 FOREIGN KEY (GårdsID) REFERENCES Kaffegård(GårdID)
      ON UPDATE CASCADE
      ON DELETE CASCADE);


CREATE TABLE Kaffe (
  KaffeNavn     VARCHAR(30) NOT NULL,
  BrenneriNavn  VARCHAR(30) NOT NULL,
  Beskrivelse   VARCHAR(240),
  Brenningsgrad VARCHAR(10) CHECK (Brenningsgrad = 'lys' OR Brenningsgrad = 'middels' OR Brenningsgrad = 'mørk'),
  BrenningDato  DATE NOT NULL,
  Kilopris      INTEGER NOT NULL,
  PartiID       INTEGER NOT NULL,
  PRIMARY KEY (KaffeNavn, BrenneriNavn),
  FOREIGN KEY (BrenneriNavn) REFERENCES Kaffebrenneri(BrenneriNavn)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
  FOREIGN KEY (PartiID) REFERENCES Kaffeparti(PartiID)
    ON UPDATE CASCADE
    ON DELETE CASCADE);

CREATE TABLE Kaffesmaking (
  SmakID      INTEGER NOT NULL,
  BrukerID    INTEGER NOT NULL,
  Beskrivelse VARCHAR(100),
  Poeng INTEGER CHECK (Poeng >= 0 AND Poeng <= 10),
  KaffeNavn   VARCHAR(30) NOT NULL,
  Dato DATE DEFAULT (DATETIME('now')),
  PRIMARY KEY (SmakID, BrukerID),
  FOREIGN KEY (BrukerID) REFERENCES Bruker(BrukerID)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
  FOREIGN KEY (KaffeNavn) REFERENCES Kaffe(KaffeNavn)
    ON UPDATE CASCADE
    ON DELETE CASCADE
  );


CREATE TABLE Kaffebønne(
    BønneID INTEGER NOT NULL,
    Artsnavn     VARCHAR(30) NOT NULL,
    PRIMARY KEY (BønneID)
);

CREATE TABLE PartiBestårAv(
    PartiID    INTEGER NOT NULL,
    BønneID    INTEGER NOT NULL,
    FOREIGN KEY (PartiID) REFERENCES Kaffeparti(PartiID) 
      ON UPDATE CASCADE
      ON DELETE CASCADE,
    FOREIGN KEY (BønneID) REFERENCES Kaffebønne(BønneID) 
      ON UPDATE CASCADE
      ON DELETE CASCADE
);



CREATE TABLE BønneDyrketPåGård(
    BønneID    INTEGER NOT NULL,
    GårdID     INTEGER NOT NULL,
    FOREIGN KEY (BønneID) REFERENCES Kaffebønne(BønneID) 
      ON UPDATE CASCADE
      ON DELETE CASCADE,
    FOREIGN KEY (GårdID) REFERENCES Kaffegård(GårdID) 
      ON UPDATE CASCADE
      ON DELETE CASCADE
);