import art
import game_data
import random
import string 

datalist = list() # game data

# this class includes all information about all celebrities/accounts. 
class Items:
        def __init__(self,name,follower_count,description,country):
            self.name = name
            self.follower_count = follower_count
            self.description = description
            self.country = country

def store_data():
    """
    In this function, given game data is stored in a global list (data) and shuffled.
    """

    data = game_data.data
    global datalist
    for i in range(len(data)):
        currentA = data[i]
        a_name = currentA.get("name")
        a_followerCount = currentA.get("follower_count")
        a_description = currentA.get("description")
        a_country = currentA.get("country")
        datalist.append(Items(a_name, a_followerCount, a_description, a_country))
    
    random.shuffle(datalist)

def compare():
    """
    Game is designed on comparison between each element on data list. This function compares them.
    """
    score = 0
    for i in range(len(datalist)+1):
        if i+1 != len(datalist):
            print(f"""
            Compare A: \n
            {datalist[i].name}
            {datalist[i].description} from {datalist[i].country}
            """)

            print(f"{art.vs}")

            print(f"""
            Compare B: \n
            {datalist[i+1].name}
            {datalist[i+1].description} from {datalist[i+1].country}
            """)    

            choice = (input("\nWhich one has more follower? "))
            choice = choice.upper()
            if choice == "A" and datalist[i].follower_count > datalist[i+1].follower_count:
                print("True!\n")                
                print('--------------------------------------------\n')

                score +=1
            elif choice == "B" and datalist[i+1].follower_count > datalist[i].follower_count:
                print("True!\n")
                print('--------------------------------------------\n')
                score +=1
            else:
                print("False.. ")
                print(f"GAME OVER! Your score is {score}\n--------------------------------------------\n")
                return

def main():
    print(art.logo)
    print()
    store_data()
    compare()
    ans = input("Do you wanna play again? (y/n): ")
    ans = ans.lower()
    if ans == "y":
        compare()
    elif ans == "n":
        print("Goodbye...")
    else:
        print("Undefined answer. Program is executing.")

main()