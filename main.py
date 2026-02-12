"""Password generator with configurable length and no repeated characters.

Generates a random password between 4-94 characters long, guaranteed
to contain at least one lowercase letter, one uppercase letter,
one digit, and one special character.

Usage:
    python main.py [length]

Examples:
    python main.py        # 16 characters (default)
    python main.py 32     # 32 characters
"""

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
    ALL_CHARS: string.ascii_letters + string.digits + string.punctuation,
}
DEFAULT_LENGTH = 16


def check_length(list_length: int) -> int:
    """Validate length of desired password. Ensure it falls within desired range.

    Args:
        list_length: Desired length of password.

    Returns:
        Length of password, or default length if desired length out of range.
    """
    if 4 <= list_length <= 94:
        return list_length
    else:
        print(
            f"\nInput Out Of Range. Creating password of default length ({DEFAULT_LENGTH})"
        )
        return DEFAULT_LENGTH


def determine_length() -> int:
    """Determine desired length of password to be created.

    Returns:
        Length of password to be created, or default password length if error encountered.
    """
    argument_count = len(sys.argv)
    if argument_count == 1:
        list_length = DEFAULT_LENGTH
    elif argument_count == 2:
        try:
            list_length = check_length(int(sys.argv[1]))
        except ValueError:
            print(
                f"\nInvalid Input. Creating password of default length ({DEFAULT_LENGTH})"
            )
            list_length = DEFAULT_LENGTH
    else:
        print(
            f"\nToo Many Arguments Provided. Creating password of default length ({DEFAULT_LENGTH})"
        )
        list_length = DEFAULT_LENGTH

    return list_length


def main():
    """Generate a random password of desired length and print to console.

    Ensures at least one character from each required category,
    removes duplicates from the available pool, and shuffles
    the final result for secure ordering.
    """
    list_length = determine_length()
    pass_list = [
        secrets.choice(CHARACTER_DICT[k])
        for k in CHARACTER_DICT.keys()
        if not k == ALL_CHARS
    ]
    available_chars_list = list(CHARACTER_DICT[ALL_CHARS])

    for char in pass_list:
        available_chars_list.remove(char)

    while len(pass_list) < list_length:
        next_char = secrets.choice(available_chars_list)
        pass_list.append(next_char)
        available_chars_list.remove(next_char)

    secrets.SystemRandom().shuffle(pass_list)
    password = "".join(pass_list)
    print(f"Password: {password}", f"\nPassword Length: {len(password)}")


if __name__ == "__main__":
    main()
