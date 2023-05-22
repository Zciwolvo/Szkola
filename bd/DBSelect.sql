USE PomiaryPogodowe
GO

SELECT * FROM dbo.fn_srednia_parametru(2, '2022-01-01', '2022-12-31')
SELECT * FROM fn_generuj_raport(1, 2, '2022-01-01', '2022-12-31')
SELECT * FROM fn_wyszukaj_pomiary(1, 2, '2022-01-01', '2022-12-31')

