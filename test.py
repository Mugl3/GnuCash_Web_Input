import streamlit as st
import pandas as pd
import numpy as np
import csv
import os
#import pyautogui
import datetime

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

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
    if 'output_file' not in st.session_state:
        path="transaction_output.csv"
        if os.path.isfile(path):
            #print("File exists")
            with open("transaction_output.csv",'r') as file:
                data=file.read()
                st.session_state['output_file']=data
                #for row in csvreader:
                #   print(row[0])
                #  st.session_state['output_file']=st.session_state['output_file']+str(row)
                # print(row)
                    #print(st.session_state['output_file'])
        else:
            with open("transaction_output.csv",'w+',newline='') as file:
                csvreader=csv.reader(file)
                st.session_state['output_file']=''

    def get_data_to_download():
        with open("transaction_output.csv",'r') as file:
                data=file.read()
                st.session_state['output_file']=data
        return data.rstrip('\n')
    st.download_button("Download transactions",get_data_to_download(),'user_transactions.csv')

    def clicked_reset():
        #pyautogui.hotkey("ctrl","F5")
        pass
        
    def clicked():
        id=str(datetime.datetime.now()).replace(" ","")
        output_file1=f"""{id},{date},{from_account},-{price},{description}"""
        output_file2=f"""{id},{date},{to_account},{price},{description}"""
        with open("transaction_output.csv",'a') as fd:
            fd.write(output_file1)
            fd.write("\n")
            fd.write(output_file2)
            fd.write("\n")
        from_account.index=0
        to_account.index=0
        price.value=None

    def clicked_transaction_clear():
        if clear_contents_check:
            st.write('Clearing contents of transactions now')
            open("transaction_output.csv",'w').close()
    st.title('Enter new transaction')

    #Populate accounts with list of items selectable
    accounts=[]
    with open('account_tree.csv', newline='') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in datareader:
            accounts.append(row[1])

    #Create the various buttons etc on the UI
    date=st.date_input("Transaction date")
    from_account=st.selectbox('Please choose from which account', accounts,None)
    to_account=st.selectbox('Please choose to which account', accounts,None)
    price=st.number_input('Insert a $ amount')
    description=st.text_input("Please write a short transaction description")
    clicked=st.button("Save",on_click=clicked)
    reset=st.button("Reset",on_click=clicked_reset)
    clear_contents_check=st.checkbox("Clear transactions due to recon already done?")
    clear_button=st.button("Clear transactions",on_click=clicked_transaction_clear)
