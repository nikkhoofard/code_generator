import argparse
import string
from random import choices


def create_password(length=8, upper=False, lower=False, digit=False, punc=False):
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

    password = choices(pool, k=length)
    return ''.join(password)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('length', type=int, help="length of password")
    parser.add_argument('-u', '--upper', help='upper case', action='store_true')
    parser.add_argument('-l', '--lower', help="lowercase", action='store_true')
    parser.add_argument('-d', '--digit', help="digit", action='store_true')
    parser.add_argument('-p', '--punc', help="punc", action='store_true')

    args = parser.parse_args()

    print(create_password(args.length, args.upper, args.lower, args.digit, args.punc))


