role = ["admin", "customer"]
main_menu = ["Supplies", "Grooming", "Clinic", "Hotel"]


grooming = {
    "cat": {
        "main": {
            "weight <= 5kg": [
                {"name": "Dry Grooming", "price": 30000},
                {"name": "Basic Grooming", "price": 50000},
                {
                    "name": "Basic Grooming with Anti-Lice/Anti-Fungal Treatment",
                    "price": 75000,
                },
                {"name": "Complete Grooming", "price": 85000},
            ],
            "weight > 5kg": [
                {"name": "Dry Grooming", "price": 40000},
                {"name": "Basic Grooming", "price": 80000},
                {
                    "name": "Basic Grooming with Anti-Lice/Anti-Fungal Treatment",
                    "price": 110000,
                },
                {"name": "Complete Grooming", "price": 120000},
            ],
        },
        "adds_on": {
            "weight <= 5kg": [
                {"name": "Shaving", "price": 85000},
                {"name": "Brushing & Teeth Cleaning", "price": 25000},
                {
                    "name": "Skin Treatment",
                    "price": 90000,
                },
            ],
            "weight > 5kg": [
                {"name": "Shaving", "price": 150000},
                {"name": "Brushing & Teeth Cleaning", "price": 25000},
                {
                    "name": "Skin Treatment",
                    "price": 125000,
                },
            ],
        },
    },
    "dog": {
        "main": {
            "small": [
                {"name": "Dry Grooming", "price": 50000},
                {"name": "Basic Grooming", "price": 80000},
                {
                    "name": "Basic Grooming with Anti-Lice/Anti-Fungal Treatment",
                    "price": 105000,
                },
                {"name": "Complete Grooming", "price": 120000},
            ],
            "medium": [
                {"name": "Dry Grooming", "price": 75000},
                {"name": "Basic Grooming", "price": 100000},
                {
                    "name": "Basic Grooming with Anti-Lice/Anti-Fungal Treatment",
                    "price": 135000,
                },
                {"name": "Complete Grooming", "price": 150000},
            ],
            "large": [
                {"name": "Dry Grooming", "price": 120000},
                {"name": "Basic Grooming", "price": 150000},
                {
                    "name": "Basic Grooming with Anti-Lice/Anti-Fungal Treatment",
                    "price": 190000,
                },
                {"name": "Complete Grooming", "price": 205000},
            ],
            "extra_large": [
                {"name": "Dry Grooming", "price": 130000},
                {"name": "Basic Grooming", "price": 175000},
                {
                    "name": "Basic Grooming with Anti-Lice/Anti-Fungal Treatment",
                    "price": 220000,
                },
                {"name": "Complete Grooming", "price": 240000},
            ],
        },
        "adds_on": {
            "small": [
                {"name": "Shaving", "price": 185000},
                {"name": "Brushing & Teeth Cleaning", "price": 30000},
                {
                    "name": "Skin Treatment",
                    "price": 120000,
                },
            ],
            "medium": [
                {"name": "Shaving", "price": 205000},
                {"name": "Brushing & Teeth Cleaning", "price": 30000},
                {
                    "name": "Skin Treatment",
                    "price": 150000,
                },
            ],
            "large": [
                {"name": "Shaving", "price": 250000},
                {"name": "Brushing & Teeth Cleaning", "price": 35000},
                {
                    "name": "Skin Treatment",
                    "price": 205000,
                },
            ],
            "extra_large": [
                {"name": "Shaving", "price": 300000},
                {"name": "Brushing & Teeth Cleaning", "price": 35000},
                {
                    "name": "Skin Treatment",
                    "price": 240000,
                },
            ],
        },
    },
}


hotel = {
    "cat": {"weight <= 5kg": 35000, "weight > 5kg": 65000},
    "dog": {"small": 45000, "medium": 65000, "large": 85000, "extra_large": 105000},
}


