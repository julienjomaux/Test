import streamlit as st
import pandas as pd
import numpy as np
from decouple import config  # <-- Add this line

st.title("My First Streamlit App :wave:")
# Add a header and some text
st.header("An Interactive Example")
st.write("This simple app demonstrates a text input, a button, and a data chart.")

stripe_link = config('STRIPE_CHECKOUT_LINK')  # Get value safely

st.markdown(
    f"""
    Chat with Tyrion Lannister to advise you on:
    - Office Politics
    - War Strategy
    - The Targaryens

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








