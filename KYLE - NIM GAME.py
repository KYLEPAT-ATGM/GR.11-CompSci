import time,sys,random,os         # function that prints letters one at a time to make them look like it is slowly showing text
def print_slow(str):
    for letter in str:                  # Creates a loop which reads over each character
        sys.stdout.write(letter)        # Prints the characters one by one in the terminal without adding a new line, so it forms the word
        sys.stdout.flush()              # The flush command instantly forces the output to be written into the terminal immediately to ensure all characters are displayed as they are written
        time.sleep(0.015)               # Value that controls the second delay before each letter will be inputted into the terminal

##################################################################################################################################################
# ASCII ART CREATION (BTW FONT IS ANSI REGULAR)
# Each function returns a list of strings representing a number in ASCII art.
# They are created by stacking these strings ontop of eachother to form the number
def one():
    return [" ██ ", "███ ", " ██ ", " ██ ", " ██ "] 

def two():
    return ["██████  ", "     ██ ", " █████  ", "██      ", "███████ "]

def three():
    return ["██████  ", "     ██ ", " █████  ", "     ██ ", "██████  "]

def four():
    return ["██   ██ ", "██   ██ ", "███████ ", "     ██ ", "     ██ "]

def five():
    return ["███████ ", "██      ", "███████ ", "     ██ ", "███████ "]

def six():
    return [" ██████  ", "██       ", "███████  ", "██    ██ ", " ██████  "]

def seven():
    return ["███████ ", "     ██ ", "    ██  ", "   ██   ", "   ██   "]

def eight():
    return [" █████  ", "██   ██ ", " █████  ", "██   ██ ", " █████  "]

def nine():
    return [" █████  ", "██   ██ ", " ██████ ", "     ██ ", " █████  "]

def zero():
    return [" ██████  ", "██  ████ ", "██ ██ ██ ", "████  ██ ", " ██████  "]

def ten():
    return [" ██  ██████  ", "███ ██  ████ ", " ██ ██ ██ ██ ", " ██ ████  ██ ", " ██  ██████  "]

def eleven():
    return [" ██  ██ ", "███ ███ ", " ██  ██ ", " ██  ██ ", " ██  ██ "]

def twelve():
    return [" ██ ██████  ", "███      ██ ", " ██  █████  ", " ██ ██      ", " ██ ███████ "]

def thirteen():
    return [" ██ ██████  ", "███      ██ ", " ██  █████  ", " ██      ██ ", " ██ ██████  "]

def fourteen():
    return [" ██ ██   ██ ", "███ ██   ██ ", " ██ ███████ ", " ██      ██ ", " ██      ██ "]

def fifteen():
    return [" ██ ███████ ", "███ ██      ", " ██ ███████ ", " ██      ██ ", " ██ ███████ "]

# THIS IS VERY CONFUSING TO UNDERSTANDDDDD
# Function to combine and print the ASCII representations of numbers horizontally
def print_numbers_horizontally(spacing=1, *numbers):
    rows = ['' for _ in range(5)]       # Create a list to hold each row of the combined output; there are 5 rows.
    space_num = ' ' * spacing           # Create a string of spaces for the specified spacing by multiplying the current spacing (1)
    for number in numbers:              # Loop through each number function passed to the function
        num_func = int_to_str(number)             # Convert the number into its corresponding ASCII art representation by calling the int_to_str() function(This changes it into a readable string for the code).
        # For each of the 5 rows of the current number cuz they are built with 5 lines
        for i in range(5):
            rows[i] += num_func[i] + space_num  # Append the current row of the number's ASCII art to the corresponding row in 'rows', with added spacing
    for row in rows:                    # After constructing all rows, print each row
        print(row)

# Example use: Print the ASCII representation of 'ten' three times, with 4 spaces in between
###print_numbers_horizontally(4, ten, ten, ten)

