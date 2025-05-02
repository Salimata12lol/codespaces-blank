import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect("banking_system.db")
cursor = conn.cursor()

# Create Accounts table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Accounts (
    account_id INTEGER PRIMARY KEY ,
    name TEXT NOT NULL,
    account_number TEXT UNIQUE NOT NULL,
    account_type TEXT NOT NULL,
    balance REAL DEFAULT,
    status TEXT DEFAULT 'Active'
);
""")

# Create Transactions table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Transactions (
    transaction_id INTEGER PRIMARY KEY,
    account_number TEXT NOT NULL,
    transaction_type TEXT NOT NULL,
    amount REAL NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_number) REFERENCES Accounts(account_number)
);
""")

# Commit changes and close connection
conn.commit()
conn.close()

print(" Database and tables created successfully.")
 



