from enum import Enum
from textwrap import dedent

from tabulate import tabulate

from module import clinic, grooming, hotel, supplies
from utils.helper import (
    cast_to_int,
    format_currency,
    integer_input,
    is_valid_choice,
    yes_no_input,
)
from utils.interface import clear_screen, show_title


class ServiceChoice(Enum):
    SUPPLIES = 1
    GROOMING = 2
    HOTEL = 3
    CLINIC = 4
    INVOICE = 5
    PAYMENT = 6


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
                """
            ),
            end="",
        )

        if get_invoice():
            print(
                dedent(
                    """
                    5. Print Invoice
                    6. Payment
                    """
                ),
                end="",
            )

        print("0. Exit\n")

        choice = integer_input(
            "Enter the number corresponding to your choice: ", len(ServiceChoice)
        )
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
            elif ServiceChoice(choice) == ServiceChoice.INVOICE:
                print_invoice()
                option = yes_no_input("Do you want to continue to payment: (Y/N)? ")
                if option.upper() == "Y":
                    payment()

                else:
                    continue
            elif ServiceChoice(choice) == ServiceChoice.PAYMENT:
                payment()

        else:
            print("Invalid choice! Please select a valid option.")


def get_invoice():
    invoice = []

    if supplies.get_basket():
        invoice.extend(supplies.map_basket_to_invoice())

    if grooming.get_basket():
        invoice.extend(grooming.map_basket_to_invoice())

    if hotel.get_basket():
        invoice.extend(hotel.map_basket_to_invoice())

    if clinic.get_basket():
        invoice.extend(clinic.map_basket_to_invoice())

    return invoice


def print_invoice():
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
    formatted_data = [[num] + arr[:] for num, arr in enumerate(get_invoice(), start=1)]

    print("Invoice:")
    print(tabulate(formatted_data, headers=headers, tablefmt="simple_outline"))


def count_total_price():
    total_price = 0
    total_price += supplies.get_total_price()
    total_price += grooming.get_total_price()
    total_price += hotel.get_total_price()
    total_price += clinic.get_total_price()

    return total_price


def payment():
    while True:
        total = count_total_price()
        print(f"Your total purchase : {format_currency(total)}")
        money = integer_input("Please enter the amount of money? ")
        change = money - total

        if money < total:
            print(
                f"Oops! It looks like your money isn't enough. You need {total - money} more. Please enter the correct amount!"
            )

        else:
            print(f"Here's your change: {change}")
            print("Thank you! Have a wonderful day!")
            option = yes_no_input("\nBack to Home: (Y/N)? ")
            if option.upper() == "Y":
                break


if __name__ == "__main__":
    main()
