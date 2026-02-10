import secrets
import string


def main():
    lowercase_letters = list(string.ascii_lowercase)
    uppercase_letters = list(string.ascii_uppercase)
    digits = list(string.digits)
    special_chars = list(string.punctuation)
    pre_password = ""
    for i in range(0, 16):
        if i < 4:
            pre_password += secrets.choice(lowercase_letters)
        elif i < 8:
            pre_password += secrets.choice(uppercase_letters)
        elif i < 12:
            pre_password += secrets.choice(digits)
        else:
            pre_password += secrets.choice(special_chars)
    password_set = set(pre_password)
    post_password = ""
    for i in password_set:
        post_password += i
    print(post_password)



if __name__ == "__main__":
    main()
