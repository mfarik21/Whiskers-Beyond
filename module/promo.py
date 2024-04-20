from enum import Enum
from textwrap import dedent

from tabulate import tabulate

from services import promo
from utils.helper import (
    cast_to_int,
    format_currency,
    get_index,
    integer_input,
    is_valid_choice,
)


class DiscountMethod(Enum):
    AMOUNT = "amount"
    PERCENTAGE = "pecentage"


def show_promo():
    headers = [
        "#",
        "Name",
        "Code",
        "Discount Amount",
        "Discount Percentage",
        "Min Purchase",
        "Quota",
    ]

    formatted_data = [
        [
            idx,
            item["name"],
            item["code"],
            format_currency(item["discount_amount"]),
            item["discount_percentage"],
            format_currency(item["min_purchase"]),
            item["quota"],
        ]
        for idx, item in enumerate(promo, start=1)
    ]

    print(tabulate(formatted_data, headers=headers, tablefmt="simple_outline"))


def add_item():

    print(
        dedent(
            """
            What is the discount method?:
            1. By amount
            2. By percentage
        """
        )
    )
    choice = input("Enter the number corresponding to your choice: ")
    choice = cast_to_int(choice)

    if is_valid_choice(choice, DiscountMethod):
        print("Please enter item specification below: ")
        name = input("Promo Name: ")

        # Handle if promo already exists:
        while True:
            code = input("Promo Code: ")
            exists = any(d.get("code") == code.upper() for d in promo)
            if exists:
                print("Code already exists. Please input another unique code.")
            else:
                break

        if DiscountMethod(choice) == DiscountMethod.AMOUNT:
            discount_amount = integer_input("Discount Amount: ")
        else:
            discount_percentage = integer_input("Discount Percentage: ")
        min_purchase = integer_input("Minimal Purchase: ")
        quota = integer_input("Quota: ")

        promo.append(
            {
                "name": name,
                "code": code,
                "discount_amount": discount_amount,
                "discount_percentage": discount_percentage,
                "min_purchase": min_purchase,
                "quota": quota,
            }
        )
    else:
        print("Invalid choice! Please select a valid option.")


def update_quota():
    show_promo()
    num = integer_input("Enter the item number you wish to update: ", len(promo))
    quota = integer_input("Enter the new quota : ")

    promo[get_index(num)]["quota"] = quota


def delete(idx):
    del promo[idx]


def check_promo_code_valid(code):
    return any(item.get("code") == code and item.get("quota", 0) > 0 for item in promo)


def get_discounted_amount(total_bill, code):
    for item in promo:
        if item.get("code") == code:
            if "discount_amount" in item:
                return total_bill - item["discount_amount"]
            elif "discount_percentage" in item:
                return total_bill - (item["discount_percentage"] * total_bill)
    return total_bill


def apply_promo(code):
    for d in promo:
        if d.get("code") == code:
            d["quota"] -= 1
            break
