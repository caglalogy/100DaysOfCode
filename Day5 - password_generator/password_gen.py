import random
import string

def error_check(digitcount, lcount, scount, ncount):
    if lcount < 0 or scount < 0 or ncount < 0:
        print("ERROR! Given character type count is negative. ")
        exit()
    if digitcount == 0:
        print("Here your unvisible password:  \nEnjoy dummy!\nHow can i create 0-digit password?\nComeback later.")
        exit()

def password_generator(lCount, sCount, nCount):
    digit_count = lCount + sCount + nCount
    error_check(digit_count,lCount,sCount,nCount)
    created_password = ""

    letters = list(string.ascii_letters)
    symbols = list(string.punctuation)
    numbers = list(string.digits)

    list_of_elements = ["letter","symbol","number"]
    
    # check if there is an absent character type initially
    if lCount == 0:
        list_of_elements.remove("letter")
    if nCount == 0:
        list_of_elements.remove("number")
    if sCount == 0:
        list_of_elements.remove("symbol")

    
    # randomize the order of these elements as letters, numbers and symbols in this loop.
    for _ in range(digit_count):
        next_character = random.choice(list_of_elements)

        if next_character == "letter" and lCount != 0:
            created_password = created_password + random.choice(letters)
            lCount-=1

            if lCount == 0:
                list_of_elements.remove("letter")

        elif next_character == "symbol" and sCount != 0:
            created_password = created_password + random.choice(symbols)
            sCount-=1 

            if sCount == 0:
                list_of_elements.remove("symbol")

        elif next_character == "number" and nCount != 0:
            created_password = created_password + random.choice(numbers)
            nCount-=1    

            if nCount == 0:
                list_of_elements.remove("number")   

    return created_password

def main():
    print("Welcome to the PyPassword Generator!")
    letter_count = int(input("How many letters would you like in your password?\n"))
    symbol_count = int(input("How many symbols would you like?\n"))
    number_count = int(input("How many number would you like?\n"))

    password = password_generator(letter_count,symbol_count,number_count)
    print(f"Here is your password: {password}")

main()