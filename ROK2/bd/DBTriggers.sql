USE PomiaryPogodowe
GO

CREATE TRIGGER tr_dodaj_nowe_stacje
ON dbo.Stacje
AFTER INSERT
AS
BEGIN
	DECLARE @id_stacji INT
	SELECT @id_stacji = ID_stacji FROM inserted
	IF NOT EXISTS (SELECT * FROM dbo.Pomiary WHERE ID_stacji = @id_stacji)
	BEGIN
		INSERT INTO dbo.Pomiary (ID_stacji, ID_parametru, Wartosc, Data_pomiaru)
		VALUES (@id_stacji, 1, 0, GETDATE())
	END
END