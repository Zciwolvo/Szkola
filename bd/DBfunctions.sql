USE PomiaryPogodowe
GO

DROP FUNCTION IF EXISTS dbo.fn_srednia_parametru;
GO
CREATE FUNCTION fn_srednia_parametru (@id_parametru INT, @data_od DATETIME, @data_do DATETIME)
RETURNS FLOAT
AS
BEGIN
    DECLARE @srednia FLOAT
    SELECT @srednia = AVG(Wartosc)
    FROM dbo.Pomiary
    WHERE ID_parametru = @id_parametru AND Data_pomiaru BETWEEN @data_od AND @data_do
    RETURN @srednia
END
GO

DROP FUNCTION IF EXISTS dbo.fn_generuj_raport;
GO
CREATE FUNCTION fn_generuj_raport (@id_stacji INT, @id_parametru INT, @data_od DATETIME, @data_do DATETIME)
RETURNS TABLE
AS
RETURN
(
    SELECT 
	pom.ID_stacji, sta.Nazwa, pom.ID_parametru, par.Nazwa AS Nazwa_parametru, 
	AVG(Wartosc) AS Sred_wartosc, MIN(Wartosc) AS Minimalna_wartosc, 
	MAX(Wartosc) AS Maksymalna_wartosc, COUNT(*) AS Liczba_pomiarow
    FROM dbo.Pomiary AS pom
    INNER JOIN dbo.Stacje AS sta ON pom.ID_stacji = sta.ID_stacji
    INNER JOIN dbo.Parametry AS par ON pom.ID_parametru = par.ID_parametru 
	WHERE pom.ID_stacji = @id_stacji AND pom.ID_parametru = @id_parametru 
	AND pom.Data_pomiaru BETWEEN @data_od AND @data_do
    GROUP BY pom.ID_stacji, sta.Nazwa, pom.ID_parametru, par.Nazwa
)
GO

DROP FUNCTION IF EXISTS dbo.fn_wyszukaj_pomiary;
GO
CREATE FUNCTION fn_wyszukaj_pomiary (@id_stacji INT, @id_parametru INT, @data_od DATETIME, @data_do DATETIME)
RETURNS TABLE
AS
RETURN
(
    SELECT pom.ID_pomiaru, pom.ID_stacji, sta.Nazwa AS Nazwa_stacji, pom.ID_parametru, par.Nazwa AS Nazwa_parametru, Wartosc, Data_pomiaru
    FROM dbo.Pomiary AS pom
    INNER JOIN dbo.Stacje AS sta ON pom.ID_stacji = sta.ID_stacji
    INNER JOIN dbo.Parametry AS par ON pom.ID_parametru = par.ID_parametru
    WHERE pom.ID_stacji = sta.ID_stacji AND pom.ID_parametru = @id_parametru AND pom.Data_pomiaru BETWEEN @data_od AND @data_do
)
GO

