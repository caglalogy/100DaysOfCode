import random

def game(computer_choice, user_choice):
    if computer_choice == user_choice:
        return 2
    else:    
        if computer_choice == "rock":
            if user_choice == "paper":
                return 1 # user win 
            elif user_choice == "scissors":
                return 0 # computer win
        
        if computer_choice == "paper":
            if user_choice == "rock":
                return 0 # computer win 
            elif user_choice == "scissors":
                return 1 # user win

        if computer_choice == "scissors":
            if user_choice == "paper":
                return 0 # computer win 
            elif user_choice == "rock":
                return 1 # user win
    
def draw_turn (userchoice):
    if userchoice == "rock":
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    if userchoice == "paper":
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

    if userchoice == "scissors":
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

def main():
    choices = ["rock","paper","scissors"] # set of results

    print("Welcome to rock-scissors-paper game!")

    # user turn
    choice = int(input("1 - rock\n2 - paper\n3 - scissors\n"))
    user_choice = choices[choice-1]
    draw_turn(user_choice)

    # computer turn
    rand_integer = random.randint(0,2)
    computer_choice = choices[rand_integer]
    draw_turn(computer_choice)

    if game(computer_choice,user_choice) == 1:
        print(f"""
        You win!
        """,end="")
    elif game(computer_choice,user_choice) == 0: 
        print(f"""
        You lost..
        """,end="")
    elif game(computer_choice,user_choice) == 2:
        print(f"""
        Draw.
        """,end="")
    print(f"""
        Computer: {computer_choice}
        You: {user_choice}
    """)
    
main()