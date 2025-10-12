from datetime import datetime

def get_days_from_today(date: str) -> int | None:
    try:
        datetime_object = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        print(f"Invalid date format. Expected 'YYYY-MM-DD', but got '{date}'")
        return None

    today = datetime.today().date()
    return (today - datetime_object).days
