import time
import random
def joke_1():
    print("Why are skeletons so calm?")
    input("")
    print("Because nothing gets under their skin!")
    time.sleep(2)
    print("lmao")
def joke_2():
    print("What did the baby corn ask the mama corn?")
    input("")
    print("Where's my pop corn?")
    time.sleep(2.00033200042)
    print("lmao")
def joke_3():
    print("Why did the scarecrow win an award?")
    input("")
    print("Because he was outstanding in his field!")
    time.sleep(2.003200042)
    print("lmao")

def what_joke():
    print("What joke do you wanna hear bro")
    chosen_joke = input("(1/2/3/random)")
    while chosen_joke not in ["1","2","3","random"]:
        print("Invalid choice, try again")
        chosen_joke = input("(1/2/3/random)")
    if chosen_joke == "random":
        chosen_joke = str(random.randint(1, 3))
    if chosen_joke == "1":
        joke_1()
    elif chosen_joke == "2":
        joke_2()
    elif  chosen_joke == "3":
        joke_3()
    
what_joke()