import random
cards = {
    "A" : 11,
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10": 10,
    "J" : 10,
    "Q" : 10,
    "K" : 10 
}
def check(user, comp, user_cards ,computer_cards):
    if user == 21:
        print("You win.")
        print(f"Your final hand: {user_cards}")
        print(f"Computer's final hand: {computer_cards}")
        exit()
    if comp == 21 or user > 21 :
        print("You lost.")
        print(f"Your final hand: {user_cards}")
        print(f"Computer's final hand: {computer_cards}")
        exit()
    if 21-user < 21-comp :
        print("You win.")
        print(f"Your final hand: {user_cards}")
        print(f"Computer's final hand: {computer_cards}")
        exit()

def game():
    user_cards = list()
    computer_cards = list()

    for i in range(2):
        user_cards.append(random.choice(list(cards.keys())))

    for i in range(2):
        computer_cards.append(random.choice(list(cards.keys())))

    user_score  = cards[user_cards[0]] + cards[user_cards[1]]
    computer_score = cards[computer_cards[0]] + cards[computer_cards[1]]    
    while user_score < 22 and computer_score < 22:
        y_or_n = "y"
        while True:
            if y_or_n == "n":
                check(user_score, computer_score, user_cards ,computer_cards)
                break   
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")
            
            y_or_n = input("Type 'y' to get another card, 'n' to pass: ")
            if y_or_n == "y":
                user_cards.append(random.choice(list(cards.keys())))
                user_score += (cards[user_cards[-1]])
            computer_move = random.randint(0,2)
            if computer_move == 0:
                computer_cards.append(random.choice(list(cards.keys())))
            check(user_score, computer_score, user_cards ,computer_cards)
    """
    2-10 --> 2-10
    K,J,Q --> 10
    A --> 11,1 (1 if only card totality pass 21)
    """

def main():
    print("""
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"
    """)
    c = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if c =="y":
        game()
    else:
        print("bye")

main()

