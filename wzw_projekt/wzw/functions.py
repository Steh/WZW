import random
import string


def create_token():
    token = ''
    for x in range(0, 4):
        token += ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
        if x <= 2:
            token += '-'
    return token
