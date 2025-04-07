# bonus trouvez le ou les regex pour un numéro de téléphone europèen
# pensez au différent formatage, le préfixe (+32) par exemple

import re

phone_numbers = [
    "+32 123 456 789",
    "0123 456 789",
    "+32-123-456-789",
    "0123456789",
    "+32123456789",
    "+32 (0) 123 456 789",
    "(+32) 123 456 789"
]

def is_valid_phone_number(phone):
    pattern = r"^(?:\+32\s?\(?0?\)?\s?\d{3}\s?\d{3}\s?\d{3}|\d{2}\s?\d{3}\s?\d{3}|\+32-\d{3}-\d{3}-\d{3}|\d{10})$"
    return re.match(pattern, phone) is not None

for phone in phone_numbers:
    if is_valid_phone_number(phone):
        print(f"{phone} -> valid")
    else:
        print(f"{phone} -> error")
