USE Practical10_DW;
GO
CREATE TABLE Fact_Sales (
    SalesKey INT IDENTITY(1,1) PRIMARY KEY,
    OrderID INT NOT NULL,
    CustomerKey INT,
    ProductKey INT,
    DateKey INT,
    Quantity INT,
    UnitPrice DECIMAL(12,2),
    TotalAmount DECIMAL(14,2),
    PaymentMethod VARCHAR(50),
    PaymentStatus VARCHAR(50),
    FOREIGN KEY (CustomerKey) REFERENCES Dim_Customer(CustomerKey),
    FOREIGN KEY (ProductKey) REFERENCES Dim_Product(ProductKey),
    FOREIGN KEY (DateKey) REFERENCES Dim_Date(DateKey)
);
