from enum import Enum
from textwrap import dedent
from typing import Dict

from tabulate import tabulate

from services import supplies
from utils.helper import (
    cast_to_int,
    dict_to_str,
    format_currency,
    generate_unique_id,
    get_index,
    integer_input,
    is_valid_choice,
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

        if err_msg:
            print(err_msg)

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

        choice = input("Enter the number corresponding to your choice: ")
        choice = cast_to_int(choice)

        if is_valid_choice(choice, SuppliesChoice):

            if SuppliesChoice(choice) == SuppliesChoice.ADD_NEW:
                show_catalog()
                choice = integer_input(
                    "Enter the product number you'd like: ", len(supplies)
                )

                qty = integer_input("Enter the quantity you'd like: ")

                idx = get_index(choice)

                is_sufficient, avail_stock = check_stock_availability(idx, qty)
                if is_sufficient:
                    item = dict(supplies[idx], qty=qty)
                    add_to_basket(item)
                else:
                    err_msg = f"Insufficient stock for item {idx}. Available quantity: {avail_stock}"

            elif SuppliesChoice(choice) == SuppliesChoice.REMOVE:
                num = integer_input(
                    "Enter the basket number of the item you want to remove: ",
                    len(basket),
                )
                idx = get_index(num)
                remove_from_basket(idx)

            elif SuppliesChoice(choice) == SuppliesChoice.CLEAR:
                option = yes_no_input(
                    "Are you sure you want to clear your basket: (Y/N)?"
                )
                if option.upper() == "Y":
                    clear_basket()

            elif SuppliesChoice(choice) == SuppliesChoice.PROCEED:
                break

        else:
            print("Invalid choice! Please select a valid option.")


def show_catalog():
    headers = [
        "#",
        "Product Name",
        "Category",
        "Subcategory",
        "Type",
        "Size",
        "Price",
    ]
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
        for idx, item in enumerate(supplies, start=1)
    ]

    print(tabulate(formatted_data, headers=headers, tablefmt="simple_outline"))


def add_item():
    print("Please enter item specification below: ")
    name = input("Product Name: ")
    category = input("Category: ")
    sub_category = input("Sub Category: ")
    type = input("Type: ")
    size = input("Size: ")
    price = input("Price: ")
    stock = input("Stock: ")

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
    del basket[idx]


def clear_basket():
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
            item["quota"] -= qty
