import uuid
from enum import Enum
from typing import Dict


def cast_to_int(input_str):
    try:
        return int(input_str)
    except ValueError:
        print("Please input a valid number!")
        return None


def menu_input(choice: str, choices: Enum) -> tuple[int, str]:
    err_msg = "Invalid choice! Please select a valid option."
    try:
        choice_int = int(choice)
        if choices(choice_int) in choices:
            return choice_int, ""
        else:
            return None, err_msg
    except ValueError:
        return None, err_msg


def is_valid_choice(choice: int, choices: Enum) -> bool:
    try:
        return choices(choice) in choices
    except (ValueError, TypeError):
        return False


def integer_input(prompt: str, maximum: int = None):
    while True:
        user_input = input(prompt)
        if not user_input.isdigit():
            print("Invalid choice! Please select a valid number.")
            continue

        user_input = int(user_input)
        if user_input <= 0:
            print("Invalid choice! Please select a positive number.")
            continue

        if maximum and not 1 <= user_input <= maximum:
            if maximum > 1:
                print(
                    f"Invalid choice! Please select a number between 1 and {maximum}."
                )
            else:
                print(f"Invalid choice! Please select a number.")
            continue

        return user_input


def string_input(prompt: str):
    while True:
        user_input = input(prompt)
        if not user_input or not user_input.strip():
            print("Invalid choice! Please enter a non-empty text.")
            continue

        return user_input


def yes_no_input(prompt):
    while True:
        user_input = input(prompt).strip().upper()
        if user_input in ["Y", "N"]:
            return user_input
        else:
            print("Invalid choice! Please enter either Y or N.")


def is_valid_num_input(num: int, max: int = None) -> bool:
    if max:
        return num > 0 and num <= max
    else:
        return num > 0


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


def generate_unique_id(length=8):
    # Generate a UUID and convert it to a hexadecimal string
    uuid_str = uuid.uuid4().hex
    # Return the first 'length' characters of the hexadecimal string
    return uuid_str[:length]
