import random
from IPython.display import clear_output

def onep_game(c1, p1):
    bot_choice = random.choice(["stone", "paper", "scissors"])
    clear_output()
    print("Bot choices %s" % bot_choice)
    if c1 == "stone":
        if bot_choice == "stone":
            result = "Tie game"
            return result
        elif bot_choice == "paper":
            result = "bot wins"
            return result
        else:
            result = "%s wins" % p1
            return result
    if c1 == "paper":
        if bot_choice == "stone":
            result = "%s wins" % p1
            return result
        elif bot_choice == "paper":
            result = "Tie game"
            return result
        else:
            result = "bot wins"
            return result
    if c1 == "scissors":
        if bot_choice == "stone":
            result = "bot wins" 
            return result
        elif bot_choice == "paper":
            result = "%s wins" % p1
            return result
        else:
            result = "Tie game"
            return result
        
def twop_game(c1, c2, p1, p2):
    if c1 == "stone":
        if c2 == "stone":
            result = "Tie game"
            return result
        elif c2 == "paper":
            result = "%s wins" % p2
            return result
        else:
            result = "%s wins" % p1
            return result
    if c1 == "paper":
        if c2 == "stone":
            result = "%s wins" % p1
            return result
        elif c2 == "paper":
            result = "Tie game"
            return result
        else:
            result = "%s wins" % p2
            return result
    if c1 == "scissors":
        if c2 == "stone":
            result = "%s wins" % p2
            return result
        elif c2 == "paper":
            result = "%s wins" % p2
            return result
        else:
            result = "Tie game"
            return result
            

while True:
    player_1 = str(raw_input("Player 1 name: "))
    player_2 = str(raw_input("Player 2 name or write bot: "))
    if player_1 == player_2:
        print "Sorry, you can't play against yourself"
        raw_input("Press enter to continue")
        clear_output()
        continue
    elif player_2 == "bot":
        print "let's play"
        p1_choise = str(raw_input("%s please choose (stone/paper/scissors): " % player_1))
        res = onep_game(p1_choise, player_1)
        print res
    else:
        print "let's play"
        p1_choise = str(raw_input("%s please choose (stone/paper/scissors): " % player_1))
        p2_choise = str(raw_input("%s please choose (stone/paper/scissors): " % player_2))
        res = twop_game(p1_choise, p2_choise, player_1, player_2)
        print res


            

        
    cont = raw_input("Press enter to continue or write quit: ")
    if cont == "quit":
        break
    clear_output()