# Function to get the ASCII representation based on an integer by calling the funct
def int_to_str(num):
    if num == 0:
        return zero()
    elif num == 1:
        return one()
    elif num == 2:
        return two()
    elif num == 3:
        return three()
    elif num == 4:
        return four()
    elif num == 5:
        return five()
    elif num == 6:
        return six()
    elif num == 7:
        return seven()
    elif num == 8:
        return eight()
    elif num == 9:
        return nine()
    elif num == 10:
        return ten()
    elif num == 11:
        return eleven()
    elif num == 12:
        return twelve()
    elif num == 13:
        return thirteen()
    elif num == 14:
        return fourteen()
    elif num == 15:
        return fifteen()
    else:
        # Return a error if the number is not between 0 and 15
        return ["     ", " UNK ", " NUM ", "     ", "     "]  # "UNK NUM" for unsupported numbers

def you_are_an_idiot():
    print(" ")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠶⠞⠛⠛⠉⠉⠉⠉⠉⠙⠛⢦⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠞⠉⠀⠀⠀⠆⠀⠀⠀⠀⠀⠀⠀⠀⠐⢹⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⢠⡾⠋⠀⠀⠀⠀⢀⣀⣤⣤⠴⠶⠶⠶⠶⠶⡶⡾⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⣴⠋⠀⠀⢀⡴⠾⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⢀⡼⠁⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠃You forgot something...")
    print("⠀⠀⢀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⣰⣏🧠⣀⣀")
    print("⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣆⠀⠀⠀⠀⠀⠀⢸⡇⣠⠏⠉⠛⠛⠋⠁")
    print("⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡄⠀⠀⠀⠀⠀⢸⣿⠋⠀⠀⠀⠀⠀⠀")
    print("⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠀⠀⠀⣼⡇⠀⠀⠀⠀⠀⠀⠀")
    print("⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠀⠀⣼⠃⣧⠀")
    print(" ")
    print_slow("You are an idiot bub.")

########################################################-------MULTIPLAYER------##########################################################################################
# This function takes the pile chosen and amount to be taken and calculates the piles using these parameters 
def update_pile(pile, take_amount):
    if take_amount >= pile:  # If taking amount is greater than or equal to pile
        return 0  # Return zero if pile is zero
    return pile - take_amount  # subtract the taking amount if take is not greater

# This function verifies if the pile can be taken from
def get_valid_pile_choice(player, pile_a, pile_b, pile_c):
    while True:
        pile_choice = input(f"{player}(a/b/c): ")
        while pile_choice not in ["a","b","c"]:
            pile_choice = input(f"{player}(a/b/c): ")
        if pile_choice == "a" and pile_a > 0:           # If both conditions are met, return a, so true.
            return "a"
        elif pile_choice == "b" and pile_b > 0:
            return "b"
        elif pile_choice == "c" and pile_c > 0:
            return "c"
        else:
            print("PLEASE ENTER A VALID PILE.")

