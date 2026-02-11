import secrets
import string


def main():
    pre_password_set = set()
    pre_password_set_lower = set()
    pre_password_set_upper = set()
    pre_password_set_digits = set()
    pre_password_set_spchars = set()
    while len(pre_password_set_lower) < 4:
        pre_password_set_lower.add(secrets.choice(string.ascii_lowercase))
    while len(pre_password_set_upper) < 4:
        pre_password_set_upper.add(secrets.choice(string.ascii_uppercase))
    while len(pre_password_set_digits) < 4:
        pre_password_set_digits.add(secrets.choice(string.digits))
    while len(pre_password_set_spchars) < 4:
        pre_password_set_spchars.add(secrets.choice(string.punctuation))       
    pre_password_set.update(pre_password_set_spchars, pre_password_set_digits, pre_password_set_upper, pre_password_set_lower)
    post_password = ""
    for i in pre_password_set:
        post_password += i
    print(post_password)


if __name__ == "__main__":
    main()
