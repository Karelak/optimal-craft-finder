import requests
import json
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("api_key")


def getallitems(api_key: str):
    url = "https://api.hypixel.net/v2/resources/skyblock/items"
    headers = {"API-Key": api_key}
    response = requests.get(url=url, headers=headers)
    return response.json()


def getbazaaritems(api_key: str):
    url = "https://api.hypixel.net/v2/skyblock/bazaar"
    headers = {"API-Key": api_key}
    response = requests.get(url=url, headers=headers)
    return response.json


data: dict = getallitems(api_key)
test = []
for item in data.get("items"):
    test.append(item["id"])
pprint(test)
