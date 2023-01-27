

import string
import string
from random import choices


def create_password(lengh=8, upper=False, lower=False, digit=False, punc=False):
    pool = ''
    if upper:
        pool += string.ascii_uppercase
    if lower:
        pool += string.ascii_lowercase
    if digit:
        pool += string.digits
    if punc:
        pool += string.punctuation
    if pool == '':
        pool += string.ascii_lowercase

    password = choices(pool, k=lengh)
    return ''.join(password)


if __name__ == '__main__':
    print(create_password())
    print(create_password(18, digit=True))
    print(create_password(digit=True, punc=True, lower=True))


