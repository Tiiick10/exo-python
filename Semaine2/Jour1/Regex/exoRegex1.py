# EXO regex 

# trouvez le regex d'une carte bancaire

import re

credit_card = ["4687615433282834", "4536-6184-4896-4489", "4879 4897 1567 4658", "765489632145", "46876154332828345"]

def is_valid_credit_card(card):
    pattern = r"^(?:\d{4}[- ]?){3}\d{4}$"
    return re.match(pattern, card) is not None

for card in credit_card:
    if is_valid_credit_card(card):
        print(f"{card} -> valid")
    else:
        print(f"{card} -> error")
