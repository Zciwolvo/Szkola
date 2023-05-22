USE PomiaryPogodowe
GO

INSERT INTO dbo.Stacje (ID_stacji, Nazwa, Kraj, Region, Miasto)
VALUES	(1, 'Stacja 1', 'Polska', 'Mazowieckie', 'Warszawa'),
		(2, 'Stacja 2', 'Polska', 'Małopolskie', 'Kraków'),
		(3, 'Stacja 3', 'Polska', 'Wielkopolskie', 'Poznań');

INSERT INTO dbo.Jednostki (ID_jednostki, Nazwa)
VALUES	(1, 'Stopień Celsjusza'),
		(2, 'Stopień Fahrenheita'),
		(3, 'Gram na metr sześcienny'),
		(4, 'Paskal');

INSERT INTO dbo.Parametry (ID_parametru, Nazwa, ID_jednostki)
VALUES	(1, 'Temperatura', 1),
		(2, 'Wilgotność', 3),
		(3, 'Ciśnienie atmosferyczne', 4);


INSERT INTO dbo.Pomiary (ID_pomiaru, ID_stacji, ID_parametru, Wartosc, Data_pomiaru)
VALUES	(1, 1, 1, 20.5, '2023-05-22 12:00:00'),
		(2, 1, 2, 50, '2023-05-22 12:00:00'),
		(3, 1, 3, 1013, '2023-05-22 12:00:00'),
		(4, 2, 1, 18.2, '2023-05-22 12:00:00'),
		(5, 2, 2, 60, '2023-05-22 12:00:00'),
		(6, 2, 3, 1015, '2023-05-22 12:00:00'),
		(7, 3, 1, 22.1, '2023-05-22 12:00:00'),
		(8, 3, 2, 45, '2023-05-22 12:00:00'),
		(9, 3, 3, 1010, '2023-05-22 12:00:00');
