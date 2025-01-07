import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

st.title("Hobbies")

st.subheader("Creative Writing")
st.write("I used to really like writing stories, but it isn't my main interest anymore. I write many fictional stories with unreal characters. I wrote a story and published it to the inklings contest, where it got chosen for one of the best stories.")
pdf_viewer(r"./imgs/Puffin Planet - example.pdf")


# with st.popover("Open popover", use_container_width=True):
#     pdf_viewer(r"./imgs/Puffin Planet - example.pdf", key="second pdf")

st.subheader("Piano")
st.write("I started playing piano at an age of four. I like songs that are happy and cheerful, not sad and gloomy. I've done 7 recitals and now I am practicing a 10 page long song.")
st.video(r"imgs/piano.mp4")

st.subheader("Swimming")
st.write("I first started swimming because I knew it would help with my stamina. I learned all the types of swimming and my swimming speed is under 35 sec for 25meter long swimming pool")
col1, col2 = st.columns(2)
with col1:
    st.video(r"imgs/IMG_8059.mp4")
with col2:
    st.video(r"imgs/IMG_8863.mp4")

st.subheader("Art")
st.write("I really likes coloring and sketching, not painting or using chalk. I like to draw things people use in school and different types of things combined.")
col1, col2 = st.columns(2)
with col1:
    st.image(r"imgs/IMG_1076.jpg")
with col2:
    st.image(r"imgs/IMG_MopDaFloor.jpg")

st.subheader("Ping Pong")
st.write("I got addicted to ping pong when I watched hundreds of videos from pongfinity. Even without a real ping pong table, I made a tiny version of it with things I have at home.")