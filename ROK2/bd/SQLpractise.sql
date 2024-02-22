SELECT * FROM sys.database_principals

EXEC sp_helplogins
EXEC sp_helplogins 'sa'

CREATE LOGIN [C:\Users\Igor] FROM WINDOWS WITH DEFAULT_DATABASE=[master],
DEFAULT_LANGUAGE=[us_english]
GO

ALTER SERVER ROLE [sysadmin] ADD MEMBER [C:\Users\Igor]
GO

SELECT * FROM sys.fn_builtin_permissions(DEFAULT)

SELECT * FROM sys.fn_builtin_permissions('login')

SELECT * FROM sys.fn_builtin_permissions(DEFAULT)
WHERE permission_name = 'SELECT'
GO	

CREATE LOGIN SzefMagazynu WITH PASSWORD='mag123#321';
--sp_addlogin PracMagazynu

CREATE USER SzefMagazynu FROM LOGIN SzefMagazynu


USE master
GO

GRANT CONNECT SQL TO [SzefMagazynu]
GO

USE [BD1d2b_2022]
go

GRANT INSERT,UPDATE, DELETE
ON BD1d2b_2022.dbo.Produkty
TO [SzefMagazynu];