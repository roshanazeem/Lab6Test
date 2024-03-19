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
   print("3. Quit")
   option = int(input("Please enter an option:"))
   if option == 1:
       originalpassword = input("Please enter your password to encode:")
       newpassword = encode(originalpassword)
       print("Your password has been encoded and stored!")
       main()


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

if __name__ == "__main__":
    main()
