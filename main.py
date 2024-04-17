from enum import Enum
from textwrap import dedent

from tabulate import tabulate

from module import clinic, grooming, hotel, supplies
from utils.helper import cast_to_int, dict_to_string, format_currency, is_valid_choice
from utils.interface import clear_screen, show_title

whole_basket = list()


class ServiceChoice(Enum):
    SUPPLIES = 1
    GROOMING = 2
    HOTEL = 3
    CLINIC = 4


def main():
    while True:
        clear_screen()
        show_title()
        print(
            dedent(
                """
        Select the services that best suit your needs:
        1. Supplies
        2. Grooming
        3. Hotel
        4. Clinic
        0. Exit
        """
            ),
            end="",
        )

        display_whole_basket()

        # payment

        choice = input("Enter the number corresponding to your choice: ")
        choice = cast_to_int(choice)

        if is_valid_choice(choice, ServiceChoice):
            if ServiceChoice(choice) == ServiceChoice.SUPPLIES:
                supplies.module()
            elif ServiceChoice(choice) == ServiceChoice.GROOMING:
                grooming.module()
            elif ServiceChoice(choice) == ServiceChoice.HOTEL:
                hotel.module()
            elif ServiceChoice(choice) == ServiceChoice.CLINIC:
                clinic.module()
        else:
            print("Invalid choice! Please select a valid option.")


def display_whole_basket():
    headers = [
        "#",
        "Service Type",
        "Item",
        "Description",
        "Qty",
        "Unit Price",
        "Subtotal",
    ]
    formatted_data = []

    num = 1
    if supplies.get_basket():
        for item in supplies.get_basket():
            formatted_data.append(
                [
                    num,
                    "Supplies",
                    item["name"],
                    dict_to_string(
                        {
                            key: value
                            for key, value in item.items()
                            if key in ["category", "sub_category", "type", "size"]
                        }
                    ),
                    item("qty"),
                    format_currency(item["price"]),
                    format_currency(item("qty") * item["price"]),
                ]
            )
            num += 1

    if grooming.get_basket():
        for item in grooming.get_basket():

            svc_name = item["service"]["main"]["name"]
            if "adds_on" in item["service"]:
                addson_svc = item["service"]["adds_on"]["name"]
                svc_name = f"{svc_name}, {addson_svc} (Adds On)"

            price = item["service"]["main"]["price"]
            if "adds_on" in item["service"]:
                addson_price = item["service"]["adds_on"]["price"]
                price += addson_price

            formatted_data.append(
                [
                    num,
                    "Grooming",
                    svc_name,
                    dict_to_string(
                        {
                            key: value
                            for key, value in item.items()
                            if key in ["kind", "name", "specs"]
                        }
                    ),
                    1,
                    format_currency(price),
                    format_currency(price),
                ]
            )
            num += 1

    if hotel.get_basket():
        for item in hotel.get_basket():
            formatted_data.append(
                [
                    num,
                    "Hotel",
                    f"{ item['nights'] } night(s) stays",
                    dict_to_string(
                        {
                            key: value
                            for key, value in item.items()
                            if key in ["kind", "name"]
                        }
                    ),
                    item["nights"],
                    format_currency(item["price"]),
                    format_currency(item["nights"] * item["price"]),
                ]
            )
            num += 1

    if clinic.get_basket():
        for item in clinic.get_basket():
            formatted_data.append(
                [
                    num + 1,
                    "Clinic",
                    item["treatment"],
                    dict_to_string(
                        {
                            key: value
                            for key, value in item.items()
                            if key in ["kind", "name"]
                        }
                    ),
                    1,
                    format_currency(item["price"]),
                    format_currency(item["price"]),
                ]
            )
            num += 1

    if formatted_data:
        print("Basket:")
        print(tabulate(formatted_data, headers=headers, tablefmt="simple_outline"))


def count_total_price():
    total_price = 0
    if supplies.get_basket():
        for item in supplies.get_basket():
            total_price += (item("qty") * item["price"],)

    if grooming.get_basket():
        for item in grooming.get_basket():

            price = item["service"]["main"]["price"]
            if "adds_on" in item["service"]:
                addson_price = item["service"]["adds_on"]["price"]
                price += addson_price

            total_price += total_price

    if hotel.get_basket():
        for item in hotel.get_basket():
            total_price += (item("nights") * item["price"],)

    if clinic.get_basket():
        for item in clinic.get_basket():
            total_price += item["price"]

    return total_price


if __name__ == "__main__":
    main()
