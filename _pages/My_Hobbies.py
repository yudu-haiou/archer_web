import streamlit as st

st.header("My Hobbies")
st.write("These are some of the things I love to do in my free time:")
hobbies = ["Soccer", "Reading", "Video Games", "Drawing"]
for hobby in hobbies:
    st.write(f"- {hobby}")        