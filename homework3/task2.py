import random

def get_numbers_ticket(min, max, quantity):
    numbers = list(range(min, max + 1))
    result = random.sample(numbers, quantity)
    result.sort()
    return result

print(get_numbers_ticket(1,10,5))


