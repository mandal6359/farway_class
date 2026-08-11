import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard

def teacher_screen():
    style_background_dashboard()
    style_base_layout()

    

    if 'teacher_login_type' in st.session_state or st.session_state.teacher_login_type=="login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()





def teacher_screen_login():
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()

    st.header('Login using password', text_alignment='center')
    st.space()
    st.space()


    teacher_username = st.text_input("Enter username", placeholder='Piyush')

    teacher_pass = st.text_input("Enter password", type='password', placeholder="Enter password")

    st.divider()

    btnc1, btnc2 = st.columns(2)

    with btnc1:
        if st.button('Login', icon=':material/passkey:', shortcut='control+enter', width='stretch'):
            if login_teacher(teacher_username, teacher_pass):
                st.toast("welcome back!", icon="👋")
                import time
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid username and password combo")

    with btnc2:
        if st.button('Register Instead', type="primary", icon=':material/passkey:', width='stretch'):
            st.session_state.teacher_login_type = 'register'

    footer_dashboard()


def teacher_screen_register():
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go Back to Home", type='primary', key='loginbackbtn', shortcut='control+backspace'):
            st.session_state['login_type'] = None
            st.rerun()




    st.header("LOGIN USING PASSWORD",  text_alignment='center')

    st.space()
    st.space()

    

    teacher_username = st.text_input("Enter your username", placeholder="Piyush")

    teacher_name = st.text_input("Enter name", placeholder="Piyush Mandal")

    teacher_pass = st.text_input("Enter your password", type="password", placeholder="Enter Password")

    teacher_pass_confirm = st.text_input("Confirm your password", type="password", placeholder="Confirm Password")

    st.divider()

    btnc1, btnc2 = st.columns(2)

    with btnc1:
        st.button("Register Now", icon=":material/passkey:", shortcut="control+enter", width="stretch")

    with btnc2:
        if st.button("Login Instead", type ='primary', icon=":material/passkey:", width="stretch"):
            st.session_state.teacher_login_type = "login"
            st.rerun()


    footer_dashboard()


