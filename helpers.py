import string
import random

EMAIL_LEN = 6

def generate_email():
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(EMAIL_LEN))