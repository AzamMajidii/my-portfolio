CREATE DATABASE NorthwindDW

/*-------------------------------------------------------------------------------------------------------------------------*/
-----------Create table DimShipper------------
USE NorthwindDW;
GO 
DROP TABLE IF EXISTS DimShipper
CREATE TABLE DimShipper
(
	ShipperKey INT PRIMARY KEY,
	ShipperIDBK INT,
	ShipCompanyName NVARCHAR(50),
	ETLTime DATETIME
) ON DIM_DW WITH (DATA_COMPRESSION=PAGE);
GO
-----------Fill DimShipper------------
USE Northwind;
GO

SELECT 
ShipperID AS ShipperKey,
ShipperID AS ShipperIDBK,
CompanyName AS ShipCompanyName,
GETDATE() AS ETLTime
FROM dbo.Shippers

/*-------------------------------------------------------------------------------------------------------------------------*/

-----------Create table DimProduct------------
CREATE TABLE DimProduct
(
	ProductKey INT PRIMARY KEY,
	ProductIDBK INT,
	ProductName NVARCHAR(50),
	SupplierID INT,
	SupplierCompanyName NVARCHAR(50),
	SupplierCity NVARCHAR(15),
	SupplierRegion NVARCHAR(15),
	SupplierCountry NVARCHAR(15),
	ProductCategoryID INT,
	ProductCategoryName NVARCHAR(30),
	ETLTime DATETIME
) ON DIM_DW WITH (DATA_COMPRESSION=PAGE);
GO

-----------Fill DimShipper------------
USE Northwind;
GO

SELECT
	Products.ProductID AS ProductKey,
	Products.ProductID AS ProductIDBK,
	Products.ProductName,
	Suppliers.SupplierID,
	Suppliers.CompanyName AS SupplierCompanyName,
	Suppliers.City AS SupplierCity,
	Suppliers.Region AS SupplierRegion,
	Suppliers.Country AS SupplierCountry,
	Categories.CategoryID AS CategoryID,
	Categories.CategoryName AS ProductCategoryName,
	GETDATE() AS ETLTime
FROM dbo.Products
LEFT JOIN dbo.Suppliers ON
	Suppliers.SupplierID = Products.SupplierID
LEFT JOIN dbo.Categories ON
	Categories.CategoryID = Products.CategoryID
GO


/*-------------------------------------------------------------------------------------------------------------------------*/

-----------Create table DimCustomer------------

USE NorthwindDW;
GO

DROP TABLE IF EXISTS DimCustomer;
GO

CREATE TABLE DimCustomer
(
	CustomerKey INT IDENTITY(1,1) PRIMARY KEY NONCLUSTERED,
	CustomerIDBK NCHAR(5),
	CustomerCompanyName NVARCHAR(50),
	CustomerCity NVARCHAR(15),
	CustomerRegion NVARCHAR(15),
	CustomerCountry NVARCHAR(15),
	ETLTime DATETIME
) ON DIM_DW WITH (DATA_COMPRESSION=PAGE);
GO
CREATE UNIQUE CLUSTERED INDEX IX_Clustered_CustomerIDBK ON DimCustomer(CustomerIDBK)
	WITH (DATA_COMPRESSION=PAGE) ON DIM_DW

-----------Fill DimCustomer------------
USE Northwind;
GO

SELECT 
	CustomerID AS CustomerIDBK,
	CompanyName AS CustomerCompanyName,
	City AS CustomerCity,
	Region AS CustomerRegion,
	Country AS CustomerCountry,
	GETDATE() AS ETLTime
FROM dbo.Customers

/*-------------------------------------------------------------------------------------------------------------------------*/

-----------Create table DimEmployee------------

USE NorthwindDW;
GO

DROP TABLE IF EXISTS DimEmployee;
GO

