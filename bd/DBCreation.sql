USE master

DROP DATABASE IF EXISTS PomiaryPogodowe;
CREATE DATABASE PomiaryPogodowe ON
(
	NAME = PomiaryPogodowe_dat,
	FILENAME = 'C:\szkola\Szkola\bd\PomiaryPogodowedat.mdf',
	SIZE = 10,
	MAXSIZE = 50,
	FILEGROWTH = 5
)
LOG ON
(
	NAME = PomiaryPogodowe_log,
	FILENAME = 'C:\szkola\Szkola\bd\PomiaryPogodowelog.ldf',
	SIZE = 5 MB,
	MAXSIZE = 25 MB,
	FILEGROWTH = 5 MB
);
GO

USE PomiaryPogodowe;

CREATE TABLE dbo.Stacje
(
	IDstacji INT NOT NULL PRIMARY KEY,
	Lokalizacja CHAR(255) NOT NULL,
	WysokoscNPM FLOAT NOT NULL,
	SzerokoscGeograficzna FLOAT NOT NULL, 
	DlugoscGeograficzna FLOAT NOT NULL
);

CREATE TABLE dbo.Pomiary 
(
	IDpomiaru INT NOT NULL PRIMARY KEY,
	IDstacji INT NOT NULL FOREIGN KEY REFERENCES Stacje(IDstacji),
	CzasPomiaru DATETIME NOT NULL,
	Temperatura FLOAT NOT NULL,
	TemperaturaOdczuwalna FLOAT NOT NULL,
	Wilgotnosc INT NOT NULL,
	Cisnienie FLOAT NOT NULL,
	SzansaOpadow INT NOT NULL,
	Opady FLOAT NOT NULL,
	PredkoscWiatru FLOAT NOT NULL,
	KierunekWiatru CHAR(2) NOT NULL
);

CREATE TABLE dbo.Uzytkownicy
(
	IDuzytkownika INT NOT NULL PRIMARY KEY,
	AdresEmail CHAR(255) NOT NULL,
	Imie CHAR(255) NOT NULL,
	Nazwisko CHAR(255) NOT NULL,
);

CREATE TABLE dbo.Raporty
(
	IDraportu INT NOT NULL PRIMARY KEY,
	IDuzytkownika INT NOT NULL FOREIGN KEY REFERENCES Uzytkownicy(IDuzytkownika),
	IDpomiaru INT NOT NULL FOREIGN KEY REFERENCES Pomiary(IDpomiaru),
	Raport CHAR(255) NOT NULL
);
GO