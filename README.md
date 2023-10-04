# GnuCash_Web_Input
Project uses streamlit/python to capture transactions. These transactions are saved as files in your folder, ready for importation into GNUCash. This makes it easy to capture transactions on the go & easy recon later.
Deploy by cloning repo & cd to the folder.
Edit the password that you want in streamlit/secrets.toml
Export your GNUCash account tree and replace the included account tree with this file
Then run: streamlit run test.py  
This will deploy your app on a webinterface with HTTP. To get HTTPS I suggest nginx reverse proxy manager or any other reverse proxy. 
Alternatively you can follow the streamlit examples to deploy this app for free on their community servers.

Example of the basic login screen - using password from secrets.toml
![image](https://github.com/Mugl3/GnuCash_Web_Input/assets/65000615/01148cd6-fa85-426b-960f-d63b036584da)

Example of homepage
![image](https://github.com/Mugl3/GnuCash_Web_Input/assets/65000615/6ed1f2c3-50b3-4be6-879e-cdad3f3dd2d1)

**Usage instructions**
1. To add transactions simply use the GUI. Once the transaction is ready, hit save.
2. In the future when you are ready to import your transactions into GNUCash download the CSV & import into GNUCash using the import tool (you can save the import template to save time).
3. When you have downloaded your transactions clear the current log by clicking the checkbox and hitting clear. 
4. You can start recording transactions again.
