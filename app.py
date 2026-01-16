import streamlit as st
import pandas as pd
import numpy as np
from decouple import config  # <-- Add this line

st.title("My First Streamlit App :wave:")

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
# Set the title of the app


# Add a header and some text
st.header("An Interactive Example &&&&&")
st.write("This simple app demonstrates a text input, a button, and a data chart.")

# Add a text input widget
user_input = st.text_input("Enter your name", "Type here...")

if st.button("Say Hello"):
    if user_input and user_input != "Type here...":
        st.success(f"Hello, {user_input}!")
    else:
        st.warning("Please enter your name.")

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
        st.markdown('## Ask Me Anything')
        question = st.text_input('Ask your question')
        if question != '':
            st.write('I drink and I know things.')
