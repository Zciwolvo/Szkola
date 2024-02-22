USE BD1d2b_2022
GO

CREATE TRIGGER block_price_change
ON Produkty
FOR UPDATE
AS
BEGIN
  IF UPDATE(CenaJednostkowa)
  BEGIN
    IF EXISTS (
      SELECT *
      FROM inserted i
      JOIN deleted d ON i.IDproduktu = d.IDproduktu
      WHERE i.CenaJednostkowa > (d.CenaJednostkowa * 1.1)
    )
    BEGIN
      RAISERROR('Price change higher that 10 percent!', 1, 1);
      ROLLBACK TRANSACTION;
      RETURN;
    END
  END
END;
