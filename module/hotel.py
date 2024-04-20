from enum import Enum
from textwrap import dedent
from typing import Dict

from tabulate import tabulate

from services import hotel
from utils.helper import (
    cast_to_int,
    dict_to_str,
    format_currency,
    get_index,
    integer_input,
    is_valid_choice,
    yes_no_input,
)
from utils.interface import clear_screen, show_title

basket = list()


class PetKind(Enum):
    CAT = 1
    DOG = 2


class CatSpecs(Enum):
    LESS_EQ_5KG = "weight <= 5kg"
    MORE_5KG = "weight > 5kg"


class DogSpecs(Enum):
    S = "small"
    M = "medium"
    L = "large"
    XL = "extra large"


class HotelChoice(Enum):
    ADD_NEW = 1
    REMOVE = 2
    CLEAR = 3
    PROCEED = 0


def module():
    while True:
        clear_screen()
        show_title("Pet Hotel")

        show_price_list()

        print(
            dedent(
                """
            Facilities:
            - FREE pickup*
            - FREE grooming*
            - Indoor Cage with Air Conditioner
            - Pics and Vids Update
            - Food and water bowls are washed twice a day.
            - Toilet cleaned daily.

            * Free pickup within the Batam Center area, complimentary
            grooming for stays of at least 5 nights.
            """
            )
        )

        if basket:
            display_basket()

        print(
            dedent(
                """
            Options:
            1. Add a revervation
            2. Cancel a reservation
            3. Clear reservation
            0. Proceed and back to Home
        """
            )
        )

        choice = input("Enter the number corresponding to your choice: ")
        choice = cast_to_int(choice)

        if is_valid_choice(choice, HotelChoice):
            if HotelChoice(choice) == HotelChoice.ADD_NEW:
                book_stays()

            elif HotelChoice(choice) == HotelChoice.REMOVE:
                num = integer_input(
                    "Enter the basket number of the service you want to remove: ",
                    len(basket),
                )
                idx = get_index(num)
                remove_from_basket(idx)

            elif HotelChoice(choice) == HotelChoice.CLEAR:
                option = yes_no_input(
                    "Are you sure you want to clear your basket: (Y/N)? "
                )
                if option.upper() == "Y":
                    clear_basket()

            elif HotelChoice(choice) == HotelChoice.PROCEED:
                break
        else:
            print("Invalid choice! Please select a valid option.")


def book_stays():
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

    if is_valid_choice(choice, PetKind):
        pet_kind = PetKind.CAT if PetKind(choice) == PetKind.CAT else PetKind.DOG
        name = input(f"What is your {pet_kind.name.lower()}'s name?: ")

        nights = integer_input("How many nights will your pet stay? ")

        if pet_kind == PetKind.CAT:
            weight = int(input("How much does your cat weigh (in kg)? "))
            spec_type = get_pet_specs(PetKind.CAT, weight=weight)
            spec_value = f"{weight}kg"
        else:
            size = input(
                "Enter the dog's size (small/medium/large/extra large | S/M/L/XL): "
            )
            spec_type = get_pet_specs(PetKind.DOG, size=size.upper())
            spec_value = spec_type.title()

        price = hotel[pet_kind.name.lower()][spec_type]

        reservation = {
            "kind": pet_kind.name.title(),
            "name": name,
            "nights": nights,
            "specs": {"weight" if pet_kind == PetKind.CAT else "size": spec_value},
            "price": price,
        }

        add_to_basket(reservation)
    else:
        print("Invalid choice! Please select a valid option.")


def show_price_list():

    headers = ["#", "Kind", "Specs", "Price"]
    formatted_data = []

    for num, (kind, prices) in enumerate(hotel.items(), start=1):
        for idx, (specs, price) in enumerate(prices.items()):
            kind_value = kind if idx == 0 else None
            formatted_data.append(
                [
                    num if idx == 0 else None,
                    kind_value,
                    specs,
                    format_currency(price),
                ]
            )
        if num < len(hotel):
            formatted_data.append([])

    print("Price List: ")
    print(tabulate(formatted_data, headers=headers, tablefmt="simple_outline"))


def get_pet_specs(type: Enum, **kwargs):
    if type == PetKind.CAT:
        weight = kwargs["weight"]
        return CatSpecs.LESS_EQ_5KG.value if weight <= 5 else CatSpecs.MORE_5KG.value
    elif type == PetKind.DOG:
        for specs in DogSpecs:
            if specs.name == kwargs["size"]:
                return specs.value


def display_basket():
    headers = ["#", "Kind", "Name", "Night(s)", "Specs", "Price", "Subtotal"]

    formatted_data = [
        [
            idx,
            item["kind"],
            item["name"],
            item["nights"],
            item["specs"],
            format_currency(item["price"]),
            format_currency(item["nights"] * item["price"]),
        ]
        for idx, item in enumerate(basket, start=1)
    ]

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
            "Hotel",
            f"{ item['nights'] } night(s) stays",
            dict_to_str(
                {key: value for key, value in item.items() if key in ["kind", "name"]}
            ),
            item["nights"],
            format_currency(item["price"]),
            format_currency(item["nights"] * item["price"]),
        ]
        for item in get_basket()
    ]


def get_total_price():
    total_price = 0
    for item in get_basket():
        total_price += item["nights"] * item["price"]
    return total_price
