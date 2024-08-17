import string
import random
import streamlit as st


# Function to generate the password
def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special):
    if length <= 0:
        st.error("Password length must be greater than 0.")
        return ""

    # Character sets based on the options selected
    character_set = ""

    if include_uppercase:
        character_set += string.ascii_uppercase
    if include_lowercase:
        character_set += string.ascii_lowercase
    if include_numbers:
        character_set += string.digits
    if include_special:
        character_set += string.punctuation

    if not character_set:
        st.error("At least one character set must be selected.")
        return ""

    # Generating the password
    password = "".join(random.choice(character_set) for _ in range(length))
    return password


# Streamlit app layout
st.title("Password Generator")

# Input fields
length = st.number_input("Password Length:", min_value=1, value=12, step=1)
include_uppercase = st.checkbox("Include Uppercase", value=True)
include_lowercase = st.checkbox("Include Lowercase", value=True)
include_numbers = st.checkbox("Include Numbers", value=True)
include_special = st.checkbox("Include Special Characters", value=True)

# Generate button
if st.button("Generate Password"):
    password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special)

    if password:
        st.text_input("Generated Password:", value=password, key="password", disabled=True)
        st.button("Copy to Clipboard", on_click=lambda: st.session_state.password)
        st.write(f"**Generated Password:** {password}")


# Copy password to clipboard function
def copy_to_clipboard():
    st.write("Password copied to clipboard")


# Handle clipboard copy
if st.session_state.get("password"):
    st.write("Password copied to clipboard")
