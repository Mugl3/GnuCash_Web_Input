import streamlit as st
import pandas as pd
import numpy as np
import csv
import os
import pyautogui
import datetime
import polars as pl
from streamlit_cookies_controller import CookieController


controller = CookieController()

# # # Set a cookie
# # controller.set('cookie_name', 'testing')

# # # Get all cookies
# cookies = controller.getAll()
# print(cookies)

# # # Get a cookie
# cookie = controller.get('device_previously_logged_in')
# print(cookie)

# # # Remove a cookie
# # controller.remove('cookie_name')

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
        st.session_state['from_accounts']=pldata.select('Account Name')
        st.session_state['to_accounts']=pldata.select('Account Name')
        st.session_state['key_to_tx_description']=None
        # pyautogui.hotkey("ctrl","F5")

    def clicked():
        id=str(datetime.datetime.now()).replace(" ","")
        #Grab the full account details from the smaller user inputs
        # from_account_full=pldata.filter(pl.col("Type")==from_account_type,pl.col("Account Name")==from_account).select("Full Account Name")
        # print(from_account_full)
        output_file1=f"""{id},{date},{st.session_state["from_account_full"]},-{price},{description}"""
        output_file2=f"""{id},{date},{st.session_state["to_account_full"]},{price},{description}"""
        with open("transaction_output.csv",'a') as fd:
            fd.write(output_file1)
            fd.write("\n")
            fd.write(output_file2)
            fd.write("\n")

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

    #Initialise the account selections
    from_accounts=accounts

    data=pd.read_csv('account_tree.csv')
    accounts_type=data['Type'].unique()
    accounts_type.sort()

    pldata=pl.read_csv('account_tree.csv')
    # print(pldata)
    if 'from_accounts' not in st.session_state:
        st.session_state['from_accounts']=pldata.select('Account Name')
    if 'to_accounts' not in st.session_state:
        st.session_state['to_accounts']=pldata.select('Account Name')
    if 'from_account_full' not in st.session_state:
        st.session_state['from_account_full']=None
    if 'to_account_full' not in st.session_state:
        st.session_state['to_account_full']=None

    def update_accounts(from_or_to):
        """
        Update the list of available account to select, based on the selection made in the account type (from or to accounts okay)
        Returns the new list of accounts to select
        """
        # print('From account type: ',from_account_type)
        if from_or_to=='key_from_account_type':
            #Update from selections
            if from_or_to not in st.session_state:
                print(f"{from_or_to} not in session state")
                pass
            else:
                # print(f'Session state from_or_to variable {from_or_to}: ',st.session_state[from_or_to])
                st.session_state['from_accounts']=pldata.filter(pl.col("Type")==st.session_state[from_or_to]).select("Account Name")
                # print("\nSuccessfully updated from accounts")
                # print(st.session_state['from_accounts'])
                
                return st.session_state['from_accounts']
        elif from_or_to=='key_to_account_type':
            #Update to account selections
            if from_or_to not in st.session_state:
                print(f"{from_or_to} not in session state")
                pass
            else:
                # print(f'Session state from_or_to variable {from_or_to}: ',st.session_state[from_or_to])
                st.session_state['to_accounts']=pldata.filter(pl.col("Type")==st.session_state[from_or_to]).select("Account Name")
                # print("\nSuccessfully updated from accounts")
                # print(st.session_state['to_accounts'])
                
                return st.session_state['to_accounts']

    #Update from textbox  
    # print(f'\nUpdating From Details below. The input is {from_account}, or values of this input is {from_account.values()}')
    # try:
    if 'key_from_account' in st.session_state:
        from_account_full=pldata.filter(pl.col("Type")==st.session_state['key_from_account_type'],pl.col("Account Name")==st.session_state['key_from_account']).select("Full Account Name")
        if len(from_account_full)>0:
            # print(from_account_full.rows(named=True)[0]['Full Account Name'])
            st.session_state['from_account_full']=from_account_full.rows(named=True)[0]['Full Account Name']

    if 'key_to_account' in st.session_state:
        from_account_full=pldata.filter(pl.col("Type")==st.session_state['key_to_account_type'],pl.col("Account Name")==st.session_state['key_to_account']).select("Full Account Name")
        if len(from_account_full)>0:
            # print(from_account_full.rows(named=True)[0]['Full Account Name'])
            st.session_state['to_account_full']=from_account_full.rows(named=True)[0]['Full Account Name']

    #Create the various buttons etc on the UI
    date=st.date_input("Transaction date",key='key_date_input')
    from_account_type=st.selectbox('Please choose from which account type', options=accounts_type,key='key_from_account_type',on_change=update_accounts, kwargs={'from_or_to':'key_from_account_type'})
    from_account=st.selectbox('Please choose from which account', options=st.session_state['from_accounts'],key='key_from_account')
    st.text(st.session_state['from_account_full'], help='Full account details that will be used')
    to_account_type=st.selectbox('Please choose to which account type', options=accounts_type,key='key_to_account_type',on_change=update_accounts, kwargs={'from_or_to':'key_to_account_type'})
    to_account=st.selectbox('Please choose to which account', options=st.session_state['to_accounts'],key='key_to_account')
    st.text(st.session_state['to_account_full'], help='Full account details that will be used')
    price=st.number_input('Insert a $ amount',key='key_number_input')
    description=st.text_input("Please write a short transaction description",value=None,key='key_to_tx_description')
    clicked=st.button("Save",on_click=clicked)
    reset=st.button("Reset",on_click=clicked_reset)
    clear_contents_check=st.checkbox("Delete saved transactions due to GNU Cash recon already done?")
    clear_button=st.button("Delete Saved transactions",on_click=clicked_transaction_clear)