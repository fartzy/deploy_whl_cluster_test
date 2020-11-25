import argparse
import base64
import json
import os
import re
import requests
from requests.auth import HTTPBasicAuth

from databricks_cli.dbfs.api import DbfsApi, DbfsPath
from databricks_cli.sdk.api_client import ApiClient
from dotenv import load_dotenv


def main():
    ENDPOINT = od.getenv('ENDPOINT')
    TOKEN = os.getenv('TOKEN')
    DBX_USER = os.getenv('DBX_USER')
    DBX_PASSWORD = os.getenv('DBX_PASSWORD')

    headers = { 'Authorization' : 'Token ' + TOKEN }

    auth = HTTPBasicAuth(DBX_USER, DBX_PASSWORD)
    api_token_auth = (f"{DBX_USER}/token", TOKEN)

    r = requests.get(f"{ENDPOINT}/clusters/", headers=headers)
    print(r.text)

def load_env():
    path = os.path.dirname(__file__)
    dotenv_path = os.path.join(path, '../.env')
    load_dotenv(dotenv_path=dotenv_path)

if __name__ == "__main__":
    main()