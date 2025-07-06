import streamlit as st
import pandas as pd
import numpy as np
from streamlit_cookies_controller import CookieController
controller = CookieController()
def check_password():
    """Returns `True` if the user had the correct password."""
    cookie = controller.get('device_previously_logged_in')
    # print(cookie)
    if cookie=='True':
        return True
    
    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
            #Write a cookie to auth this user going forward
            try:
                controller.remove('device_previously_logged_in')
            except:
                print('Device has no previously logged in cookie. Thus not removing it. ')
            controller.set('device_previously_logged_in', 'True')
        else:
            st.session_state["password_correct"] = False
            #Write a cookie to auth this user going forward
            controller.set('device_previously_logged_in', 'False')
    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True
    
if check_password():
    df = pd.read_csv('account_tree.csv')

    st.dataframe(df)  # Same as st.write(df)