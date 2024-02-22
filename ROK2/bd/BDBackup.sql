USE master
GO

EXEC master.dbo.sp_addumpdevice @devtype = N'disk',
	@logicalname = N'BackUpTest',
	@physicalname = N'C:\szkola\Szkola\bd'
GO

BACKUP DATABASE BD1d2b_2022 TO BackUpTest;

