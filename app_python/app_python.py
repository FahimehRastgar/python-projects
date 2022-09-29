import mysql.connector

connection_details = {
    'host': 'localhost', 
    'user': 'root', 
    'password':'00000000',
    'database': 'app_python'
}

def db_connection():

    return mysql.connector.connect(
        user = connection_details['user'], 
        password = connection_details['password'], 
        host = connection_details['host'],
        database = connection_details['database'])



def init():

    db = db_connection()

    users_cursor = db.cursor()
    users_cursor.execute("SELECT * FROM users")

    users_list = users_cursor.fetchall()

    for user in users_list:
        print(user)

    db.close()

init()