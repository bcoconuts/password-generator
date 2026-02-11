# password generator

import secrets
import string
import sys

SET_LENGTH = int(sys.argv[1])//4
SET_REMAINDER = int(sys.argv[1])%4

def main():
    pre_password_set = set()
    pre_password_set_lower = set()
    pre_password_set_upper = set()
    pre_password_set_digits = set()
    pre_password_set_spchars = set()
    pre_password_set_remainder = set()
    while len(pre_password_set_lower) < SET_LENGTH:
        pre_password_set_lower.add(secrets.choice(string.ascii_lowercase))
    while len(pre_password_set_upper) < SET_LENGTH:
        pre_password_set_upper.add(secrets.choice(string.ascii_uppercase))
    while len(pre_password_set_digits) < SET_LENGTH:
        pre_password_set_digits.add(secrets.choice(string.digits))
    while len(pre_password_set_spchars) < SET_LENGTH:
        pre_password_set_spchars.add(secrets.choice(string.punctuation))
    for i in range(0, SET_REMAINDER):
        pre_password_set_remainder.add(secrets.choice(string.ascii_letters))
    pre_password_set.update(pre_password_set_spchars, pre_password_set_digits, pre_password_set_upper, pre_password_set_lower, pre_password_set_remainder)
    post_password = ""
    for i in pre_password_set:
        post_password += i
    print(post_password)
    print(len(post_password))


if __name__ == "__main__":
    main()
