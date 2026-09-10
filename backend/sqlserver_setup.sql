CREATE TABLE dbo.clients (
    id INT IDENTITY(1,1) PRIMARY KEY,
    client_name NVARCHAR(200) NOT NULL,
    email NVARCHAR(255) NOT NULL,
    phone NVARCHAR(50) NULL,
    company NVARCHAR(200) NULL,
    city NVARCHAR(100) NULL,
    status NVARCHAR(50) NOT NULL DEFAULT 'active'
);

INSERT INTO dbo.clients (client_name, email, phone, company, city, status)
VALUES
    ('Alicia Johnson', 'alicia.johnson@example.com', '+1-555-0101', 'Northwind Labs', 'Seattle', 'active'),
    ('Marcus Chen', 'marcus.chen@example.com', '+1-555-0102', 'BrightPeak', 'Austin', 'pending'),
    ('Sofia Patel', 'sofia.patel@example.com', '+1-555-0103', 'RiverStone Group', 'Chicago', 'active');
