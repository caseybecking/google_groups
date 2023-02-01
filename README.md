# Google Groups and Users
This was created quickly to pull all groups and users within those groups and output to csv format.


## Requirements
- Python 3.9
- Google OAuth 2.0 Client ID
- credentials.json File

You can follow this quick start guide to help as well - [Google Pyhton Quickstart](https://developers.google.com/docs/api/quickstart/python)

## Install
```sh
mv config_sample.cfg config.cfg
python3.9 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
Update the customer_id variable in the config.cfg to match your customer id from your google admin account settings page, save the file
```sh
python group.py
```
A popup should come up, login and accept the access. This will write a token.json file to your local drive.

## Output
This will also output a csv file to the directory after you run the script.