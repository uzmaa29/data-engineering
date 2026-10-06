CREATE DATABASE Practical8_ETL;
GO
USE Practical8_ETL;
GO
CREATE TABLE Customers_CSV (CustomerID INT, Name VARCHAR(100), Email VARCHAR(150), City VARCHAR(100));
GO
CREATE TABLE Customers_Combined (CustomerID INT, Name VARCHAR(100), Email VARCHAR(150), City VARCHAR(100));
GO
CREATE TABLE Sales_JSON (order_id INT, customer_id INT, product VARCHAR(100), quantity INT, price DECIMAL(12,2), total_amount DECIMAL(14,2), status VARCHAR(50));
GO
CREATE TABLE Incremental_Sales (OrderID INT, CustomerID INT, Product VARCHAR(100), Quantity INT, Price DECIMAL(12,2), LastUpdated DATE);
GO
SELECT * FROM Customers_CSV;
SELECT * FROM Customers_Combined;
SELECT * FROM Sales_JSON;
SELECT * FROM Incremental_Sales;
