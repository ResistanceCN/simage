from random import seed, choice
from string import ascii_letters, digits


def gen_str(str_len=16):
    """Generate random string."""
    seed()
    chars = ascii_letters + digits
    return ''.join([choice(chars) for _ in range(str_len)])
