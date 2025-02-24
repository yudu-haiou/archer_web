import streamlit as st
from PIL import Image

def resize_img(file_path):
    img = Image.open(file_path)
    new_size = (350, 380)
    return img.resize(new_size, Image.LANCZOS)

st.header("My interests")
st.write("Check out some of the cool things I've made and do!")


st.subheader("Soccer")
st.write("Soccer is one of my favorite hobbies! Here's why I love it:")
st.markdown("""
- It's a great way to stay active and healthy
- I get to play with my friends and make new ones
- It teaches me teamwork and sportsmanship
- I love the excitement of scoring goals
""")

st.subheader("Soccer")
# Display video
st.video(r"imgs/archer_match.MP4")

st.write("My Achievements:")
st.markdown("""
- I won the NorCal State Cup Champion U11
- I won the local junior league tournament
- I have six gold medals and many more silver medals in soccer
- I scored 15 goals last season
- My soccer team is number 2nd in the US
""")

st.write("Norcal Soccer State Cup Champion U11")
col1, col2 = st.columns(2)
with col1:
    st.image(r"imgs/norcal_champion.jpg", caption="Norcal Soccer State Cup Champion")
with col2:
    st.video(r"imgs/norcal_champion.mp4")
    st.markdown("Award Ceremony of Norcal State Cup Champion")

st.write("My Experiences and medals")
col1, col2 = st.columns(2)
with col1:
    st.image(r"imgs/BacaFCInSpain.jpg", caption="Barca FC Summer Camp in Barcelona,Spain,Europe")
    st.image(r"imgs/MARCET.jpg", caption="Marcet soccer camp in Barcelona, Spain")
    # st.image(resize_img("imgs/ICI C'EST PARIS.jpg"), caption="PSG soccer camp in Miami")
with col2:
    st.image(r"imgs/ICI C'EST PARIS_corp.jpg", caption="PSG soccer camp in Miami")
   
    st.image(r"imgs/Medals.jpg", caption = "my medals")
    # st.image(resize_img("imgs/MARCET.jpg"), caption="Marcet soccer camp in Barcalona, Spain")

# st.write("My medals")
# st.image(r"imgs/Medals.jpg", caption = "my medals", width=300)

# Display soccer images
col1, col2 = st.columns(2)
with col1:
    st.image(r"imgs/archer_metal.JPG", caption="My tournament medals")
with col2:
    st.image(r"imgs/archer_team.JPG", caption="A photo with my team")

# Add soccer video highlights
st.video(r"imgs/archer_goal.MP4")

# Add interactive element for soccer
if st.button("Show Soccer Fun Fact"):
    st.write("Did you know? Soccer is the most popular sport in the world, with over 4 billion fans globally!")

st.subheader("First LEGO League Robotics Match")
st.write("I participated in the First LEGO League robotics match! It was an exciting experience where I got to build and program a robot to complete various challenges.")

# Display images
col1, col2 = st.columns(2)
with col1:
    st.image(r"imgs/archer_robotics.JPG", caption="My LEG0 robot team")
with col2:
    st.image(r"imgs/MyRobot.jpg", caption="My LEG0 robot")

# Add more details about the experience
st.write("Here are some highlights from our robotics match:")
st.markdown("""
- **Robot Design**: We built our robot using LEGO Mindstorms, incorporating sensors and motors to navigate the challenge field.
- **Programming**: I learned how to program our robot using block-based coding to complete specific tasks.
- **Teamwork**: Working with my teammates, we solved problems and improved our robot's performance.
- **Innovation Project**: In our innovation project, we represented our team and created slides about our robot design and our idea to help people who are in need of help in the ocean. After the competition, we won the medal for having the best innovation project!
- **Competition Day**: We competed against other teams, presenting our robot design and completing missions on the challenge field.
""")

st.image(r"imgs/InovationAward.jpg", caption="FLL Innovation Award", width=300)

# Add an interactive element
if st.button("Show Fun Fact"):
    st.write("Did you know? The First LEGO League was founded in 1998 and now involves over 320,000 children worldwide!")


st.subheader("coding achievments")
st.markdown("""
- I learned the following coding languages: Python, HTML, JavaScript, Scratch
- I created this personal portfilio website by streamlit 
- I finished my coding projects, including pong game by python, static webpage by JavaScript, etc.
""")
col1, col2, col3 = st.columns(3)
# st.subheader("coding projects: Star War, Header, RPS")
with col1:
    # st.video(r"imgs/starwar.mp4")
    st.image(r"imgs/starwar.gif", caption="Star war")
with col2:
    # st.video(r"imgs/Header.mp4")
    st.image(r"imgs/Header.gif", caption="Header")
with col3:
    # st.video(r"imgs/RPS.mp4")
    st.image(r"imgs/RPS.gif", caption="RPS")

st.video(r"imgs/rescue-screen-capture.mp4")
st.write("The purpose of this video is to show how drones can patrol the area with charging stations in the water. So then the swimmers could get saved more easily. The charging stations are powered by the ocean waves, this is environmental friendly and safe for swimmers nearby. The process starts out with drones depatched from the base. Then the make a loop to see if there is any swimmers. When on drone detects a swimmer it sends a signal to the boats nearby and the boats save the swimmer.")

# st.write("here is one of the projects I made, https://www.codesters.com/preview/ca36c58532804b4ea29e83201f9f99fd/")

