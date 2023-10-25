import pymysql

# Database Configuration
db = pymysql.connect(
    host='sql11.freesqldatabase.com',
    user='sql11653855',
    password='x2lIMdfC7C',
    port=3306
)

# Create a cursor object
cursor = db.cursor()

# Create the database
cursor.execute("CREATE DATABASE IF NOT EXISTS sql11653855")

# Use the database
cursor.execute("USE sql11653855")

# Create the table
cursor.execute("CREATE TABLE IF NOT EXISTS pastes (id INT AUTO_INCREMENT PRIMARY KEY, content TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

# Commit changes and close connection
db.commit()
cursor.close()
db.close()
