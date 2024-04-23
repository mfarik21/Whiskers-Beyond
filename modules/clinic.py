from enum import Enum
from textwrap import dedent
from typing import Dict

from tabulate import tabulate

from services.clinic import clinic
from utils.helper import (
    dict_to_str,
    format_currency,
    get_index,
    integer_input,
    menu_input,
    string_input,
    yes_no_input,
)
from utils.interface import clear_screen, show_title

basket = list()


class PetKind(Enum):
    CAT = 1
    DOG = 2


class ClinicChoice(Enum):
    ADD_NEW = 1
    REMOVE = 2
    CLEAR = 3
    PROCEED = 0


def module():
    err_msg = ""
    while True:
        clear_screen()
        show_title("Pet Clinic")

        if basket:
            display_basket()

        print(
            dedent(
                """
            Options:
            1. Request a treatment
            2. Cancel a treatment
            3. Clear all treatments
            0. Proceed and back to Home 
        """
            )
        )

        if err_msg:
            print(err_msg)
            err_msg = ""

        choice = input("Enter the number corresponding to your choice: ")
        choice, err = menu_input(choice, ClinicChoice)
        if err:
            err_msg += err
            continue

        if ClinicChoice(choice) == ClinicChoice.ADD_NEW:
            checkout_treatment()

        elif ClinicChoice(choice) == ClinicChoice.REMOVE:
            num = integer_input(
                "Enter the basket number of the service you want to remove: ",
                len(basket),
            )
            if not basket:
                err_msg += "Your basket is empty! Please add item to basket first!"
            else:
                remove_from_basket(get_index(num))

        elif ClinicChoice(choice) == ClinicChoice.CLEAR:
            clear_basket()

        elif ClinicChoice(choice) == ClinicChoice.PROCEED:
            break


def checkout_treatment():
    print(
        dedent(
            """
            What kind of pet do you have?:
            1. Cat
            2. Dog
        """
        )
    )
    while True:
        choice, err = menu_input(
            input("Enter the number corresponding to your choice: "), PetKind
        )
        if err:
            print(err)
            continue

        pet_kind = PetKind.CAT if PetKind(choice) == PetKind.CAT else PetKind.DOG
        name = string_input(f"What is your {pet_kind.name.lower()}'s name?: ")
        show_treatment(pet_kind.name.lower())

        treatment_choice = integer_input(
            "Enter the treatment number needed for your pet: ",
            len(clinic[pet_kind.name.lower()]),
        )

        idx = get_index(treatment_choice)

        chosen_treatment = {
            "kind": pet_kind.name.title(),
            "name": name,
            "treatment": clinic[pet_kind.name.lower()][idx]["treatment"],
            "price": clinic[pet_kind.name.lower()][idx]["price"],
        }
        add_to_basket(chosen_treatment)
        break


def get_treatments(pet_kind, is_visible=True):
    return [item for item in clinic[pet_kind] if item["is_visible"] == is_visible]


def show_treatment(pet_kind, is_visible=True):
    # Filter treatment list based on visibility
    treatments = get_treatments(pet_kind, is_visible)

    headers = [
        "#",
        "Treatment Name",
        "Decription",
        "Price",
    ]
    formatted_data = [
        [
            idx,
            item["treatment"],
            item["desc"],
            format_currency(item["price"]),
        ]
        for idx, item in enumerate(treatments, start=1)
    ]

    print(tabulate(formatted_data, headers=headers, tablefmt="simple_outline"))


def set_visibility(pet_kind, treatment_id, visibility):
    for item in clinic[pet_kind]:
        if item.get("id") == treatment_id:
            item["is_visible"] = visibility


def display_basket():
    headers = ["#", "Kind", "Name", "Treatment Name", "Price"]
    formatted_data = [
        [idx, item["kind"], item["name"], item["treatment"], item["price"]]
        for idx, item in enumerate(basket, start=1)
    ]

    print()
    print(tabulate(formatted_data, headers=headers, tablefmt="simple_outline"))


def get_basket():
    return basket


def add_to_basket(item: Dict):
    basket.append(item)


def remove_from_basket(idx: int):
    del basket[idx]


def clear_basket():
    option = yes_no_input("Are you sure you want to clear your basket: (Y/N)? ")
    if option.upper() == "Y":
        basket.clear()


def map_basket_to_invoice():
    return [
        {
            "id": None,
            "service": "Clinic",
            "name": item["treatment"],
            "desc": dict_to_str(
                {key: value for key, value in item.items() if key in ["kind", "name"]}
            ),
            "qty": 1,
            "price": format_currency(item["price"]),
            "subtotal": format_currency(item["price"]),
        }
        for item in get_basket()
    ]


def get_total_price():
    total_price = 0
    if get_basket():
        for item in get_basket():
            total_price += item["price"]

    return total_price
