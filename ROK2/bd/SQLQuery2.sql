USE BD1d2b_2022

SELECT * FROM Produkty WHERE IDproduktu = 1

UPDATE Produkty
SET CenaJednostkowa = CenaJednostkowa*1.1
WHERE IDproduktu = 1

SELECT * FROM Produkty WHERE IDproduktu = 1