import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_title(section=None):
    section_title = f"** {section} **" if section else ""
    print(
        f"\n* WhiskersBeyond: Pet Clinic, Grooming, Hotel & Supplies *\n{section_title}",
    )
