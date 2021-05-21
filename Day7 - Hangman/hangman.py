import random

def main():
    with open("words.txt") as words:
        word_list = []
        for word in words:
            word_list.append(word.rstrip("\n"))

    chance = 5
    random_word = random.choice(word_list)
    starred_word = ""

    # keep the word secret
    for _ in range(len(random_word)):
        starred_word = starred_word + "_"

    print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
""")

    print("Welcome to Hangman Game! ")
    print(f"Here your secret word: {starred_word}")

    while 1:
        if chance == -1:
            print(f"You lost the game. The secret word was: {random_word}")
            return 0

        guess = input("guess: ")
        guess_check = turn(starred_word,random_word,guess)
        if guess_check == 0:
            print("wrong..")
            chance -= 1
            if chance == -1:
                pass
            else:
                print(f"{chance} wrong guess chance left.")
        else: 
            starred_word = guess_check
            print("you found!")
            print(guess_check)

def turn(starred_word, random_word, letter):
    random_word_list = list(random_word)
    starred_word_list = list(starred_word)

    if letter in random_word_list:
        # print("FOUND!")
        for index in range(len(random_word_list)):
            if random_word_list[index] == letter:
                starred_word_list[index] = letter

        starred_word = "".join(starred_word_list)
        return starred_word
    else:
        return 0

main()