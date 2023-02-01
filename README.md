# Basic ReadMe
This was created quickly to pull all groups and users within those groups and output to json format.


## Requirements
Python 3.9
Google OAuth 2.0 Client ID
credentials.json File

## Usage
```sh
python3.9 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
mv config_sample.cfg config.cfg
```
Update the customer_id variable in the config.cfg to match your customer id from your google admin account settings page, save the file
```sh
python group.py
```
A popup should come up, login and accept the access. This will write a token.json file to your local drive.

This will also output a csv file to the directory after you run the script.