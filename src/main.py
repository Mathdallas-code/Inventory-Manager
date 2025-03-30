"""
This can be used for managing stock in stores.
"""

import json
import os
import tabulate

# My module imports
from modules.itemHandler import *
from modules.funcs import *

# Setting variables
inventory = items
headers = [
    "Item",
    "Opening stock",
    "Stocks bought this month",
    "Stock Sales",
    "Closing stock",
    "Cost Price",
    "Selling Price",
    "Profit/Loss",
    "Profit/Loss per item",
]  # Set headers for tabulate table


# Used to save the json file with the value of inventory
def save_json_main():
    with open("data/inventory.json", "w") as f:
        json.dump(inventory, f, sort_keys=True, indent=4)
        f.close()


while True:
    print('-------------------------------------')
    user_input = input(
        "Commands: \n\t1 - Check inventory\n\t"
        + "2 - Add item\n\t"
        + "3 - Change property of item\n\t"
        + "4 - Delete an item\n\t"
        + "5 - Clear terminal\n\t"
        + "6 - Exit the program\n\n"
        + "  > "
    )
    inventory = items
    if user_input == "1":
        if inventory == {}:
            print("No data found!")
        else:
            save_json_main()
            data = []
            for x in inventory:
                profit_or_loss = None
                profit = 0
                if inventory[x]["cost_price"] > inventory[x]["selling_price"]:
                    profit_or_loss = "Loss"
                    profit = inventory[x]["cost_price"] - inventory[x]["selling_price"]
                elif inventory[x]["selling_price"] > inventory[x]["cost_price"]:
                    profit_or_loss = "Profit"
                    profit = inventory[x]["selling_price"] - inventory[x]["cost_price"]
                else:
                    profit_or_loss = "No profit or loss"
                    profit = "Nil"
                data.append(
                    [
                        inventory[x]["name"],
                        inventory[x]["opening_stock"],
                        inventory[x]["stocks_bought"],
                        inventory[x]["sales"],
                        inventory[x]["closing_stock"],
                        inventory[x]["cost_price"],
                        inventory[x]["selling_price"],
                        profit_or_loss,
                        profit,
                    ]
                )

            table = tabulate.tabulate(tabular_data=data, headers=headers, tablefmt="rounded_grid")
            print(table)
            print("-------------------")
            print("---- |Summary| ----")
            print("-------------------")
            total_cp = 0
            total_sp = 0
            for y in inventory:
                total_cp += inventory[y]["cost_price"] * inventory[x]["stocks_bought"]
                total_sp += inventory[y]["selling_price"] * inventory[x]["sales"]
            print(f"Total C.P: {total_cp}")
            print(f"Total S.P: {total_sp}")
            if total_sp > total_cp:
                print(f"Total profit: {total_sp - total_cp}")
            elif total_sp < total_cp:
                print(f"Total loss: {total_cp - total_sp}")
            else:
                print("No total profit or loss")

    elif user_input == "2":
        item_name = input("Enter item name: ")
        item_opening_stock = input("Enter opening stock: ")
        if not check_int(item_opening_stock):
            print("Error: Opening stock is not a number")
            continue
        else:
            item_opening_stock = int(item_opening_stock)
        item_stocks_bought = input("Enter number of stocks you bought: ")
        if not check_int(item_stocks_bought):
            print("Error: Stocks bought is not a number")
            continue
        else:
            item_stocks_bought = int(item_stocks_bought)
        item_closing_or_sales = input(
            "Do you want to write the closing-stocks(stocks bought at end of month) or sales? "
        ).lower()
        if item_closing_or_sales == "closing-stock":
            item_closing_stock = input("Enter closing stock: ")
            if not check_int(item_closing_stock):
                print("Error: Closing stock is not a number")
                continue
            else:
                item_closing_stock = int(item_closing_stock)
            item_sales = (item_opening_stock + item_stocks_bought) - item_closing_stock
        elif item_closing_or_sales == "sales":
            item_sales = input("Enter sales of the stock: ")
            if not check_int(item_sales):
                print("Error: Sales is not a number")
                continue
            else:
                item_sales = int(item_sales)
            item_closing_stock = (item_opening_stock + item_stocks_bought) - item_sales
        else:
            print("Invalid input. Please try again.")
            continue
        item_cost_price = input("Enter item cost price: ")
        if not check_float(item_cost_price):
            print("Error: Cost price is not a number")
            continue
        else:
            item_cost_price = float(item_cost_price)
        item_selling_price = input("Enter item selling price: ")
        if not check_float(item_selling_price):
            print("Error: Selling price is not a number")
            continue
        else:
            item_selling_price = float(item_selling_price)
        add_item(
            Item(
                name=item_name,
                opening_stock=item_opening_stock,
                stocks_bought=item_stocks_bought,
                closing_stock=item_closing_stock,
                sales=item_sales,
                cost_price=item_cost_price,
                selling_price=item_selling_price,
            )
        )
        save_json_main()

    elif user_input == "3":
        item_name = input("Enter item name: ")
        val_type = input(
            "Enter name of value to be changed(name, opening_stock, stocks_bought, closing_stock, sales, cost_price, selling_price; quantity): "
        ).lower()
        new_val = input("Enter new value: ")
        if val_type not in [
            "name",
            "opening_stock",
            "stocks_bought",
            "closing_stock",
            "sales",
            "cost_price",
            "selling_price",
            "quantity",
        ]:
            print("Error: Name of value is not correct")
            continue
        if val_type != "name":
            try:
                new_val = int(new_val)
            except:
                print("Error: Value is not an integer")
        print(change_val(item_name=item_name, val_type=val_type, new_val=new_val))
        save_json_main()

    elif user_input == "4":
        item_name = input("Enter name of item to deleted: ")
        remove_item(item_name=item_name)
        save_json_main()

    elif user_input == "5":
        os.system("clear" if os.name == "posix" else "cls")

    elif user_input == "6":
        print("Bye!")
        break

quit(0)
