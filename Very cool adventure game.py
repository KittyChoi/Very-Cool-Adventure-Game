#We write functions that led us to win the game first, then we do the losing doors -----> building blocks down up method, make yours elgo bricks first, then connect them afterwards
import time

def lobby():
    skull = open("skull", "r")
    print(skull.read())
    skull.close()
    print("Welcome adventurer, to the experience of your lifetime. Make your decisions wisely.....or else you may not leave this place alive.")
    time.sleep(4.4)
    print("There are 6 rooms in this house, each with 2 doors.")
    time.sleep(3)
    print()
    print("To win, you must choose the correct door in each room to stay alive.")
    time.sleep(3)
    print("To lose, enter yourself to the wrong room of doom and suffer the consequences.")
    time.sleep(3)
    print()
    print("Your location: Lobby")
    time.sleep(4)
    print()
    print("Enter the your first door to start the game....or to die right here.")
    time.sleep(3)
    print()
    print("Door 1: Monster Room")
    time.sleep(2)
    print("Door 2: Bear Room")

    continue_loop = True
    while continue_loop == True:
        time.sleep(2)
        choice1 = input("Enter your choice here....Input 1 or 2 ----> ")
        if choice1 == "1":
            monster_room()
            continue_loop = False
        elif choice1 == "2":
            bear_room()
            continue_loop = False
        else:
            print("!INVALID INPUT!")



def monster_room():
    print()
    print(".", end="")
    time.sleep(1.5)
    print(".", end="")
    time.sleep(1.5)
    print(".", end="")
    time.sleep(3)
    print()
    print("It is your lucky day! It turns out the monster was quite cute and friendly.")
    monster = open("monster", "r")
    print(monster.read())
    monster.close()
    print()
    time.sleep(5)
    print("Now, it is time to test your luck again, choose your next door...")
    print()
    time.sleep(3)
    print("Door 1: The Gold Room")
    time.sleep(2)
    print("Door 2: The Silver Room")

    continue_loop = True
    while continue_loop == True:
        time.sleep(2)
        choice2 = input("Enter your choice here....Input 1 or 2 ----> ")
        if choice2 == "1":
            gold_room()
            continue_loop = False
        elif choice2 == "2":
            silver_room()
            continue_loop = False
        else:
            print("!INVALID INPUT!")

def bear_room():
    print()
    print(".", end="")
    time.sleep(1.5)
    print(".", end="")
    time.sleep(1.5)
    print(".", end="")
    time.sleep(3)
    print()
    print("The gigantic killer bear stands before you as it drools at the smell of your flesh.")
    bear = open("bear", "r")
    print(bear.read())
    bear.close()
    print()
    time.sleep(4)
    print("You got eaten by the bear alive...")
    print()
    time.sleep(4)
    reason = "Killer Bear"
    game_over(reason)



def gold_room():
    print()
    print(".", end="")
    time.sleep(1.5)
    print(".", end="")
    time.sleep(1.5)
    print(".", end="")
    time.sleep(3)
    print()
    print("Shining, shimmering, blinding yellow light shine on your face as you open the door.")
    gold = open("gold", "r")
    print(gold.read())
    gold.close()
    time.sleep(5)
    print("Congratulations, you have discovered a room full of gold bars. Be sure to take some with you. It may become useful later...")
    print()
    time.sleep(3)
    print("Now, proceed with caution and thought, choose your next door...")
    print()
    time.sleep(3)
    print("Door 1: The Mahogany Room")
    time.sleep(2)
    print("Door 2: The Oak Room")

    continue_loop = True
    while continue_loop == True:
        time.sleep(2)
        choice3 = input("Enter your choice here....Input 1 or 2 ----> ")
        if choice3 == "1":
            mahogany_room()
            continue_loop = False
        elif choice3 == "2":
            oak_room()
            continue_loop = False
        else:
            print("!INVALID INPUT!")

