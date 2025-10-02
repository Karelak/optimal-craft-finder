import json
import requests
import os
from pprint import pprint


def getallitems():
    try:
        response = requests.get(url="https://api.hypixel.net/v2/skyblock/bazaar")
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None


def getprices(dataset: dict, searchitems: list):
    if not dataset or "products" not in dataset:
        return None
    prices = {}
    for item in searchitems:
        products: dict = dataset.get("products").get(item)
        if products is None:
            print(f"Warning: Item '{item}' not found in bazaar data. Skipping.")
            continue  # Skip missing items instead of crashing
        summary: dict = products.get("quick_status")
        if summary is None:
            continue
        # Optional: Remove pprint if it's too noisy (it prints every summary)
        # pprint(summary)
        prices[item] = {
            "buyPrice": summary.get("buyPrice"),
            "sellPrice": summary.get("sellPrice"),
        }
    return prices


def mergejson(fp: str):
    merged_data = {}
    files = os.listdir(fp)
    for file in files:
        if file.endswith(".json"):
            filepath = os.path.join(fp, file)
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                merged_data[file.replace(".json", "")] = data

    with open("out.json", "w", encoding="utf-8") as outfile:
        json.dump(merged_data, outfile, indent=2)


def getforgeitems(mainfile: str = "out.json"):
    forgeitems = []
    with open(mainfile, "r", encoding="utf-8") as f:
        items: dict = json.load(f)
    for item in items.keys():
        item_data = items.get(item)
        if item_data and item_data.get("recipes") and len(item_data["recipes"]) > 0:
            if item_data["recipes"][0].get("type") == "forge":
                forgeitems.append(item)
    return forgeitems


# mergejson("C:/Users/Kaarel/Downloads/NotEnoughUpdates-REPO/items")
forgableitems: list = getforgeitems("out.json")
with open("bazaardata.json", "r") as f:
    dataset = json.load(f)
    finalset = getprices(dataset=dataset, searchitems=forgableitems)
    pprint(finalset)
