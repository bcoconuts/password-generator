# password generator - Creates random passwor between 4-40 characters ling, with no repeated characters

import secrets
import string
import sys

LOWER_LETTER_SET = set(string.ascii_lowercase)
UPPER_LETTER_SET = set(string.ascii_uppercase)
DIGIT_SET = set(string.digits)
PUNCTUATION_SET = set(string.punctuation)
CHARACTERS = string.ascii_letters + string.digits + string.punctuation
DEFAULT_LENGTH = 16

def check_length(set_length: int) -> int:
    if 3 < set_length <= 40:
        return set_length
    else:
        print(f"\nInput Out Of Range. Creating password of default length ({DEFAULT_LENGTH})")
        return DEFAULT_LENGTH


def determine_length() -> int:
    argument_count = len(sys.argv)
    if argument_count > 2:
        set_length = DEFAULT_LENGTH
        print(f"\nToo Many Arguments Provided. Creating password of default length ({DEFAULT_LENGTH})")
    elif 0 < argument_count <= 1:
        set_length = DEFAULT_LENGTH
    else:
        try:
            set_length = check_length(int(sys.argv[1]))
        except ValueError:
            set_length = DEFAULT_LENGTH
            print(f"\nInvalid Input. Creating password of default length ({DEFAULT_LENGTH})")

    return set_length


def main():
    set_length = determine_length()
    pass_set = set()
    while len(pass_set) < set_length or pass_set.isdisjoint(LOWER_LETTER_SET) or pass_set.isdisjoint(UPPER_LETTER_SET) or pass_set.isdisjoint(DIGIT_SET) or pass_set.isdisjoint(PUNCTUATION_SET):
        pass_set.add(secrets.choice(CHARACTERS))
        if len(pass_set) > set_length:
            pass_set.clear()
    password = "".join(pass_set)
    print(f"Password: {password}", f"\nPassword Length: {len(password)}")


if __name__ == "__main__":
    main()