def silver_room():
    print()
    print(".", end="")
    time.sleep(1.5)
    print(".", end="")
    time.sleep(1.5)
    print(".", end="")
    time.sleep(3)
    print()
    print("Your greed brought you into a room filled with deadly molten silver.")
    silver = open("silver", "r")
    print(silver.read())
    silver.close()
    print()
    time.sleep(5)
    print("Before you could do anything else, you drowned in this pool of liquid silver.")
    time.sleep(4)
    reason = "Molten Silver"
    print()
    game_over(reason)



def mahogany_room():
    print()
    print(".", end="")
    time.sleep(1.5)
    print(".", end="")
    time.sleep(1.5)
    print(".", end="")
    time.sleep(3)
    print()
    print("You enter a forest of ant infested mahogany wood. The ants crawl up your body and you scream in terror.")
    ant = open("ant", "r")
    print(ant.read())
    ant.close()
    print()
    time.sleep(5)
    print("The ants eat you alive as you are left helpless on the cold dirt Earth. The bites on your body turn infectious, killing you brutally, and slowly.")
    time.sleep(4)
    reason = "Infected ant attack"
    game_over(reason)

def oak_room():
    print()
    print(".", end="")
    time.sleep(1.5)
    print(".", end="")
    time.sleep(1.5)
    print(".", end="")
    time.sleep(3)
    print()
    print("The smell of woody nature overwhelm your nostrils, you open your eyes and find yourself in a beautiful leafy forest.")
    oak = open("oak", "r")
    print(oak.read())
    oak.close()
    time.sleep(5)
    print("You're doing better than most people....keep going....but first, be sure to lounge in this forest before you make your next important decision.")
    print()
    time.sleep(4)
    print("Now, when you are ready, choose your next door...")
    print()
    time.sleep(2)
    print("Door 1: The Diamond Room")
    time.sleep(2)
    print("Door 2: The Crystal Room")

    continue_loop = True
    while continue_loop == True:
        time.sleep(2)
        choice4 = input("Enter your choice here....Input 1 or 2 ----> ")
        if choice4 == "1":
            diamond_room()
            continue_loop = False
        elif choice4 == "2":
            crystal_room()
            continue_loop = False
        else:
            print("!INVALID INPUT!")



def diamond_room():
    print()
    print(".", end="")
    time.sleep(1.5)
    print(".", end="")
    time.sleep(1.5)
    print(".", end="")
    time.sleep(3)
    print()
    print("Mysterious, spotless, and silent....you find yourself somewhere, unsure where exactly, but something in your heart tells you that this place is safe.")
    time.sleep(4)
    print("Look at yourself...look at your surroundings....you have found yourself in a room lined with walls of diamond and floors of diamond.")
    print()
    diamond = open("diamond", "r")
    print(diamond.read())
    diamond.close()
    time.sleep(5)
    print("Never in your life have you seen such a magnificent scene, so, before you make a the worst decision of your lifetime, pick up some diamond in this room before you make the most important decision of your life.")
    print()
    time.sleep(4)
    print("The finale...choose your fate, decide your final room...choose your next door...")
    print()
    time.sleep(3)
    print("Door 1: The Troll's Room")
    time.sleep(2)
    print("Door 2: The Magician's Room")

    continue_loop = True
    while continue_loop == True:
        time.sleep(2)
        choice5 = input("Enter your choice here....Input 1 or 2 ----> ")
        if choice5 == "1":
            troll_room()
            continue_loop = False
        elif choice5 == "2":
            magician_room()
            continue_loop = False
        else:
            print("!INVALID INPUT!")

def crystal_room():
    print()
    print(".", end="")
    time.sleep(1.5)
    print(".", end="")
    time.sleep(1.5)
    print(".", end="")
    time.sleep(3)
    print()
    print("You get thrown into the a room lined with walls made of shimmering crystals...")
    time.sleep(2.5)
    print()
    print("At first, all seems fine, but before you could react, undeniably sharp crystal spears start breaking out of the seemingly innocent walls. You try to run, but it is too late, the crystal spear has pierced through your chest. ")
    crystal = open("crystal", "r")
    print(crystal.read())
    crystal.close()
    time.sleep(4)
    reason = "Crystal spear"
    game_over(reason)



