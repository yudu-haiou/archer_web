import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

st.title("Hobbies")

st.subheader("Creative Writing")
st.write("Archer used to really like writing stories, but it isn't his main interest anymore. He writes many fictional stories with unreal characters. He wrote a story and published it to the inklings contest, where it got chosen for one of the best stories.")
pdf_viewer(r"./imgs/Puffin Planet - example.pdf")

st.subheader("Piano")
st.write("Archer started playing piano at an age of four. He likes songs that are happy and cheerful, not sad and gloomy. He has done 7 recitals and now he is practicing a 10 page long song.")
st.video(r"imgs/piano.mp4")

st.subheader("Swimming")
st.write("Archer first started swimming because he knew it would help with his stamina. He learned all the types of swimming and his swimming speed is under 35 sec for 25meter long swimming pool")
col1, col2 = st.columns(2)
with col1:
    st.video(r"imgs/IMG_8059.mp4")
with col2:
    st.video(r"imgs/IMG_8863.mp4")

st.subheader("Art")
st.write("Archer really likes coloring and sketching, not painting or using chalk. He likes to draw things people use in school and different types of things combined.")
col1, col2 = st.columns(2)
with col1:
    st.image(r"imgs/IMG_1076.jpg")
with col2:
    st.image(r"imgs/IMG_MopDaFloor.jpg")

st.subheader("Ping Pong")
st.write("Archer got addicted to ping pong when he watched hundreds of videos from pongfinity. Even without a real ping pong table, he makes a tiny version of it with things he has at home.")