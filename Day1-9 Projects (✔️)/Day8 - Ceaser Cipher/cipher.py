import string 

letters = list(string.ascii_lowercase)

def crypt(message, shift):
    message_as_list = list(message)

    for lt in range(len(message_as_list)):
        flag = letters.index(message_as_list[lt])
        if (shift + flag) < len(letters):
            flag += shift
            message_as_list[lt] = letters[flag]
        elif (shift + flag) >= len(letters):
            flag = shift + flag - len(letters)
            message_as_list[lt] = letters[flag]

    message="".join(message_as_list)
    return message

def main():
    print("Welcome to the Ceaser Cipher!")
    print("What do you want to do?")
    ans = "yes"
    while(ans == "yes"):
        choice = input("Type 1 for encryption, 2 for decryption\n")
        message = input("Type your message:(no spaces)\n")
        shift = int(input("Type the shift number: \n"))

        if choice == "1":
            encoded_message = crypt(message,shift)
            print(f"Here's the encoded message: {encoded_message}")
            ans = input("Type 'yes' to back to menu again, otherwise type 'no'\n")
        
        if choice == "2":
            decoded_message = crypt(message,-shift)
            print(f"Here's the encoded message: {decoded_message}")            
            ans = input("Type 'yes' to back to menu again, otherwise type 'no'\n")

    print("Bye..")

main()
