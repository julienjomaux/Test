import streamlit as st
import pandas as pd
import numpy as np
from decouple import config  # <-- Add this line

st.title("My First Streamlit App :wave:")
# Add a header and some text
st.header("A test")

stripe_link = config('STRIPE_CHECKOUT_LINK')  # Get value safely

st.markdown(
    f"""
    If you want to access all the apps of GEM Energy Analytics, please sign up following the link below. 

    Currently, the fee is 30 € per month. When the payment is done, you will receive an password that will grant you access to all apps. Every month, you will receive an email with a new password to access the apps (except if you unsubscribe). 
    Feel free to reach out at Julien.jomaux@gmail.com

    #### [Sign Up Now :metal:]({stripe_link})
    """
)
with st.form("login_form"):
    st.write("Login")
    email = st.text_input('Enter Your Email')
    password = st.text_input('Enter Your Password')
    submitted = st.form_submit_button("Login")


if submitted:
    if password == config('SECRET_PASSWORD'):
        st.session_state['logged_in'] = True
        st.text('Succesfully Logged In!')
    else:
        st.text('Incorrect, login credentials.')
        st.session_state['logged_in'] = False


if 'logged_in' in st.session_state.keys():
    if st.session_state['logged_in']:
        # Add a slider widget
        number = st.slider("Pick a number", 0, 100, 25)
        st.write(f"You selected: {number}")
        
        # Display a simple line chart with random data
        st.subheader("Random Data Chart")
        data = pd.DataFrame(
            np.random.randn(10, 2),
            columns=['col1', 'col2']
        )
        st.line_chart(data)








