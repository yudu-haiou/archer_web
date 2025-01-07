import streamlit as st
col1, col2 = st.columns(2)
with col1:
    st.header("About Me")
    st.write("Here are some things about me:")
    st.markdown("""
    - I'm 10 years old
    - My favorite subject in school is Classics(it is also known as history)
    - I play competitive soccer
    - I like to put effort in making things look better
    - I like to do graphs and linear equations in math
    - I like to do coding and understand new coding languages
    - I like to decorate our house during holidays
    - I like to read non-fictional books
    - I published a story called Puffin Planet in Inklings Book 2024
    """)

with col2:
    st.image(r"imgs/Inklings Book 2024.jpg")