clinic = {
    "cat": [
        {"treatment": "Cat Neutering", "desc": "", "price": 300000, "unit": ""},
        {"treatment": "Doctor's Consultation", "desc": "", "price": 250000, "unit": ""},
        {"treatment": "USG", "desc": "", "price": 120000, "unit": ""},
        {"treatment": "Cat Minor Surgery", "desc": "", "price": 350000, "unit": ""},
        {"treatment": "Cat Major Surgery", "desc": "", "price": 600000, "unit": ""},
        {
            "treatment": "Tricat Vaccination",
            "desc": "For Feline panleukopenia, Feline rhinotracheitis, Feline calicivirus",
            "price": 250000,
            "unit": "",
        },
        {
            "treatment": "Tetracat Vaccination",
            "desc": "For Feline panleukopenia, Feline rhinotracheitis, Feline calicivirus, Chlamydia",
            "price": 210000,
            "unit": "",
        },
    ],
    "dog": [
        {"treatment": "Dog Neutering", "desc": "", "price": 2000000, "unit": ""},
        {"treatment": "Doctor's Consultation", "desc": "", "price": 250000, "unit": ""},
        {"treatment": "USG", "desc": "", "price": 120000, "unit": ""},
        {
            "treatment": "Dog Mijor Surgery",
            "desc": "",
            "price": 900000,
            "unit": "",
        },
        {
            "treatment": "Dog Major Surgery",
            "desc": "",
            "price": 1500000,
            "unit": "",
        },
        {
            "treatment": "DP Vaccination",
            "desc": "For Distemper and Parvovirus",
            "price": 200000,
            "unit": "",
        },
        {
            "treatment": "PiBr Vaccination",
            "desc": "For Parainfluenza dan Bordetella",
            "price": 1500000,
            "unit": "",
        },
        {
            "treatment": "DHLPI Vaccination",
            "desc": "For Distemper, Hepatitis, Leptospirosis, Parvovirus, dan Rabies 2",
            "price": 225000,
            "unit": "",
        },
        {
            "treatment": "Rabies Vaccination",
            "desc": "For Ra",
            "price": 1500000,
            "unit": "",
        },
    ],
}


