import pymysql

# Database Configuration
db = pymysql.connect(
    host='sql11.freesqldatabase.com',
    user='sql11653855',
    password='x2lIMdfC7C',
    database='sql11653855',
    port=3306
)

# Create a cursor object
cursor = db.cursor()

# Check if the table exists
cursor.execute("SHOW TABLES LIKE 'pastes'")
table_exists = cursor.fetchone() is not None

if table_exists:
    print("Table 'pastes' exists.")
else:
    print("Table 'pastes' does not exist.")

cursor.close()
db.close()
