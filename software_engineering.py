def encode(password):
    new_password = [num + 3 for num in password]
    return new_password


def decode(new_password):
    password = [num - 3 for num in new_password]
    return password


def main():
    while True:
        # print menu
        print("Menu\n-------------")
        print("1. Encode\n2. Decode\n3. Quit")
        print()
        user_selection = int(input("Please enter an option: "))
        # menu option 1
        if user_selection == 1:
            password = input("Please enter your password to encode: ")
            password = [int(i) for i in password]
            print("Your password has been encoded and stored!")
            print()
        # menu option 2
        if user_selection == 2:
            new_password = encode(password)
            password = decode(new_password)

            new_password = ''.join(str(i) for i in encode(password))
            password = ''.join(str(i) for i in password)
            print(f'The new password is {new_password}, and the original password is {password}.')
            print()
        # menu option 3
        if user_selection == 3:
            exit()


if __name__ == "__main__":
    main()
