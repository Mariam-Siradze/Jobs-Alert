'''Module in which the class responsible for user authentication (On Streamlint) is initialized.'''

import streamlit as st
from auth.password_utils import hash_password
from auth.users import UserManager as user

class AuthenticationApp():

    def login():
        '''Method which authenticates the user via authenticate_user method and logs the user in if the hashed passwords match'''
        st.title("Login")
        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")

        if st.button("Login", key="login_button"):
            if user.authenticate_user(username, password):
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
                st.success(f"Welcome, {username}!")
            else:
                st.error("Invalid username or password.")
    
    def signup():
        st.title("Signup")
        username = st.text_input("Create a Username", key="signup_username")
        password = st.text_input("Create a Password", type="password", key="signup_password")
        confirm_password = st.text_input("Confirm Password", type="password", key="signup_confirm_password")

        if st.button("Signup", key="signup_button"):
            if user.username_exists(username):
                st.error("Username already exists. Please choose another one.")
            elif password != confirm_password:
                st.error("Passwords do not match.")
            else:
                user.add_user(username, hash_password(password))
                st.success("Account created successfully! You can now log in.")
