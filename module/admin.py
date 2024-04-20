from enum import Enum
from textwrap import dedent

from module import clinic as clinic_module
from module import promo as promo_module
from module import supplies as supplies_module
from utils.helper import cast_to_int, get_index, integer_input, is_valid_choice
from utils.interface import clear_screen, show_title


class AdminChoice(Enum):
    ADD_SUPPLIES = 1
    UPDATE_SUPPLIES_STOCK = 2
    DELETE_SUPPLIES = 3

    POPULATE_CLINIC_TREATMENT = 4
    HIDE_CLINIC_TREATMENT = 5

    SHOW_PROMO_LIST = 6
    ADD_PROMO = 7
    UPDATE_PROMO_QUOTA = 8
    DELETE_PROMO = 9

    HOME = 0


class VisibilityChoice(Enum):
    POPULATE = "populate"
    HIDE = "hide"


def module():
    while True:
        clear_screen()
        show_title("Admin")

        print(
            dedent(
                """
            Supplies:
            1. Add new items to Supplies
            2. Update an item stock in Supplies
            3. Delete an item in Supplies

            Clinic:
            4. Populate a treatment in Clinic
            5. Hide a treatment in Clinic

            Promo Codes:
            6. Show promo list
            7. Add a promo codes
            8. Update promo codes quota
            9. Delete a promo codes

            Exit:
            0. Exit Admin Page 
        """
            )
        )

        choice = input("Enter the number corresponding to your choice: ")
        choice = cast_to_int(choice)

        if is_valid_choice(choice, AdminChoice):
            if AdminChoice(choice) == AdminChoice.ADD_SUPPLIES:
                supplies_module.add_item()

            elif AdminChoice(choice) == AdminChoice.UPDATE_SUPPLIES_STOCK:
                supplies_module.show_catalog()
                num = integer_input("Enter the item number you wish to update: ")
                qty = integer_input("Enter the new stock quantity: ")
                supplies_module.update_stock(get_index(num), qty)

            elif AdminChoice(choice) == AdminChoice.DELETE_SUPPLIES:
                num = integer_input("Enter the item number you wish to delete: ")
                supplies_module.delete(get_index(num))

            elif AdminChoice(choice) == AdminChoice.POPULATE_CLINIC_TREATMENT:
                populate_or_hide_treatment(VisibilityChoice.POPULATE)

            elif AdminChoice(choice) == AdminChoice.HIDE_CLINIC_TREATMENT:
                populate_or_hide_treatment(VisibilityChoice.HIDE)

            elif AdminChoice(choice) == AdminChoice.SHOW_PROMO_LIST:
                promo_module.show_promo()

            elif AdminChoice(choice) == AdminChoice.ADD_PROMO:
                promo_module.add_item()

            elif AdminChoice(choice) == AdminChoice.UPDATE_PROMO_QUOTA:
                promo_module.update_quota()

            elif AdminChoice(choice) == AdminChoice.DELETE_PROMO:
                promo_module.delete()

        else:
            print("Invalid choice! Please select a valid option.")


def populate_or_hide_treatment(option):
    print(
        dedent(
            """
            Enter pet kind?:
            1. Cat
            2. Dog
        """
        )
    )
    choice = input("Enter the number corresponding to your choice: ")
    choice = cast_to_int(choice)
    pet_kind = (
        clinic_module.PetKind.CAT
        if clinic_module.PetKind(choice) == clinic_module.PetKind.CAT
        else clinic_module.PetKind.DOG
    ).name.lower()

    if is_valid_choice(choice, clinic_module.PetKind):

        visibility = (
            False if VisibilityChoice(option) == VisibilityChoice.POPULATE else True
        )

        clinic_module.show_treatment(pet_kind, visibility)
        num = integer_input("Enter the treatment number you wish to populate: ")
        clinic_module.set_visibility(pet_kind, get_index(num), not visibility)
    else:
        print("Invalid choice! Please select a valid option.")
