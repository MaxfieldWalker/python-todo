import random


def generate_id():
    s = "0123456789abcdef"
    return "".join([random.choice(s) for _ in range(0, 8)])
