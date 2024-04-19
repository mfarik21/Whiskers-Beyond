from enum import Enum
from textwrap import dedent
from typing import Dict

from tabulate import tabulate

from services import clinic
from utils.helper import (
    cast_to_int,
    dict_to_str,
    format_currency,
    get_index,
    get_int_input,
    is_valid_choice,
)
from utils.interface import clear_screen, show_title

basket = list()


class PetChoice(Enum):
    CAT = 1
    DOG = 2


class ClinicChoice(Enum):
    ADD_NEW = 1
    REMOVE = 2
    CLEAR = 3
    PROCEED = 0


def module():
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

        choice = input("Enter the number corresponding to your choice: ")
        choice = cast_to_int(choice)

        if is_valid_choice(choice, ClinicChoice):
            if ClinicChoice(choice) == ClinicChoice.ADD_NEW:
                checkout_treatment()

            elif ClinicChoice(choice) == ClinicChoice.REMOVE:
                num = get_int_input(
                    "Enter the basket number of the service you want to remove: ",
                    len(basket),
                )
                idx = get_index(num)
                remove_from_basket(idx)

            elif ClinicChoice(choice) == ClinicChoice.CLEAR:
                option = input("Are you sure you want to clear your basket: (Y/N)? ")
                if option.upper() == "Y":
                    clear_basket()

            elif ClinicChoice(choice) == ClinicChoice.PROCEED:
                break
        else:
            print("Invalid choice! Please select a valid option.")


def checkout_treatment():
    print(
        dedent(
            """
            What furry friend do you have?:
            1. Cat
            2. Dog
        """
        )
    )
    choice = input("Enter the number corresponding to your choice: ")
    choice = cast_to_int(choice)

    if is_valid_choice(choice, PetChoice):
        pet_kind = (
            PetChoice.CAT if PetChoice(choice) == PetChoice.CAT else PetChoice.DOG
        )
        name = input(f"What is your {pet_kind.name.lower()}'s name?: ")
        show_treatment(pet_kind.name.lower())

        choice = get_int_input(
            "Enter the treatment number needed for your pet: ",
            len(clinic[pet_kind.name.lower()]),
        )

        idx = get_index(choice)

        chosen_treatment = {
            "kind": pet_kind.name.title(),
            "name": name,
            "treatment": clinic[pet_kind.name.lower()][idx]["treatment"],
            "price": clinic[pet_kind.name.lower()][idx]["price"],
        }
        add_to_basket(chosen_treatment)


def show_treatment(pet_kind):
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
        for idx, item in enumerate(clinic[pet_kind], start=1)
    ]

    print(tabulate(formatted_data, headers=headers, tablefmt="simple_outline"))


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
    basket.clear()


def map_basket_to_invoice():
    return [
        [
            "Clinic",
            item["treatment"],
            dict_to_str(
                {key: value for key, value in item.items() if key in ["kind", "name"]}
            ),
            1,
            format_currency(item["price"]),
            format_currency(item["price"]),
        ]
        for item in get_basket()
    ]


def get_total_price():
    total_price = 0
    if get_basket():
        for item in get_basket():
            total_price += item["price"]

    return total_price
