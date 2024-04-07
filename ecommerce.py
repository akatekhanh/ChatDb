import sqlite3

# Connect to the database (creates a new database if it doesn't exist)
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Create the Customers table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Customers (
        customer_id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    )
''')

# Insert sample data into the Customers table
customers_data = [
    (1, 'John Smith', 'john@example.com'),
    (2, 'Lisa Brown', 'lisa@example.com'),
    (3, 'Mark Davis', 'mark@example.com'),
    (4, 'Sarah Clark', 'sarah@example.com'),
    (5, 'Michael Lee', 'michael@example.com'),
    (6, 'Emily Moore', 'emily@example.com'),
    (7, 'David Hall', 'david@example.com'),
    (8, 'Amy Adams', 'amy@example.com'),
    (9, 'Peter King', 'peter@example.com'),
    (10, 'Olivia Wood', 'olivia@example.com')
]

cursor.executemany('INSERT INTO Customers VALUES (?, ?, ?)', customers_data)

# Create the Orders table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        product TEXT,
        quantity INTEGER,
        order_date TEXT,
        FOREIGN KEY (customer_id) REFERENCES Customers (customer_id)
    )
''')

# Insert sample data into the Orders table
orders_data = [
    (1, 1, 'iPhone 12', 2, '2023-08-15'),
    (2, 3, 'Samsung TV', 1, '2023-09-02'),
    (3, 2, 'MacBook Pro', 1, '2023-10-10'),
    (4, 5, 'AirPods Pro', 3, '2023-11-18'),
    (5, 4, 'PlayStation 5', 1, '2023-12-05'),
    (6, 6, 'Kindle Paperwhite', 2, '2023-12-15'),
    (7, 7, 'Xbox Series X', 1, '2024-01-02'),
    (8, 8, 'GoPro Hero 9', 1, '2024-02-14'),
    (9, 1, 'Apple Watch SE', 1, '2024-02-28'),
    (10, 9, 'Canon EOS R', 1, '2024-03-17')
]

cursor.executemany('INSERT INTO Orders VALUES (?, ?, ?, ?, ?)', orders_data)

# Create the Products table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        product_id INTEGER PRIMARY KEY,
        name TEXT,
        price REAL
    )
''')

# Insert sample data into the Products table
products_data = [
    (1, 'iPhone 12', 899.99),
    (2, 'Samsung TV', 1499.99),
    (3, 'MacBook Pro', 1999.99),
    (4, 'AirPods Pro', 249.99),
    (5, 'PlayStation 5', 499.99),
    (6, 'Kindle Paperwhite', 129.99),
    (7, 'Xbox Series X', 599.99),
    (8, 'GoPro Hero 9', 349.99),
    (9, 'Apple Watch SE', 299.99),
    (10, 'Canon EOS R', 2499.99)
]

cursor.executemany('INSERT INTO Products VALUES (?, ?, ?)', products_data)

# Create the Categories table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Categories (
        category_id INTEGER PRIMARY KEY,
        name TEXT
    )
''')

# Insert sample data into the Categories table
categories_data = [
    (1, 'Electronics'),
    (2, 'Books'),
    (3, 'Gaming'),
    (4, 'Sports')
]

cursor.executemany('INSERT INTO Categories VALUES (?, ?)', categories_data)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Sample SQLite database with 4 tables created successfully.")