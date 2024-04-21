grooming = {
    "cat": {
        "main": {
            "weight <= 5kg": [
                {"name": "Dry Grooming", "price": 30000},
                {"name": "Basic Grooming", "price": 50000},
                {
                    "name": "Basic Grooming with Anti-Lice/Anti-Fungal Treatment",
                    "price": 75000,
                    "is_visible": True,
                },
                {"name": "Complete Grooming", "price": 85000},
            ],
            "weight > 5kg": [
                {"name": "Dry Grooming", "price": 40000},
                {"name": "Basic Grooming", "price": 80000},
                {
                    "name": "Basic Grooming with Anti-Lice/Anti-Fungal Treatment",
                    "price": 110000,
                    "is_visible": True,
                },
                {"name": "Complete Grooming", "price": 120000},
            ],
        },
        "adds_on": {
            "weight <= 5kg": [
                {"name": "Shaving", "price": 85000},
                {
                    "name": "Brushing & Teeth Cleaning",
                    "price": 25000,
                    "is_visible": True,
                },
                {"name": "Skin Treatment", "price": 90000},
            ],
            "weight > 5kg": [
                {"name": "Shaving", "price": 150000},
                {
                    "name": "Brushing & Teeth Cleaning",
                    "price": 25000,
                    "is_visible": True,
                },
                {"name": "Skin Treatment", "price": 125000},
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
                    "is_visible": True,
                },
                {"name": "Complete Grooming", "price": 120000},
            ],
            "medium": [
                {"name": "Dry Grooming", "price": 75000},
                {
                    "name": "Basic Grooming",
                    "price": 100000,
                },
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
