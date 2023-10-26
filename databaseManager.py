import mysql.connector

# Connect to your MySQL Database
myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="personal_tool_db"
)

cursor = myDB.cursor()

# Perform Actions:


myDB.close()