import time
from enum import Enum
from textwrap import dedent

from modules import clinic as clinic_module
from modules import supplies as supplies_module
from utils.helper import get_index, integer_input, menu_input
from utils.interface import clear_screen, show_title


class AdminChoice(Enum):
    SHOW_SUPPLIES = 1
    ADD_SUPPLIES = 2
    UPDATE_SUPPLIES_STOCK = 3
    DELETE_SUPPLIES = 4

    SHOW_CLINIC_TREATMENT = 5
    POPULATE_CLINIC_TREATMENT = 6
    HIDE_CLINIC_TREATMENT = 7

    HOME = 0


class VisibilityChoice(Enum):
    POPULATE = "populate"
    HIDE = "hide"


def module():
    err_msg = ""
    while True:
        clear_screen()
        show_title("Admin")

        print(
            dedent(
                """
            Supplies:
            1. Show Supplies catalog
            2. Add a new item to Supplies
            3. Update an item stock in Supplies
            4. Delete an item in Supplies

            Clinic:
            5. Show Clinic Treatment
            6. Populate a treatment in Clinic
            7. Hide a treatment in Clinic

            Exit:
            0. Exit Admin Page 
        """
            )
        )

        if err_msg:
            print(err_msg)
            err_msg = ""

        choice = input("Enter the number corresponding to your choice: ")
        choice, err = menu_input(choice, AdminChoice)
        if err:
            err_msg += err
            continue

        if AdminChoice(choice) == AdminChoice.SHOW_SUPPLIES:
            supplies_module.show_catalog(show_stock=True)
            input("Enter any input to continue: ")
            continue

        elif AdminChoice(choice) == AdminChoice.ADD_SUPPLIES:
            supplies_module.add_item()

        elif AdminChoice(choice) == AdminChoice.UPDATE_SUPPLIES_STOCK:
            supplies_module.show_catalog(show_stock=True)
            num = integer_input(
                "Enter the item number you wish to update: ",
                len(supplies_module.get_supplies()),
            )
            qty = integer_input("Enter the new stock quantity: ")
            supplies_module.update_stock(get_index(num), qty)

        elif AdminChoice(choice) == AdminChoice.DELETE_SUPPLIES:
            supplies_module.show_catalog(show_stock=True)
            num = integer_input(
                "Enter the item number you wish to delete: ",
                len(supplies_module.get_supplies()),
            )
            supplies_module.delete(get_index(num))

        elif AdminChoice(choice) == AdminChoice.SHOW_CLINIC_TREATMENT:
            show_clinic_treatment()
            input("Enter any input to continue: ")
            continue

        elif AdminChoice(choice) == AdminChoice.POPULATE_CLINIC_TREATMENT:
            populate_or_hide_treatment(VisibilityChoice.POPULATE)

        elif AdminChoice(choice) == AdminChoice.HIDE_CLINIC_TREATMENT:
            populate_or_hide_treatment(VisibilityChoice.HIDE)

        elif AdminChoice(choice) == AdminChoice.HOME:
            break


def populate_or_hide_treatment(option):
    pet_kind = input_pet_kind()
    is_visible = (
        False if VisibilityChoice(option) == VisibilityChoice.POPULATE else True
    )

    treatments = clinic_module.get_treatments(pet_kind, is_visible)
    if treatments:
        clinic_module.show_treatment(pet_kind, is_visible)
        num = integer_input(
            f"Enter the treatment number you wish to {'populate' if is_visible == False else 'hide'}: "
        )
        idx = get_index(num)
        treatment_id = treatments[idx]["id"]
        clinic_module.set_visibility(pet_kind, treatment_id, not is_visible)
    else:
        print("No data")
        input("Enter any input to continue: ")


def input_pet_kind():
    print(
        dedent(
            """
            Enter the kind of pet:
            1. Cat
            2. Dog
            """
        )
    )
    while True:
        choice = input("Enter the number corresponding to your choice: ")

        choice, err = menu_input(choice, clinic_module.PetKind)
        if err:
            print(err)
            continue

        pet_kind = clinic_module.PetKind(choice).name.lower()
        return pet_kind


def show_clinic_treatment():
    pet_kind = input_pet_kind()
    clinic_module.show_treatment(pet_kind, is_visible=True)
