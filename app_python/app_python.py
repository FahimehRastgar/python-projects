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


def add_user():
    
    person = {
        "first_name": "",
        "last_name": "",
        "email": "",
        "postcode": "",
        "city": "",
        "company_id": ""
                
        }
        
    person['first_name'] = input("""---- Adding a new user ----

Please fill in these information: 

Name: """)

    person["last_name"] = input("Last name: ")
    person["email"] = input("Email: ")
    person["postcode"] = input("Postcode: ")
    person["city"] = input("City: ")
    person["company_id"] = input("Company ID: ")


    da = db_connection()
    cursor = da.cursor() 

    ins_qry = "INSERT INTO Users ({columns}) VALUES {values};" .format(
            tablename = "Users",
            columns=', '.join(person.keys()),
            values=tuple(person.values())
        )
    
    x = cursor.execute(ins_qry)
    da.commit()
    da.close()


def list_users():
    db = db_connection()
    users_cursor = db.cursor()


    users_cursor.execute("SELECT count(id) as total_users from Users")
    users_count = users_cursor.fetchone()
    total = users_count[0]
    print(f" ---- {total} Users ----")

    
    users_cursor.execute("SELECT * FROM users")

    users_list = users_cursor.fetchall()

    for user in users_list:
    
        print (f"""-- ID: {user[0]}
Name: {user[1]}
Last name: {user[2]}
Email: {user[3]}
Postcode: {user[4]}
City: {user[5]}
Company ID: {user[6]}
        """)

    db.close()


def init():

    users_option = input("""What would you like to do?

    (v) : View all users
    (a) : Add a new user


What is your command? """)

    if users_option == "v":
        list_users()

    elif users_option == "a":
        add_user()

init()