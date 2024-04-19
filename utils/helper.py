from enum import Enum
from typing import Dict


def cast_to_int(input_str):
    try:
        return int(input_str)
    except ValueError:
        print("Please input a valid number!")
        return None


def is_valid_choice(choice: int, choices: Enum) -> bool:
    try:
        return choices(choice) in choices
    except (ValueError, TypeError):
        return False


def get_int_input(prompt: str, maximum: int = None):
    while True:
        try:
            user_input = int(input(prompt))

            if maximum:
                if 1 <= user_input <= maximum:
                    return user_input
                else:
                    print(
                        f"Invalid choice! Please select a number between 1 and {maximum}."
                    )
            else:
                return user_input

        except ValueError:
            print("Invalid choice! Please select a valid number.")


def get_yes_no_input(prompt):
    while True:
        user_input = input(prompt).strip().upper()
        if user_input in ["Y", "N"]:
            return user_input
        else:
            print("Invalid choice! Please enter either Y or N.")


def is_valid_num_input(num: int, len: int) -> bool:
    return num > 0 and num <= len


def is_valid_qty_input(qty: int) -> bool:
    try:
        return int(qty) > 0
    except ValueError:
        return False


def get_index(num: int) -> bool:
    return num - 1


def format_currency(amount: int) -> str:
    formatted_amount = "{:,.2f}".format(amount).replace(",", ".")
    last_dot_index = formatted_amount.rfind(".")

    if last_dot_index != -1:
        formatted_amount = (
            formatted_amount[:last_dot_index]
            + ","
            + formatted_amount[last_dot_index + 1 :]
        )

    return "Rp " + formatted_amount


def dict_to_str(dict: Dict):
    return ", ".join(f"{key}: {value}" for key, value in dict.items())
