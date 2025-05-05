# Contents of /streamlit-app/streamlit-app/app/main.py

import streamlit as st

def main():
    st.title("Welcome to fAIndHouse")
    
    st.sidebar.header("User Input")
    
    # Slider for selecting a number
    number = st.sidebar.slider("Select a number", 0, 100, 50)
    
    # Text input for user name
    name = st.sidebar.text_input("Enter your name", "Guest")
    
    # Button to submit the input
    if st.sidebar.button("Submit"):
        st.write(f"Hello, {name}! You selected the number {number}.")
    
    # Display the selected number
    st.write("You selected:", number)

if __name__ == "__main__":
    main()