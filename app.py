import streamlit as st
import pandas as pd
import numpy as np

st.title("My First Streamlit App 👋")
st.markdown(
        f"""
        Chat with Tyrion Lannister to advise you on:
        - Office Politics
        - War Strategy
        - The Targaryens


        #### [Sign Up Now 🤘🏻]({config('STRIPE_CHECKOUT_LINK')})
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
