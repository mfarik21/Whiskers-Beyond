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

    invoice = get_invoice()
    for num, item in enumerate(invoice, start=1):
        formatted_row = [num] + [value for key, value in item.items() if key != "id"]
        formatted_data.append(formatted_row)

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
            # Check Supplies item to deduct stock
            filtered_treatment_list = [
                item for item in get_invoice() if item["service"] == "Supplies"
            ]
            for item in filtered_treatment_list:
                supplies.deduct_stock(item["id"], item["qty"])

            print(f"Here's your change: {change}")
            print("Thank you! Have a wonderful day!")
            option = yes_no_input("\nBack to Home: (Y/N)? ")
            if option.upper() == "Y":
                break