CREATE TABLE DimEmployee
(
	EmployeeKey INT PRIMARY KEY,
	EmployeeIDBK INT,
	FullName NVARCHAR(50),
	Title NVARCHAR(50),
	Gender NVARCHAR(30),
	BirthDateKey DATE,
	HireDateKey DATE,
	City NVARCHAR(15),
	Region NVARCHAR(15),
	Country NVARCHAR(15),
	ReportsTo INT,
	ETLTime DATETIME
) ON DIM_DW WITH (DATA_COMPRESSION=PAGE);
GO

-----------Fill DimEmployee------------
USE Northwind;
GO

SELECT
	EmployeeID AS EmployeeKey,
	EmployeeID AS EmployeeIDBK,
	CONCAT(FirstName, ' ',LastName) AS FullName,
	Title,
	TitleOfCourtesy AS Gender,
	BirthDate,
	HireDate,
	City,
	Region,
	Country,
	ReportsTo,
	GETDATE() AS ETLTime
FROM dbo.Employees



/*-------------------------------------------------------------------------------------------------------------------------*/

-----------Create table DimShipGeography------------

CREATE TABLE DimShipGeography
(
	ShipGeographyKey INT IDENTITY(1,1) PRIMARY KEY NONCLUSTERED,
	ShipCity NVARCHAR(15),
	ShipCountry NVARCHAR(15),
	ETLTime DATETIME
) ON DIM_DW WITH (DATA_COMPRESSION=PAGE);

CREATE UNIQUE CLUSTERED INDEX IX_Clustered_ShipCountry_ShipCity ON DimShipGeography(ShipCity, ShipCountry)
	WITH (DATA_COMPRESSION=PAGE) ON DIM_DW
GO

-----------Fill DimShipGeography------------
USE Northwind;
GO

SELECT 
	DISTINCT ShipCity AS ShipCity ,
	ShipCountry,
	GETDATE() AS ETLTime
  FROM dbo.Orders

/*-------------------------------------------------------------------------------------------------------------------------*/

-----------Create table FactOrder------------

CREATE TABLE FactOrder
(
	OrderKey INT IDENTITY(1,1) PRIMARY KEY NONCLUSTERED,
	OrderIDBK INT,
	CustomerKey INT,
	EmployeeKey INT,
	ProductKey INT,
	OrderDateKey INT,
	RequiredDateKey INT,
	ShippedDateKey INT,
	ShipperKey INT,
	ShipGeographyKey INT,
	ShipAddress NVARCHAR(60),
	ShipPostalCode NVARCHAR(10),
	Freight MONEY,
	UnitPrice MONEY,
	Quantity SMALLINT,
	Discount DECIMAL(5,2)
) ON Fact_DW WITH (DATA_COMPRESSION=PAGE);

CREATE UNIQUE CLUSTERED INDEX IX_CLUSTERED_OrderIDBK ON FactOrder(OrderIDBK)
	WITH (DATA_COMPRESSION=PAGE) ON Fact_DW;
GO

-----------Fill FactOrder------------
USE Northwind;
GO

SELECT 
	Orders.OrderID AS OrderIDBK,
	Orders.CustomerID,
	Orders.EmployeeID AS EmployeeKey,
	FORMAT(Orders.OrderDate,'yyyMMdd') AS OrderDateKey,
	FORMAT(Orders.RequiredDate,'yyyMMdd') AS RequiredDateKey,
	FORMAT(Orders.ShippedDate,'yyyMMdd') AS ShippedDateKey,
	Orders.ShipVia AS ShipperKey,
	Orders.ShipName,
	Orders.ShipAddress,
	Orders.ShipCity,
	Orders.ShipPostalCode,
	Orders.ShipCountry,
	OrderDetails.ProductID AS ProductKey,
	Orders.Freight,
	OrderDetails.UnitPrice,
	OrderDetails.Quantity,
	OrderDetails.Discount, 
	GETDATE() AS ETLTime
FROM dbo.Orders
LEFT JOIN dbo.[Order Details] AS OrderDetails ON
	OrderDetails.OrderID = Orders.OrderID;
GO