def multiplayer():
    os.system('cls')
    print_slow("THIS IS A MULTIPLAYER GAME MODE, PLEASE ENTER YOUR NAMES.")
    input(" ")
    player_1 = input("PLAYER ONE: ")
    while player_1 == "":
        player_1 = input("ENTER A VALID NAME: ")
    print(" ")
    player_2 = input("PLAYER TWO: ")
    while player_2 == "":
        player_2 = input("ENTER A VALID NAME: ")
    while player_2 == player_1:
        player_2 = input("ENTER A VALID NAME: ")
    print(" ")
    print_slow(f"{player_1} VS {player_2}")
    print(" ")
    print_slow("ROLLING A DICE...")
    time.sleep(1)
    print("")
    print_slow("...")
    time.sleep(1)
    dice_roll = random.randint(1,10)
    if dice_roll  % 2 == 0:     # If even number is rolled player 1 goes first
        player_turn = player_1
        print(" ")
        print_slow(f"{player_1} WILL GO FIRST.")
    else:
        player_turn = player_2
        print(" ")
        print_slow(f"{player_2} WILL GO FIRST.")

    input(" ")
    print_slow("THE GAME BEGINS.")
    input(" ")
    pile_a = random.randint(7,15)        # Make random piles from 7-15
    pile_b = random.randint(7,15)
    pile_c = random.randint(7,15)
    print_slow("GENERATING NUMBERS...")
    time.sleep(1)
    print("")
    print_slow("...")
    time.sleep(1)
    os.system("cls")
    print(" ")
    print_numbers_horizontally(4, pile_a, pile_b, pile_c)

    while pile_a > 0 or pile_b  > 0 or pile_c > 0:
        def player_1_turn():
            nonlocal pile_a, pile_b, pile_c  # Declare to modify outer variables
            #PLAYER 1's TURN
            print(" ")
            print_slow(f"{player_1}'s TURN - - - - - - - - - - - -")
            input(" ")

            print_slow("WHICH PILE WILL YOU TAKE FROM?")
            print(" ")
            # PULLS THE FUNCTION TO  GET THE VALID PILE CHOICE
            player_1_pile_choice =  get_valid_pile_choice(player_1, pile_a, pile_b, pile_c)
            
            print_slow("HOW MANY NUMBERS WILL YOU TAKE?")
            print("")
            player_1_pile_take = input(f"{player_1}(1-15): ")
            while player_1_pile_take  not in ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]:  # WHILE LOOP TO CHECK IF THE INPUT IS BETWEEN 1-15
                player_1_pile_take = input(f"{player_1}(1-15): ")
                print(" ")

            player_1_pile_take = int(player_1_pile_take)  # Convert to integer
            # Processes which pile was chosen and uses update_pile (read update pile for more info)
            if player_1_pile_choice == "a":
                pile_a = update_pile(pile_a, player_1_pile_take)
            elif player_1_pile_choice == "b":
                pile_b = update_pile(pile_b, player_1_pile_take)
            elif player_1_pile_choice == "c":
                pile_c = update_pile(pile_c, player_1_pile_take)
            
            # Checks if player 1 lost
            if pile_a == 0 and pile_b == 0 and pile_c == 0:
                print(" ")
                print_slow(f"{player_1} IS AN IDIOT.")
                print(" ")
                print_slow(f"{player_2} WINS!")
                you_are_an_idiot()
                input("")
                os.system('cls')
                print_slow("Would you like to restart the game?")
                restart = input("(yes/no): ")
                if restart == "yes":
                    print("ok")
                    print("")
                    for i in range(5):
                        time.sleep(0.55)
                        print_slow("...")
                        print("")
                    start_game()
                else:
                    time.sleep(2)
                    print_slow("ok")
                    time.sleep(1.75)
                    exit()

            os.system('cls')
            print_slow(f"{player_1} took  {player_1_pile_take} from pile {player_1_pile_choice}")
            print(" ")
            print_numbers_horizontally(4, pile_a, pile_b, pile_c)
            
        def player_2_turn():
            nonlocal pile_a, pile_b, pile_c  # Declare to modify outer variables
            # PLAYER 2's TURN
            print(" ")
            print_slow(f"{player_2}'s TURN - - - - - - - - - - - -")
            input(" ")
            print_slow("WHICH PILE WILL YOU TAKE FROM?")
            print(" ")
            player_2_pile_choice = get_valid_pile_choice(player_2, pile_a, pile_b, pile_c)
            

            print_slow("HOW MANY NUMBERS WILL YOU TAKE?")
            print(" ")
            player_2_pile_take = input(f"{player_2}(1-15): ")
            while player_2_pile_take  not in ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]:
                player_2_pile_take = input(f"{player_2}(1-15): ")
                print(" ")

            player_2_pile_take = int(player_2_pile_take)  # Convert to integer
            # Update piles based on player's choice
            if player_2_pile_choice == "a":
                pile_a = update_pile(pile_a, player_2_pile_take)
            elif player_2_pile_choice == "b":
                pile_b = update_pile(pile_b, player_2_pile_take)
            elif player_2_pile_choice == "c":
                pile_c = update_pile(pile_c, player_2_pile_take)

            
            # Cheks if player 2 lost
            if pile_a == 0 and pile_b == 0 and pile_c == 0:
                print(" ")
                print_slow(f"{player_2} IS AN IDIOT.")
                print(" ")
                print_slow(f"{player_1} WINS!")
                you_are_an_idiot()
                input("")
                os.system('cls')
                print_slow("Would you like to restart the game?")
                restart = input("(yes/no): ")
                if restart == "yes":
                    print("ok")
                    print("")
                    for i in range(5):
                        time.sleep(0.55)
                        print_slow("...")
                        print("")
                    start_game()
                else:
                    time.sleep(2)
                    print_slow("ok")
                    time.sleep(1.75)
                    exit()

            
            os.system('cls')
            print_slow(f"{player_2} took  {player_2_pile_take} from pile {player_2_pile_choice}")
            print(" ")
            print_numbers_horizontally(4, pile_a, pile_b, pile_c)
        if player_turn  == player_1:
            player_1_turn()
            player_2_turn()
        else:
            player_2_turn()
            player_1_turn()

