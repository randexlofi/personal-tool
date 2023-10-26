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
def CheckUserInDB(_user):
    try:
        sql = f"SELECT user FROM users WHERE user = '{_user}'"
        cursor.execute(sql)
        result = cursor.fetchall()[0][0]

        if result == _user:
            return result
        else:
            return None
    except Exception as e:
        print('Error: ', e)



myDB.close()