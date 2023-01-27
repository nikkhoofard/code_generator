

import string
import string
from random import choices


def create_password(lengh=8):
    password = choices(string.ascii_lowercase, k=lengh)
    return ''.join(password)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(create_password())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
