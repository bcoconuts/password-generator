# password generator

import secrets
import string
import sys

LOWER_LETTER_SET = set(string.ascii_lowercase)
UPPER_LETTER_SET = set(string.ascii_uppercase)
DIGIT_SET = set(string.digits)
PUNCTUATION_SET = set(string.punctuation)
CHARACTERS = string.ascii_letters + string.digits + string.punctuation

def main():
    if len(sys.argv) == 2:
        set_length = int(sys.argv[1])
    else:
        set_length = 16
    pass_set = set()
    while len(pass_set) < set_length or pass_set.isdisjoint(LOWER_LETTER_SET) or pass_set.isdisjoint(UPPER_LETTER_SET) or pass_set.isdisjoint(DIGIT_SET) or pass_set.isdisjoint(PUNCTUATION_SET):
        pass_set.add(secrets.choice(CHARACTERS))
        if len(pass_set) > set_length:
            pass_set.clear()
    password = "".join(pass_set)
    print(password, f"Password Length: {len(password)}")


if __name__ == "__main__":
    main()
