import mysql.connector

# Perform Actions:
def CheckUserInDB(_user):
    myDB = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="personal_tool_db"
    )

    cursor = myDB.cursor()

    try:
        sql = f"SELECT user FROM users WHERE user = '{_user}'"
        cursor.execute(sql)
        result = cursor.fetchall()[0][0]

        if result == _user:
            return result
        else:
            return None
    except Exception as e:
        return None

    myDB.close()

def CheckUserPwd(_user):
    myDB = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="personal_tool_db"
    )

    cursor = myDB.cursor()

    try:
        sql = f"SELECT password FROM users WHERE user = '{_user}'"
        cursor.execute(sql)
        result = cursor.fetchall()[0][0]

        if result == _user:
            return result
        else:
            return None
    except Exception as e:
        return None

    myDB.close()
