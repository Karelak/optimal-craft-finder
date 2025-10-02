import json
import requests


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


def getprices(items):
    if not items or "products" not in items:
        return None
    prices = {}
    for product_id, product_data in items["products"].items():
        quick_status = product_data.get("quick_status", {})
        prices[product_id] = {
            "productId": quick_status.get("productId"),
            "sellPrice": quick_status.get("sellPrice"),
            "buyPrice": quick_status.get("buyPrice"),
        }
    return prices


items = getallitems()
getprices(items)