def troll_room():
    print()
    print(".", end="")
    time.sleep(1.5)
    print(".", end="")
    time.sleep(1.5)
    print(".", end="")
    time.sleep(3)
    print()
    print("You enter a humid, dark room and hear a fatal noise that shattered your eardrums.")
    time.sleep(3)
    print()
    print("As you fall to your knees in pain, you glimpse the evil eyes a 2D troll above you, singing his magnificent, yet fatal song.... ")
    troll = open("troll", "r")
    print(troll.read())
    troll.close()
    time.sleep(4)
    reason = "Murderous evil Troll"
    game_over(reason)

def magician_room():
    print()
    print(".", end="")
    time.sleep(1.5)
    print(".", end="")
    time.sleep(1.5)
    print(".", end="")
    time.sleep(3)
    print()
    print("The magician appeared out of thin air and greets you as you step foot into this dark room.")
    magician = open("magician.txt", "r")
    print(magician.read())
    magician.close()
    time.sleep(5.5)
    print()
    print("Amazed, he offers to use his magic to make use of the precious items you have collected and turn it into a trophy.")
    wand = open("wand", "r")
    print(wand.read())
    wand.close()
    time.sleep(5.5)
    print("He offers you to perform the spell yourself....He says: Type the magic word to turn your items into a trophy!")
    print()
    time.sleep(3)
    print("The magic word is.....ABRACADABRA")
    time.sleep(2)
    magic_word = input("Type your magic word here ----> ")

    if magic_word.upper() == "ABRACADABRA":
        win()
    else:
        time.sleep(4)
        reason = "yourself, by performing a DEADLY, WRONG SPELL."
        game_over(reason)



def game_over(reason):
    print("!!GAME OVER!!")
    print()
    print(f"You have been killed by {reason}")
    play_again()

def win():
    print()
    print("M", end="")
    time.sleep(0.5)
    print("A", end="")
    time.sleep(0.5)
    print("G", end="")
    time.sleep(0.5)
    print("I", end="")
    time.sleep(0.5)
    print("C", end="")
    time.sleep(0.5)
    print(" ", end="")
    time.sleep(0.5)
    print("I", end="")
    time.sleep(0.5)
    print("S", end="")
    time.sleep(0.5)
    print(" ", end="")
    time.sleep(0.5)
    print("W", end="")
    time.sleep(0.5)
    print("O", end="")
    time.sleep(0.5)
    print("R", end="")
    time.sleep(0.5)
    print("K", end="")
    time.sleep(0.5)
    print("I", end="")
    time.sleep(0.5)
    print("N", end="")
    time.sleep(0.5)
    print("G", end="")
    print()
    time.sleep(4)
    print()
    print("CONGRATULATIONS ADVENTURER!!! YOU ARE ONE OF THE ONLY HUMANS IN THE WORLD THAT HAS MADE IT THOUGH THIS HOUSE ALIVE.")
    time.sleep(5)
    print()
    print("PREPARE YOURSELF FOR YOUR NEXT ADVENTURE....YOU MAY NOT BE SO LUCKY....")
    print()
    time.sleep(4)
    print("But first, a TROPHY awaits you....")
    trophy = open("trophy", "r")
    print(trophy.read())
    trophy.close()
    play_again()

def play_again():
    time.sleep(2)
    want_to_play_again = input("Are you satisfied with the result? Do you want to test your luck once more, and play again? Input (Y/N) ----> ")
    if want_to_play_again.upper() == "Y" or "YES":
        print()
        print()
        print()
        lobby()
    else:
        print()
        print("Alright adventurer, see you in your next adventure...alive...")

lobby()




