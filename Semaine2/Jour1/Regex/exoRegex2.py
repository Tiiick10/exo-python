# trouvez le regex pour une adresse mail.
# testez ces adresser mail
# ryad@gmail.com
# ryad@@gmail.com
# ryadgmail.com
# ryad@.com
# ryad@ryad.be

import re

addresses = ["ryad@gmail.com", "ryad@@gmail.com", "ryadgmail.com", "ryad@.com", "ryad@ryad.be" ]

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

for email in addresses:
    if is_valid_email(email):
        print(f"{email} -> true")
    else:
        print(f"{email} -> error")