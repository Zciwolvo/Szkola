USE PomiaryPogodowe
GO

INSERT INTO dbo.Stacje (IDstacji, Lokalizacja, WysokoscNPM, SzerokoscGeograficzna, DlugoscGeograficzna)
VALUES (1, 'New York City', 10.2, 40.7128, -74.0060),
(2, 'Los Angeles', 71.9, 34.0522, -118.2437),
(3, 'Chicago', 181.9, 41.8781, -87.6298),
(4, 'Houston', 18.3, 29.7604, -95.3698),
(5, 'Miami', 2.4, 25.7617, -80.1918);

INSERT INTO dbo.Pomiary (IDpomiaru, IDstacji, CzasPomiaru, Temperatura, TemperaturaOdczuwalna, Wilgotnosc, Cisnienie, SzansaOpadow, Opady, PredkoscWiatru, KierunekWiatru)
VALUES (1, 1, '2023-04-25 12:00:00', 15.2, 12.8, 70, 1012.2, 40, 0, 5.4, 'NE'),
(2, 1, '2023-04-25 13:00:00', 16.8, 14.5, 68, 1010.9, 55, 0, 6.1, 'E'),
(3, 2, '2023-04-25 12:00:00', 20.1, 21.2, 63, 1008.5, 20, 0, 3.2, 'SW'),
(4, 2, '2023-04-25 13:00:00', 19.5, 20.1, 66, 1009.8, 10, 0, 4.5, 'S'),
(5, 3, '2023-04-25 12:00:00', 12.3, 10.5, 75, 1013.4, 75, 0.2, 2.1, 'W'),
(6, 3, '2023-04-25 13:00:00', 11.8, 9.9, 72, 1014.1, 60, 0.1, 2.8, 'NW');

INSERT INTO dbo.Uzytkownicy (IDuzytkownika, AdresEmail, Imie, Nazwisko)
VALUES (1, 'john.doe@example.com', 'John', 'Doe'),
(2, 'jane.doe@example.com', 'Jane', 'Doe'),
(3, 'bob.smith@example.com', 'Bob', 'Smith');

INSERT INTO dbo.Raporty (IDraportu, IDuzytkownika, IDpomiaru, Raport)
VALUES (1, 1, 1, 'Temperatura w normie'),
(2, 1, 2, 'Wysoka szansa na opady'),
(3, 2, 3, 'Niska wilgotność powietrza'),
(4, 2, 4, 'Niska szansa na opady');

