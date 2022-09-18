

import random

def guess(x):

    random_number = random.randint(1 , x)

    guess = 0
    while guess != random_number : 
        guess = int(input(f"guess a number melan 1 and {x}:"))
        if guess < random_number :
            print ("sorry is high")
        elif guess > random_number:
            print("no law")

    print(f"yeeeey {guess}")


guess(5) 


