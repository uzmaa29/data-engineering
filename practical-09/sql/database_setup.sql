CREATE DATABASE Practical9_ECommerce;
GO
USE Practical9_ECommerce;
GO

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(150),
    city VARCHAR(100),
    signup_date DATE
);

CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(100),
    unit_price DECIMAL(12,2)
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    order_date DATE,
    quantity INT,
    status VARCHAR(30)
);

CREATE TABLE Payments (
    payment_id INT PRIMARY KEY,
    order_id INT,
    payment_date DATE,
    payment_method VARCHAR(50),
    payment_amount DECIMAL(12,2),
    payment_status VARCHAR(30)
);

CREATE TABLE Sales_Report (
    order_id INT,
    customer_id INT,
    product_id INT,
    order_date DATE,
    quantity INT,
    status VARCHAR(30),
    product_name VARCHAR(100),
    category VARCHAR(100),
    unit_price DECIMAL(12,2),
    line_total DECIMAL(14,2),
    name VARCHAR(100),
    city VARCHAR(100),
    payment_method VARCHAR(50),
    payment_amount DECIMAL(12,2),
    payment_status VARCHAR(30)
);

SELECT category, SUM(line_total) AS total_sales
FROM Sales_Report
WHERE status = 'Completed'
GROUP BY category
ORDER BY total_sales DESC;