#---------------------------------------------------------------------------------------SINGLEPLAYER MODE (INCOMPLETE)--------------------------------------------------------------------------- 
def bot_move(pile_a, pile_b, pile_c):
    # The AI randomly chooses a pile and a number to take
    piles = [pile_a, pile_b, pile_c]
    available_piles = [i for i, pile in enumerate(piles) if pile > 0]   # Checks if indices of pile is positive (this line basically chooses which piles can be selected)
                                                                        # The enumerate function iterates through every item and keeps track of it basically
                                                                        # Finally it checks the indices if it is positive or not, if zero, it will be excluded 
    if available_piles:
        chosen_pile_index = random.choice(available_piles) # Randomly select an index from the available piles
        pile_amount = piles[chosen_pile_index]              
        if (pile_a == 0 and pile_b > 1 and pile_c == 0) or \
           (pile_b == 0 and pile_a > 1 and pile_c == 0) or \
           (pile_c == 0 and pile_a > 1 and pile_b == 0):
                                                                                                        #THIS DOES NOT WORK PROPERLY FOR SOME REASON
            take_amount = pile_amount - 1  # Take enough to leave 1 for the player
        # If one of the piles is 2 and another is non-empty, take 1
        if (pile_a == 2 and (pile_b > 0 or pile_c > 0)) or \
           (pile_b == 2 and (pile_a > 0 or pile_c > 0)) or \
           (pile_c == 2 and (pile_a > 0 or pile_b > 0)):
            take_amount = 1
            
        else:
            take_amount = random.randint(1, pile_amount) 

        if chosen_pile_index == 0:              # The piles are labled from 0,1,2
            return 'a', take_amount  # pile_a
        elif chosen_pile_index == 1:
            return 'b', take_amount  # pile_b
        else:
            return 'c', take_amount  # pile_c
    return None, 0  # In case there are no piles to take from

