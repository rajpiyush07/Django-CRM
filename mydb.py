from collections.abc import Container  # Fix for Python 3.10+ compatibility
import mysql.connector

# Establish connection to MySQL
database = mysql.connector.connect(
    host='localhost',
    user='PIYUSH',
    passwd='PASSWORD'
)

# Prepare a cursor object
cursorObject = database.cursor()

# Create database
cursorObject.execute("CREATE DATABASE elderco")

print("All DONE!!!")
