# GnuCash_Web_Input
Project uses streamlit/python to capture transactions. These transactions are saved as files in your folder, ready for importation into GNUCash. This makes it easy to capture transactions on the go & easy recon later.


Example of the basic login screen - using password from secrets.toml
![image](https://github.com/Mugl3/GnuCash_Web_Input/assets/65000615/01148cd6-fa85-426b-960f-d63b036584da)

Example of homepage
![image](https://github.com/Mugl3/GnuCash_Web_Input/assets/65000615/6ed1f2c3-50b3-4be6-879e-cdad3f3dd2d1)

**Installation**
Clone repo & cd to the project folder.
1. 
Edit the password that you want in streamlit/secrets.toml

Export account tree from GNUCash:
1. Click file, export account tree to CSV
   ![image](https://github.com/Mugl3/GnuCash_Web_Input/assets/65000615/bf125620-39a6-4b82-a736-144b55ac6d91)
2. Name your file account_tree.csv and save it in the project root folder.

Then run: streamlit run test.py  
This will deploy your app on a webinterface with HTTP. To get HTTPS I suggest nginx reverse proxy manager or any other reverse proxy. 
Alternatively you can follow the streamlit examples to deploy this app for free on their community servers.
https://streamlit.io/cloud

There is options for docker too, I will investigate this in the future. 
   
**Usage instructions**
1. To add transactions simply use the GUI. Once the transaction is ready, hit save.
2. In the future when you are ready to import your transactions into GNUCash download the CSV & import into GNUCash (File, Import, Import transactions from CSV) using the import tool (you can save the import template to save time).
   See below for suggested importing template
   ![image](https://github.com/Mugl3/GnuCash_Web_Input/assets/65000615/4a7a6c2c-91c3-46a8-a3c8-fed8fa9c21cd)
 
4. When you have downloaded your transactions clear the current log by clicking the checkbox and hitting clear. 
5. You can start recording transactions again.
