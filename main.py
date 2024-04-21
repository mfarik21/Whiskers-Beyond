from enum import Enum
from textwrap import dedent

from module import clinic, grooming, hotel, supplies
from module.payment import get_invoice, payment, print_invoice
from utils.helper import cast_to_int, integer_input, is_valid_choice, yes_no_input
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


if __name__ == "__main__":
    main()
