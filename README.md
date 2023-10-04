# GnuCash_Web_Input
Project uses streamlit/python to capture transactions. These transactions are saved as files in your folder, ready for importation into GNUCash. This makes it easy to capture transactions on the go & easy recon later.
Deploy by cloning repo & cd to the folder.
Edit the password that you want in streamlit/secrets.toml
Then run: streamlit run test.py  
This will deploy your app on a webinterface with HTTP. To get HTTPS I suggest nginx reverse proxy manager or any other reverse proxy. 