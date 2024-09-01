import re

def email_validate(email=None) -> str:
    if email is not None:
        regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(regex) is not None
    else:
        return None