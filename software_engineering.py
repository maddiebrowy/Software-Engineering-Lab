def encode(password):
    new_password = [num + 3 for num in password]
    return new_password


def main():
    while True:
        print("Menu\n-------------")
        print("1. Encode\n2. Decode\n3. Quit")
        print()
        user_selection = int(input("Please enter an option: "))
        if user_selection == 1:
            password = input("Please enter your password to encode: ")
            password = [int(i) for i in password]
            print("Your password has been encoded and stored!")
            print()
        # user selection 2
        if user_selection == 2:
            new_password = ''.join(str(i) for i in encode(password))
            password = ''.join(str(i) for i in password)
            print(f'The new password is {new_password}, and the original password is {password}.')
            print()


if __name__ == "__main__":
    main()
