import re

def normalize_phone(phone_number: str) -> str:
    phone_number = re.sub(r'[^\d+]', '', phone_number.strip())

    if phone_number.startswith('+380'):
        return phone_number
    elif phone_number.startswith('380'):
        return '+' + phone_number
    else:
        return '+38' + phone_number.lstrip('0')
