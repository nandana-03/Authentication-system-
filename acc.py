import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth

# Initialize Firebase app if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate('summarizer-c36b2-6b2b59f1f260.json')
    firebase_admin.initialize_app(cred)

def app():
    st.title("Welcome to :violet[YouTube-Summarizer]")
    choice = st.selectbox("Login/Signup", ['Login', 'Sign Up'])
    email = st.text_input('Email Address')
    password = st.text_input('Password', type='password')

    if choice == 'Login':
        if st.button("Login"):
            try:
                user = auth.get_user_by_email(email)
                st.success('Login successful!')
            except Exception as e:
                st.error(f'Login failed: {e}')
    else:
        username = st.text_input('Enter your unique username')

        if st.button('Create my account'):
            try:
                user = auth.create_user(email=email, password=password, uid=username)
                st.success('Account created successfully!')
                st.markdown('Please login using your email and password.')
                st.balloons()
            except Exception as e:
                if hasattr(e, 'code') and e.code == 'EMAIL_EXISTS':
                    st.error('Sign up failed: Email address already in use')
                else:
                    st.error(f'Sign up failed: {e}')

app()
