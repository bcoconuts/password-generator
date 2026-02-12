# password generator - Creates random passwor between 4-94 characters long, with no repeated characters. minimum of one lowercase, uppercase, digit, and sp char


import secrets
import string
import sys


UPPERCASE_CHARS = "uppercase_chars"
LOWERCASE_CHARS = "lowercase_chars"
DIGITS = "digits"
PUNCTUATION = "punctuation"
ALL_CHARS = "all_chars"
CHARACTER_DICT = {
    UPPERCASE_CHARS: string.ascii_uppercase,
    LOWERCASE_CHARS: string.ascii_lowercase,
    DIGITS: string.digits,
    PUNCTUATION: string.punctuation,
    ALL_CHARS: string.ascii_letters + string.digits + string.punctuation
}
DEFAULT_LENGTH = 16


def check_length(list_length: int) -> int:
    if 4 <= list_length <= 94:
        return list_length
    else:
        print(f"\nInput Out Of Range. Creating password of default length ({DEFAULT_LENGTH})")
        return DEFAULT_LENGTH


def determine_length() -> int:
    argument_count = len(sys.argv)
    if argument_count == 1:
        list_length = DEFAULT_LENGTH
    elif argument_count == 2:
        try:
            list_length = check_length(int(sys.argv[1]))
        except ValueError:
            print(f"\nInvalid Input. Creating password of default length ({DEFAULT_LENGTH})")
            list_length = DEFAULT_LENGTH
    else:
        print(f"\nToo Many Arguments Provided. Creating password of default length ({DEFAULT_LENGTH})")
        list_length = DEFAULT_LENGTH

    return list_length


def main():
    list_length = determine_length()
    pass_list = [secrets.choice(CHARACTER_DICT[k]) for k in CHARACTER_DICT.keys() if not k == ALL_CHARS]
    available_chars = CHARACTER_DICT[ALL_CHARS]

    for char in pass_list:
        available_chars = available_chars.replace(char, "")

    while len(pass_list) < list_length:
        next_char = secrets.choice(available_chars)
        pass_list.append(next_char)
        available_chars = available_chars.replace(next_char, "")
        
    secrets.SystemRandom().shuffle(pass_list)
    password = "".join(pass_list)
    print(f"Password: {password}", f"\nPassword Length: {len(password)}")


if __name__ == "__main__":
    main()
