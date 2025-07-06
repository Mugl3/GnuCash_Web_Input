import streamlit as st
import pandas as pd
import numpy as np
import csv
import os
# import pyautogui
import datetime
import polars as pl
from streamlit_cookies_controller import CookieController
import time

pages = {
    "Home": [
        st.Page("streamlit_app.py", title="Enter new transactions"),
        # st.Page("manage_account.py", title="Manage your account"),
    ],
    "View/Edit": [
        st.Page("pages/saved_transactions.py", title="Completed Transactions"),
        st.Page("pages/saved_account_tree.py", title="Account Selections"),
        # st.Page("trial.py", title="Try it out"),
    ],
    "Resources": [
        # st.Page("saved.py", title="Learn about us"),
        # st.Page("trial.py", title="Try it out"),
        #https://docs.streamlit.io/develop/api-reference/navigation/st.navigation
    ],
}

pg=st.navigation(pages,position="top")

pg.run()