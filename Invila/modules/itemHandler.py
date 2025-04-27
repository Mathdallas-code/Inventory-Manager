import json
from modules.item import Item

with open("Invila/data/inventory.json") as f:
    items: dict = json.load(f)


def save_json():
    with open("Invila/data/inventory.json", "w") as f:
        json.dump(items, f, sort_keys=True, indent=4)
        f.close()


def add_item(item: Item):
    if item.name in items.keys():
        return "Item already exists"
    else:
        items[item.name] = {
            "name": item.name,
            "opening_stock": item.opening_stock,
            "stocks_bought": item.stocks_bought,
            "closing_stock": item.closing_stock,
            "sales": item.sales,
            "cost_price": float(item.cost_price),
            "selling_price": float(item.selling_price),
        }
    save_json()


def view_items() -> dict:
    return items


def change_val(item_name: str, val_type: str, new_val):
    try:
        items[item_name][val_type] = new_val
        print(f"{val_type.capitalize()} of item changed!")
        save_json()
    except:
        return "No item exists"
    save_json()


def remove_item(item_name: str):
    try:
        del items[item_name]
        save_json()
        return "Item deleted!"
    except:
        return "No item exists"
