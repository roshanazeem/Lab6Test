# Roshan Azeem
originalpassword = ""
newpassword = ""


def main():
    global originalpassword
    global newpassword
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")
    option = int(input("Please enter an option: "))
    if option == 1:
        originalpassword = input("Please enter your password to encode: ")
        newpassword = encode(originalpassword)
        print("Your password has been encoded and stored!\n")
        main()
    elif option == 2:
        if newpassword:
            print(f"The encoded password is {newpassword}, "
                  f"and the original password is {decode(newpassword)}\n")
        else:
            print("You need to encode a password first.\n")
        main()
    elif option == 3:
        print("Goodbye!")
    else:
        print("Sorry, that is not a valid option.\n")


def encode(password):
    newpassword = ""
    for i in (password):
        encode = int(i) + 3
        if encode >= 10:
            encode -= 10
            newpassword = newpassword + str(encode)
        else:
            newpassword = newpassword + str(encode)
    return newpassword


def decode(password: str) -> str:
    """
    Decodes password by subtracting 3 from each number
    Ex. decode("45678888") -> "12345555'
    Created by Corban Pendrak on 19Mar24
    :param password: 8-digit password string
    :return: Decoded 8-digit password string
    """
    return "".join(str((int(num) - 3) % 10) for num in password)


if __name__ == "__main__":
    main()