supplies = [
    {
        "name": "Royal Canin Kitten, Dry Food 400gr",
        "desc": "",
        "category": "Cat Food",
        "sub_category": "Kitten Food",
        "type": "Dry Food",
        "size": "400gr",
        "price": 78000,
        "stock": 10,
    },
    {
        "name": "Royal Canin Kitten, Dry Food 2kg",
        "desc": "",
        "category": "Cat Food",
        "sub_category": "Kitten Food",
        "type": "Dry Food",
        "size": "2kg",
        "price": 348000,
        "stock": 10,
    },
    {
        "name": "Royal Canin Mother & Baby Cat, Dry Food 400gr",
        "desc": "Specifically for mothers during pregnancy and lactation, and their kittens (age 1 to 4 months) during weaning.",
        "category": "Cat Food",
        "sub_category": "Mother & Baby Cat Food",
        "type": "Dry Food",
        "size": "400gr",
        "price": 74000,
        "stock": 10,
    },
    {
        "name": "Royal Canin Mother & Baby Cat, Dry Food 2kg",
        "desc": "",
        "category": "Cat Food",
        "sub_category": "Mother & Baby Cat Food",
        "type": "Dry Food",
        "size": "2kg",
        "price": 335000,
        "stock": 10,
    },
    {
        "name": "Whiskas Junior Repack, Kitten Dry Food 500gr",
        "desc": "",
        "category": "Cat Food",
        "sub_category": "Kitten Food",
        "type": "Dry Food",
        "size": "500gr",
        "price": 27000,
        "stock": 10,
    },
    {
        "name": "Whiskas Junior Repack, Kitten Dry Food 1kg",
        "desc": "",
        "category": "Cat Food",
        "sub_category": "Kitten Food",
        "type": "Dry Food",
        "size": "1kg",
        "price": 55000,
        "stock": 10,
    },
    {
        "name": "Whiskas Wet Food Tuna, 400gr",
        "desc": "",
        "category": "Cat Food",
        "sub_category": "Kitten Food",
        "type": "Wet Food",
        "size": "400gr",
        "price": 25000,
        "stock": 10,
    },
    {
        "name": "Whiskas Ocean Fish Repack 1kg",
        "desc": "",
        "category": "Cat Food",
        "sub_category": "Adult Cat Food",
        "type": "Dry Food",
        "size": "1kg",
        "price": 54000,
        "stock": 10,
    },
    {
        "name": "Royal Canin Mini Puppy, Dry Food 2kg",
        "desc": "",
        "category": "Dog Food",
        "sub_category": "Mini Puppy Dog Food",
        "type": "Dry Food",
        "size": "2kg",
        "price": 285000,
        "stock": 10,
    },
    {
        "name": "Royal Canin Mini Puppy, Dry Food 4kg",
        "desc": "",
        "category": "Dog Food",
        "sub_category": "Mini Puppy Dog Food",
        "type": "Dry Food",
        "size": "2kg",
        "price": 510000,
        "stock": 10,
    },
    {
        "name": "Royal Canin Medium Puppy, Dry Food 4kg",
        "desc": "",
        "category": "Dog Food",
        "sub_category": "Medium Puppy Dog Food",
        "type": "Dry Food",
        "size": "4kg",
        "price": 470000,
        "stock": 10,
    },
    {
        "name": "Royal Canin Medium Puppy Pouch, Wet Food 140gr",
        "desc": "",
        "category": "Dog Food",
        "sub_category": "Medium Puppy Dog Food",
        "type": "Wet Food",
        "size": "140gr",
        "price": 25000,
        "stock": 10,
    },
    {
        "name": "Royal Canin Maxi Puppy, Dry Food 4kg",
        "desc": "",
        "category": "Dog Food",
        "sub_category": "Maxi Puppy Dog Food",
        "type": "Dry Food",
        "size": "4kg",
        "price": 460000,
        "stock": 10,
    },
    {
        "name": "Royal Canin Maxi Puppy Pouch, Wet Food 140gr",
        "desc": "",
        "category": "Dog Food",
        "sub_category": "Maxi Puppy Dog Food",
        "type": "Wet Food",
        "size": "140gr",
        "price": 25000,
        "stock": 10,
    },
    {
        "name": "Royal Canin Mini Adult, Dry Food 4kg",
        "desc": "For adult small breed dogs (weighing between 1 and 10 kg) - over 10 months old.",
        "category": "Dog Food",
        "sub_category": "Mini Adult Dog Food",
        "type": "Dry Food",
        "size": "4kg",
        "price": 480000,
        "stock": 10,
    },
    {
        "name": "Royal Canin Medium Adult, Dry Food 4kg",
        "desc": "For adult medium-sized breed dogs (from 11 to 25 kg) - From 12 months to 7 years old.",
        "category": "Dog Food",
        "sub_category": "Medium Adult Dog Food",
        "type": "Dry Food",
        "size": "4kg",
        "price": 415000,
        "stock": 10,
    },
    {
        "name": "Royal Canin Maxi Adult, Dry Food 4kg",
        "desc": "For adult large breed dogs (from 26 to 44 kg) - From 15 months to 5 years old.",
        "category": "Dog Food",
        "sub_category": "Maxi Adult Dog Food",
        "type": "Dry Food",
        "size": "4kg",
        "price": 415000,
        "stock": 10,
    },
    {
        "name": "Pet Carrier/Pet Cargo Large",
        "desc": "",
        "category": "Pet Supplies",
        "sub_category": "-",
        "type": "-",
        "size": "Size in cm: 62 x 39 x 38",
        "price": 274000,
        "stock": 10,
    },
    {
        "name": "Pet Cage Size Large",
        "desc": "",
        "category": "Pet Supplies",
        "sub_category": "-",
        "type": "-",
        "size": "Size in cm: 61 x 43 x 53",
        "price": 288000,
        "stock": 10,
    },
    {
        "name": "Cat Litter Box Large",
        "desc": "With plenty of room, this litter box can easily fit kitties of up to 10kg in size. It is suitable for multi-cat household use as well!",
        "category": "Pet Supplies",
        "sub_category": "-",
        "type": "-",
        "size": "Size in cm: 57 x 44 x 38",
        "price": 385000,
        "stock": 10,
    },
]