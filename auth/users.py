'''A class that manages the users (inserting the info into the table and authentication) is initialized in this module.'''
from db.tables import create_users_table
from auth.password_utils import hash_password, verify_password
from db.db_connection import get_connection

class UserManager():
    def username_exists(username):
        '''Runs a select query and checkes whether or not a user is already installed.'''
        create_users_table()  
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cur.fetchone()
        cur.close()
        conn.close()
        return user is not None
    
    def add_user(username, hashed_password):
        '''A method which is used to insert the user data into the table'''
        create_users_table()  
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        conn.commit()
        cur.close()
        conn.close()


    def authenticate_user(username, password):
        '''Hashes the received password and checks whether or not the user input input matches the inserted data.'''
        create_users_table()  
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT password FROM users WHERE username = %s", (username,))
        stored_password = cur.fetchone()
        cur.close()
        conn.close()
        if stored_password:
            return verify_password(stored_password[0], password)
        return False