print("""
                  __..-----')
        ,.--._ .-'_..--...-'
       '-"'. _/_ /  ..--''""'-.
       _.--""...:._:(_ ..:"::. \
    .-' ..::--""_(##)#)"':. \ \)    \ _|_ /
   /_:-:'/  :__(##)##)    ): )   '-./'   '\.-'
   "  / |  :' :/""\///)  /:.'    --(       )--
     / :( :( :(   (#//)  "       .-'\.___./'-.
    / :/|\ :\_:\   \#//\            /  |  \
    |:/ | ""--':\   (#//)              '
    \/  \ :|  \ :\  (#//)
         \:\   '.':. \#//\
          ':|    "--'(#///)
                     (#///)
                     (#///)         ___/""\     
                      \#///\           oo##
                      (##///)         `-6 #
                      (##///)          ,'`.
                      (##///)         // `.\
                      (##///)        ||o   \\
                       \##///\        \-+--//
                       (###///)       :_|_(/
                       (sjw////)__...--:: :...__
                       (#/::'''        :: :     ""--.._
                  __..-'''           __;: :            "-._
          __..--""                  `---/ ;                '._
 ___..--""                             `-'                    "-..___
   (_ ""---....___                                     __...--"" _)
     ''''--...  ___......-----......._______......----...     --...
                   ''''''"       ---.....   ___....----
 
""")

print("\nWelcome to Treasure Island.\nYour mission is to find the treasure.")
print("You are at a cross road. Where do you want to go?")
direction = input("left or right?\n")
if direction == "left":
    activity = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if activity == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one blue and one yellow. Which color do you choose?")
        color = input("red, yellow or blue?\n")
        if color == "red":
            print("It's a room full of fire.\nGame Over.")
        elif color == "yellow":
            print("You found the treasure! You win!")
        elif color == "blue":
            print("You have been eaten by beasts.\nGame Over.")
        else:
            print("Game Over.")
    else:
        print("You have been attacked by trout.\nGame Over.")
else:
    print("You fell in a hole.\nGame Over.")