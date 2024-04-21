from tabulate import tabulate

from module import clinic, grooming, hotel, supplies
from utils.helper import format_currency, integer_input, yes_no_input


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
