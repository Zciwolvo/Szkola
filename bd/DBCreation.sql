USE master

DROP DATABASE IF EXISTS PomiaryPogodowe;
CREATE DATABASE PomiaryPogodowe ON
(
	NAME = PomiaryPogodowe_dat,
	FILENAME = 'C:\szkola\Szkola\bd\PomiaryPogodowe_dat.mdf',
	SIZE = 10,
	MAXSIZE = 50,
	FILEGROWTH = 5
)
LOG ON
(
	NAME = PomiaryPogodowe_log,
	FILENAME = 'C:\szkola\Szkola\bd\PomiaryPogodowe_log.ldf',
	SIZE = 5 MB,
	MAXSIZE = 25 MB,
	FILEGROWTH = 5 MB
);
GO

USE PomiaryPogodowe;

DROP TABLE IF EXISTS dbo.Stacje;
CREATE TABLE dbo.Stacje
(
	ID_stacji INT NOT NULL PRIMARY KEY,
	Nazwa CHAR(255) NOT NULL,
	Kraj CHAR(255) NOT NULL,
	Region CHAR(255),
	Miasto CHAR(255)
);

DROP TABLE IF EXISTS dbo.Jednostki;
CREATE TABLE dbo.Jednostki
(
	ID_jednostki INT NOT NULL PRIMARY KEY,
	Nazwa CHAR(255) NOT NULL
);

DROP TABLE IF EXISTS dbo.Parametry;
CREATE TABLE dbo.Parametry
(
	ID_parametru INT NOT NULL PRIMARY KEY,
	Nazwa CHAR(255) NOT NULL,
	ID_jednostki INT NOT NULL FOREIGN KEY REFERENCES dbo.Jednostki(ID_jednostki)
);

DROP TABLE IF EXISTS dbo.Pomiary;
CREATE TABLE dbo.Pomiary 
(
	ID_pomiaru INT NOT NULL PRIMARY KEY,
	ID_stacji INT NOT NULL FOREIGN KEY REFERENCES Stacje(ID_stacji),
	ID_parametru INT NOT NULL FOREIGN KEY REFERENCES dbo.Parametry(ID_parametru),
	Wartosc FLOAT NOT NULL,
	Data_pomiaru DATETIME NOT NULL
);
GO
