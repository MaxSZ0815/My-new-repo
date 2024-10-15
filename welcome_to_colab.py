import streamlit as st

# Title of the app
st.title("Full Name Generator")

# Input fields for first and last name
first_name = st.text_input("Enter your first name:")
last_name = st.text_input("Enter your last name:")

# When both fields are entered, show the full name
if first_name and last_name:
    full_name = first_name + " " + last_name
    st.write(f"Your full name is: **{full_name}**")
