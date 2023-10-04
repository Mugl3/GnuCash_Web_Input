# GnuCash_Web_Input
Project uses streamlit/python to capture transactions. These transactions are saved as files in your folder, ready for importation into GNUCash. This makes it easy to capture transactions on the go & easy recon later. This project is not designed to be multi-user friendly at the moment. 


Example of the basic login screen - using password from secrets.toml
![image](https://github.com/Mugl3/GnuCash_Web_Input/assets/65000615/6a7ea632-f589-48cc-92a0-9f7e940acd99)

Example of homepage
![image](https://github.com/Mugl3/GnuCash_Web_Input/assets/65000615/ed9164cd-8c57-4541-bc4a-09ab987279fb)

**Installation**
1. Clone repo & cd to the project folder.
2. Edit the password that you want in streamlit/secrets.toml

Export account tree from GNUCash:
1. Click file, export account tree to CSV
2. Name your file account_tree.csv and save it in the project root folder.

Then run: streamlit run test.py  
This will deploy your app on a webinterface with HTTP. To get HTTPS I suggest nginx reverse proxy manager or any other reverse proxy. 
Alternatively you can follow the streamlit examples to deploy this app for free on their community servers.
See https://streamlit.io/cloud for more details

There are options for docker too, I will investigate this in the future. 
   
**Usage instructions**
1. To add transactions simply use the GUI. Once the transaction is ready, hit save.
2. In the future when you are ready to import your transactions into GNUCash download the CSV & import into GNUCash (File, Import, Import transactions from CSV) using the import tool (you can save the import template to save time).
   See below for suggested importing template
![image](https://github.com/Mugl3/GnuCash_Web_Input/assets/65000615/f7ec017a-1e24-4dfb-a1c5-78f67dedec63)

4. When you have downloaded your transactions clear the current log by clicking the checkbox and hitting clear. 
5. You can start recording transactions again.

**ToDo**
Add cookies support for seamless login - https://discuss.streamlit.io/t/cookies-support-in-streamlit/16144
Deploy via docker
