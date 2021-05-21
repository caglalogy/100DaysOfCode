import os
import time

def bid_info(dict_of_users):
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    dict_of_users[name] = bid
    return dict_of_users

def winner_detection(bidders_dict):
    max_value = 0
    for bidder in bidders_dict:
        if bidders_dict[bidder] > max_value:
            max_value = bidders_dict[bidder]

    for k in bidders_dict:
        if bidders_dict[k] == max_value:
            return k

def main():
    logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
    auctioner_db = {}
    print("Welcome to the secret auction program.")
    c = "yes"
    while c == "yes":
        bid_info(auctioner_db)
        c = input("Are there any other bidders? Type 'yes' or 'no'\n")
        if c == "yes":
            os.system('cls')
        elif c == "no":
            print("The winner will be announced soon..")
            time.sleep(2)
            print(logo)
            time.sleep(1)
            winner = winner_detection(auctioner_db)
            print(f"The winner is {winner} with a bid of ${auctioner_db[winner]}")
    
main()