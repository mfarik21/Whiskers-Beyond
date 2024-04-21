from enum import Enum
from textwrap import dedent

from modules import admin, clinic, grooming, hotel, supplies
from modules.payment import get_invoice, payment, print_invoice
from utils.helper import menu_input
from utils.interface import clear_screen, show_title


class ServiceChoice(Enum):
    SUPPLIES = 1
    GROOMING = 2
    HOTEL = 3
    CLINIC = 4
    INVOICE = 5
    PAYMENT = 6
    EXIT = 0


ADMIN_SECRET_MENU = "***"


def main():
    err_msg = ""
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

        if err_msg:
            print(err_msg)
            err_msg = ""

        choice = input("Enter the number corresponding to your choice: ")

        if choice == ADMIN_SECRET_MENU:
            admin.module()
            continue

        choice, err = menu_input(choice, ServiceChoice)
        if err:
            err_msg += err
            continue

        service_modules = {
            ServiceChoice.SUPPLIES: supplies.module,
            ServiceChoice.GROOMING: grooming.module,
            ServiceChoice.HOTEL: hotel.module,
            ServiceChoice.CLINIC: clinic.module,
            ServiceChoice.INVOICE: print_invoice,
            ServiceChoice.PAYMENT: payment,
            ServiceChoice.EXIT: exit,
        }

        service_function = service_modules.get(ServiceChoice(choice))
        if service_function:
            service_function()


if __name__ == "__main__":
    main()
