USE Practical10_DW;
GO
CREATE TABLE Dim_Customer (
    CustomerKey INT IDENTITY(1,1) PRIMARY KEY,
    CustomerID INT NOT NULL,
    Name VARCHAR(100), Email VARCHAR(150), City VARCHAR(100), SignupDate DATE
);
CREATE TABLE Dim_Product (
    ProductKey INT IDENTITY(1,1) PRIMARY KEY,
    ProductID INT NOT NULL,
    ProductName VARCHAR(100), Category VARCHAR(100), UnitPrice DECIMAL(12,2)
);
CREATE TABLE Dim_Date (
    DateKey INT PRIMARY KEY,
    DateValue DATE NOT NULL,
    Year INT, Month INT, MonthName VARCHAR(20), Quarter INT
);
