import streamlit as st

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
- Won the local junior league tournament
- Scored 15 goals last season
- His soccer team is number 20th in the state
""")

st.write("My Experiences")
col1, col2 = st.columns(2)
with col1:
    st.image(r"imgs/ICI C'EST PARIS.jpg", caption="PSG soccer camp in Miami")
with col2:
    st.image(r"imgs/MARCET.jpg", caption="Marcet soccer camp in Barcalona")

# Display soccer images
col1, col2 = st.columns(2)
with col1:
    st.image(r"imgs/archer_metal.JPG", caption="My tournament medals")
with col2:
    st.image(r"imgs/archer_team.JPG", caption="A photo with his team")

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
- **Competition Day**: We competed against other teams, presenting our robot design and completing missions on the challenge field.
""")


# Add an interactive element
if st.button("Show Fun Fact"):
    st.write("Did you know? The First LEGO League was founded in 1998 and now involves over 320,000 children worldwide!")


st.subheader("coding achievment")
st.markdown("""
- learned many coding languages
- created this with streamlit 
- made a game called pong in python
- wants to be able to create a website with javascript
""")

st.video(r"imgs/rescue-screen-capture.mp4")

st.write("here is one of the projects Archer made, https://www.codesters.com/preview/ca36c58532804b4ea29e83201f9f99fd/")

