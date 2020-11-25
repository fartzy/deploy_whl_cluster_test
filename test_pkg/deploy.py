import argparse
import base64
import json
import os
import re
import requests

from databricks_cli.dbfs.api import DbfsApi, DbfsPath
from databricks_cli.sdk.api_client import ApiClient
from dotenv import load_dotenv


def main():
    ENDPOINT = od.getenv('ENDPOINT')
    TOKEN = os.getenv('TOKEN')

    databricks_client = ApiClient(host=config.ENDPOINT, token=TOKEN)
    dbfs_client = DbfsApi(self.databricks_client)

    src_path = "~/dev/deploy_whl_cluster_test/dist/test_package-0.0.1-py3-none-any.whl"

    dbfs_client.cp(src=src_path, dst=dst_path, overwrite=True, recursive=False)


def _get_file_as_base64(path, read_mode="rb"):
    with open(path, read_mode) as wheel_handler:
        return base64.b64encode(wheel_handler.read())

def load_env():
    path = os.path.dirname(__file__)
    dotenv_path = os.path.join(path, '../.env')
    load_dotenv(dotenv_path=dotenv_path)

if __name__ = "__main__":