def singleplayer():
    os.system('cls')
    print_slow("THIS IS A SINGLEPLAYER GAME MODE, PLEASE ENTER YOUR NAME.")
    input(" ")
    player = input("YOUR NAME: ")
    while player == "":
        player = input("ENTER A VALID NAME: ")
    print(" ")
    print_slow(f"HELLO {player}, THE GAME BEGINS.")
    input(" ")
    print_slow("ROLLING A DICE...")
    time.sleep(1)
    print("")
    print("...")  # Simulate rolling the dice
    time.sleep(1)
    dice_roll = random.randint(1, 10)
    player_turn = player if dice_roll % 2 == 0 else "BOT"
    print(" ")
    print_slow(f"{player_turn} WILL GO FIRST." if player_turn == player else "BOT WILL GO FIRST.")

    # Initialize piles
    pile_a = random.randint(7, 15)
    pile_b = random.randint(7, 15)
    pile_c = random.randint(7, 15)
    print(" ")
    print_numbers_horizontally(4, pile_a, pile_b, pile_c)

    while pile_a > 0 or pile_b > 0 or pile_c > 0:
        if player_turn == player:
            print(" ")
            print_slow(f"{player}'s TURN - - - - - - - - - - - -")
            input(" ")

            print_slow("WHICH PILE WILL YOU TAKE FROM?")
            print(" ")
            player_pile_choice = get_valid_pile_choice(player, pile_a, pile_b, pile_c)

            print_slow("HOW MANY NUMBERS WILL YOU TAKE?")
            print(" ")
            player_pile_take = input(f"{player}(1-15): ")
            while player_pile_take not in map(str, range(1, 16)):   # map does the thing to every item in range, thus turning them all into strings
                player_pile_take = input(f"{player}(1-15): ")

            player_pile_take = int(player_pile_take)
            if player_pile_choice == "a":
                pile_a = update_pile(pile_a, player_pile_take)
            elif player_pile_choice == "b":
                pile_b = update_pile(pile_b, player_pile_take)
            elif player_pile_choice == "c":
                pile_c = update_pile(pile_c, player_pile_take)

            if pile_a == 0 and pile_b == 0 and pile_c == 0:
                print(" ")
                print_slow(f"{player} IS AN IDIOT.")
                print(" ")
                print_slow("BOT WINS!")
                you_are_an_idiot()
                input("")
                os.system('cls')
                print_slow("Would you like to restart the game?")
                restart = input("(yes/no): ")
                if restart == "yes":
                    print("ok")
                    print("")
                    for i in range(5):
                        time.sleep(0.55)
                        print_slow("...")
                        print("")
                    start_game()
                else:
                    time.sleep(2)
                    print_slow("ok")
                    time.sleep(1.75)
                    exit()


            os.system('cls')
            print_slow(f"{player} took {player_pile_take} from pile {player_pile_choice}")
            print(" ")
            print_numbers_horizontally(4, pile_a, pile_b, pile_c)

            player_turn = "BOT"  # Switch turn to bot
        else:
            print(" ")
            print_slow("BOT'S TURN - - - - - - - - - - - -")
            input(" ")

            pile_choice, take_amount = bot_move(pile_a, pile_b, pile_c)     #This is solely to update the numbers
            if pile_choice == 'a':
                pile_a = update_pile(pile_a, take_amount)
            elif pile_choice == 'b':
                pile_b = update_pile(pile_b, take_amount)
            elif pile_choice == 'c':
                pile_c = update_pile(pile_c, take_amount)

            if pile_a == 0 and pile_b == 0 and pile_c == 0:
                print(" ")
                print_slow("BOT IS AN IDIOT.")
                print(" ")
                print_slow(f"{player} WINS!")
                you_are_an_idiot()
                input("")
                os.system('cls')
                print_slow("Would you like to restart the game?")
                restart = input("(yes/no): ")
                if restart == "yes":
                    print("ok")
                    print("")
                    for i in range(5):
                        time.sleep(0.55)
                        print_slow("...")
                        print("")
                    start_game()
                else:
                    time.sleep(2)
                    print_slow("ok")
                    time.sleep(1.75)
                    exit()


            os.system('cls')
            print_slow(f"BOT took {take_amount} from pile {pile_choice}")
            print(" ")
            print_numbers_horizontally(4, pile_a, pile_b, pile_c)

            player_turn = player  # Switch turn to player

# STARTING BOOT SEQUENCE
def start_game():
    os.system('cls')
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  ") 
    print(" _   _ ________  ___  _____   ___  ___  ___ _____ ")
    print(r"| \ | |_   _|  \/  | |  __ \ / _ \ |  \/  ||  ___|")
    print(r"|  \| | | | | .  . | | |  \// /_\ \| .  . || |__  ")
    print(r"| . ` | | | | |\/| | | | __ |  _  || |\/| ||  __| ")        # the r's are used to turn the special text into raw strings so no special characters are interpreted
    print(r"| |\  |_| |_| |  | | | |_\ \| | | || |  | || |___ ")
    print(r"\_| \_/\___/\_|  |_/  \____/\_| |_/\_|  |_/\____/ ")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    print(" ")
    print_slow("PLEASE PLAY THIS GAME IN FULL TERMINAL MODE.")
    print(" ")
    print_slow("PRESS ENTER TO BEGIN:")
    input(" ")
    print_slow("SINGLE PLAYER OR MULTIPLAYER? (The AI is actually stupid)")
    print(" ")
    one_or_two_player = input("(single/multi): ")
    while one_or_two_player not in ["single","multi"]:
        print_slow("INVALID RESPONSE.")
        print(" ")
        one_or_two_player = input("(single/multi): ")
    if one_or_two_player == "multi":
        multiplayer()
    else:
        singleplayer()
start_game()