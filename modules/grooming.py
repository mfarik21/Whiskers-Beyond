from enum import Enum
from textwrap import dedent
from typing import Dict

from tabulate import tabulate

from services.grooming import grooming
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


class ServiceType(Enum):
    MAIN = "main"
    ADDS_ON = "adds_on"


class CatSpecs(Enum):
    LESS_EQ_5KG = "weight <= 5kg"
    MORE_5KG = "weight > 5kg"


class DogSpecs(Enum):
    S = "small"
    M = "medium"
    L = "large"
    XL = "extra_large"


class GroomingChoice(Enum):
    ADD_NEW = 1
    REMOVE = 2
    CLEAR = 3
    PROCEED = 0


def module():
    err_msg = ""
    while True:
        clear_screen()
        show_title("Pet Grooming")

        if basket:
            display_basket()

        print(
            dedent(
                """
            Options:
            1. Checkout a service
            2. Remove a service from basket
            3. Clear basket
            0. Proceed and back to Home 
        """
            )
        )

        if err_msg:
            print(err_msg)
            err_msg = ""

        choice = input("Enter the number corresponding to your choice: ")
        choice, err = menu_input(choice, GroomingChoice)
        if err:
            err_msg += err
            continue

        if GroomingChoice(choice) == GroomingChoice.ADD_NEW:
            checkout_service()

        elif GroomingChoice(choice) == GroomingChoice.REMOVE:
            num = integer_input(
                "Enter the basket number of the service you want to remove: ",
                len(basket),
            )
            if not basket:
                err_msg += "Your basket is empty! Please add item to basket first!"
            else:
                remove_from_basket(get_index(num))

        elif GroomingChoice(choice) == GroomingChoice.CLEAR:
            clear_basket()

        elif GroomingChoice(choice) == GroomingChoice.PROCEED:
            break


def checkout_service():
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

        if pet_kind == PetKind.CAT:
            weight = integer_input("How much does your cat weigh (in kg)? ")
            spec_type = get_pet_specs(PetKind.CAT, weight=weight)
            spec_value = f"{weight}kg"
        else:
            while True:
                size = input(
                    "Enter the dog's size (small/medium/large/extra large | S/M/L/XL): "
                ).upper()
                if size not in ["S", "M", "L", "XL"]:
                    print("Please input a valid dog's size.")
                    continue
                else:
                    spec_type = get_pet_specs(PetKind.DOG, size=size)
                    spec_value = spec_type.title()
                    break

        chosen_service = {
            "kind": pet_kind.name.title(),
            "name": name,
            "specs": {"weight" if pet_kind == PetKind.CAT else "size": spec_value},
            "service": {},
        }

        show_services(pet_kind, ServiceType.MAIN.value, spec_type)

        prod_num = integer_input(
            "Enter the product number you'd like: ",
            len(grooming[pet_kind.name.lower()][ServiceType.MAIN.value][spec_type]),
        )
        idx = get_index(prod_num)
        chosen_service["service"]["main"] = grooming[pet_kind.name.lower()][
            ServiceType.MAIN.value
        ][spec_type][idx]

        option = yes_no_input("Do you want to add an additional service? (Y/N): ")
        if option.upper() == "Y":
            print("Add-ons: ")
            show_services(pet_kind, ServiceType.ADDS_ON.value, spec_type)
            prod_num = integer_input(
                "Enter the product number you'd like: ",
                len(
                    grooming[pet_kind.name.lower()][ServiceType.ADDS_ON.value][
                        spec_type
                    ]
                ),
            )
            idx = get_index(prod_num)
            chosen_service["service"]["adds_on"] = grooming[pet_kind.name.lower()][
                ServiceType.ADDS_ON.value
            ][spec_type][idx]

        add_to_basket(chosen_service)
        break


def show_services(pet_choice, service_type, specs):

    if pet_choice == PetKind.CAT:
        filtered_grooming_list = grooming["cat"][service_type][specs]

    elif pet_choice == PetKind.DOG:
        filtered_grooming_list = grooming["dog"][service_type][specs]

    headers = ["#", "Service Name", "Price"]
    formatted_data = [
        [idx, item["name"], format_currency(item["price"])]
        for idx, item in enumerate(filtered_grooming_list, start=1)
    ]

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
    headers = ["#", "Kind", "Name", "Specs", "Service Name", "Description", "Price"]
    formatted_data = []

    for idx, item in enumerate(basket, start=1):
        main_svc = [
            idx,
            item["kind"],
            item["name"],
            dict_to_str(item["specs"]),
            item["service"]["main"]["name"],
            "Main",
            item["service"]["main"]["price"],
        ]
        formatted_data.append(main_svc)
        if "adds_on" in item["service"]:
            addson_svc = [
                None,
                None,
                None,
                None,
                item["service"]["adds_on"]["name"],
                "Additional",
                item["service"]["adds_on"]["price"],
            ]

            formatted_data.append(addson_svc)

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
    output = []

    for item in get_basket():
        svc_name = item["service"]["main"]["name"]
        price = item["service"]["main"]["price"]

        if "adds_on" in item["service"]:
            addson_svc = item["service"]["adds_on"]["name"]
            addson_price = item["service"]["adds_on"]["price"]
            svc_name = f"{svc_name}, {addson_svc} (Adds On)"
            price += addson_price

        output.append(
            {
                "id": None,
                "service": "Grooming",
                "name": svc_name,
                "desc": dict_to_str(
                    {
                        key: value
                        for key, value in item.items()
                        if key in ["kind", "name", "specs"]
                    }
                ),
                "qty": 1,
                "price": format_currency(price),
                "subtotal": format_currency(price),
            }
        )

    return output


def get_total_price():
    total_price = 0
    for item in get_basket():
        price = item["service"]["main"]["price"]
        if "adds_on" in item["service"]:
            addson_price = item["service"]["adds_on"]["price"]
            price += addson_price

        total_price += price

    return total_price
