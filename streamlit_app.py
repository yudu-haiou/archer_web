import streamlit as st
from streamlit_option_menu import option_menu

# def main():
st.set_page_config(
    page_title="Archer's Portfolio",
    page_icon="desktop_computer",
    layout="wide",
    initial_sidebar_state="auto",
)
with st.sidebar:
    choose = option_menu(
        "Archer Xiang",
        [
            "Lucy",
            "About Me",
            "Education",
            "Projects",
            "Hobbies",
            "Contact",
        ],
        icons=[
            "robot",
            "person fill",
            "book half",
            "clipboard",
            "trophy fill",
            "envelope",
        ],
        menu_icon="mortarboard",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#0D1117"},
            "icon": {"color": "darkorange", "font-size": "20px"},
            "nav-link": {
                "font-size": "17px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#1F2937",
            },
            "nav-link-selected": {"background-color": "#A41117"},
        },
    )
    st.markdown(
    "<a href='mailto:alexwatersword@gmail.com'><img src='https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png' width='40'></a>"
    "</div>",
    unsafe_allow_html=True,
)

pages = {
    "Lucy": "_pages/home.py",
    "About Me": "_pages/About_Me.py",
    "Education": "_pages/My_Education.py",
    "Projects": "_pages/My_Projects.py",
    "Hobbies": "_pages/My_Hobbies.py",
    "Contact": "_pages/Contact.py",
}

# Dynamically load the selected page
page_file = pages.get(choose)
if page_file:
    with open(page_file, encoding="utf-8") as file:
        exec(file.read())

# if __name__ == "__main__":
#     main()