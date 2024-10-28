def multi_table(user_num):
    print(f"MULTIPLICATION TABLE OF {user_num}:")
    print("")
    for i in range(1, 13):
        print(f"{user_num} x {i} = {int(user_num) * i}")

def give_positive():  
    user_num = input("Give a positive integer: ")
    if int(user_num) < 0:
        user_num = input("Give a positive integer: ")
    if int(user_num) > 0:
        multi_table(user_num)
give_positive()