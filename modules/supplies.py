from enum import Enum
from textwrap import dedent
from typing import Dict

from tabulate import tabulate

from services.supplies import supplies
from utils.helper import (
    dict_to_str,
    format_currency,
    generate_unique_id,
    get_index,
    integer_input,
    menu_input,
    string_input,
    yes_no_input,
)
from utils.interface import clear_screen, show_title

basket = list()


class SuppliesChoice(Enum):
    ADD_NEW = 1
    REMOVE = 2
    CLEAR = 3
    PROCEED = 0


def module():
    err_msg = ""

    while True:
        clear_screen()
        show_title("Pet Supplies")

        if basket:
            display_basket()

        print(
            dedent(
                """
            Options:
            1. Add new items to basket
            2. Remove an item from basket
            3. Clear basket
            0. Proceed and back to Home 
        """
            )
        )

        if err_msg:
            print(err_msg)
            err_msg = ""

        choice = input("Enter the number corresponding to your choice: ")

        choice, err = menu_input(choice, SuppliesChoice)
        if err:
            err_msg += err
            continue

        if SuppliesChoice(choice) == SuppliesChoice.ADD_NEW:
            show_catalog()
            choice = integer_input(
                "Enter the product number you'd like: ", len(supplies)
            )

            while True:
                qty = integer_input("Enter the quantity you'd like: ")

                idx = get_index(choice)

                is_sufficient, avail_stock = check_stock_availability(idx, qty)
                if is_sufficient:
                    item = dict(supplies[idx], qty=qty)
                    add_to_basket(item)
                    break
                else:
                    print(
                        f"Insufficient stock for item {choice}. Available quantity: {avail_stock}"
                    )

        elif SuppliesChoice(choice) == SuppliesChoice.REMOVE:
            num = integer_input(
                "Enter the basket number of the item you want to remove: ",
                len(basket),
            )

            if not basket:
                err_msg += "Your basket is empty! Please add item to basket first!"
            else:
                remove_from_basket(get_index(num))

        elif SuppliesChoice(choice) == SuppliesChoice.CLEAR:
            clear_basket()

        elif SuppliesChoice(choice) == SuppliesChoice.PROCEED:
            break


def get_supplies():
    return supplies


def show_catalog(show_stock=False):
    headers = [
        "#",
        "Product Name",
        "Category",
        "Subcategory",
        "Type",
        "Size",
        "Price",
    ] + (["Stock"] if show_stock else [])

    formatted_data = [
        [
            idx,
            item["name"],
            item["category"],
            item["sub_category"],
            item["type"],
            item["size"],
            format_currency(item["price"]),
        ]
        + ([item["stock"]] if show_stock else [])
        for idx, item in enumerate(supplies, start=1)
    ]

    print(tabulate(formatted_data, headers=headers, tablefmt="simple_outline"))


def add_item():
    print("Please enter item specification below: ")
    name = string_input("Product Name: ")
    category = string_input("Category: ")
    sub_category = string_input("Sub Category: ")
    type = string_input("Type: ")
    size = string_input("Size: ")
    price = integer_input("Price: ")
    stock = integer_input("Stock: ")

    supplies.append(
        {
            "id": generate_unique_id(),
            "name": name,
            "category": category,
            "sub_category": sub_category,
            "type": type,
            "size": size,
            "stock": stock,
            "price": price,
        }
    )


def update_stock(idx, qty):
    supplies[idx]["stock"] = qty


def delete(idx):
    del supplies[idx]


def display_basket():
    headers = ["#", "Product Name", "Qty", "Unit Price", "Subtotal"]
    formatted_data = [
        [idx, item["name"], item["qty"], item["price"], item["qty"] * item["price"]]
        for idx, item in enumerate(basket, start=1)
    ]

    print()
    print(tabulate(formatted_data, headers=headers, tablefmt="simple_outline"))


def check_stock_availability(idx, qty):
    if idx >= 0 and idx <= len(supplies):
        available_stock = supplies[idx].get("stock")
        return (available_stock >= qty, available_stock)


def get_basket():
    return basket


def add_to_basket(item: Dict):

    # Handling adding item that already exists
    list_item = [item["name"] for item in basket]
    if item["name"] in list_item:
        for cart_item in basket:
            if cart_item["name"] == item["name"]:
                cart_item["qty"] += item["qty"]
                return

    basket.append(item)


def remove_from_basket(idx: int):
    if idx < len(basket):
        del basket[idx]
    else:
        print("Please enter correct number from basket!")


def clear_basket():
    option = yes_no_input("Are you sure you want to clear your basket: (Y/N)? ")
    if option.upper() == "Y":
        basket.clear()


def map_basket_to_invoice():
    return [
        {
            "id": item["id"],
            "service": "Supplies",
            "name": item["name"],
            "desc": dict_to_str(
                {
                    key: value
                    for key, value in item.items()
                    if key in ["category", "sub_category", "type", "size"]
                }
            ),
            "qty": item["qty"],
            "price": format_currency(item["price"]),
            "subtotal": format_currency(item["qty"] * item["price"]),
        }
        for item in get_basket()
    ]


def get_total_price():
    total_price = 0
    if get_basket():
        for item in get_basket():
            total_price += item["qty"] * item["price"]
    return total_price


def deduct_stock(id, qty):
    for item in supplies:
        if item.get("id") == id:
            item["stock"] -= qty
