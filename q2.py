#Number Guessing Game

import random
num = random.randint(1,100)

while True:
    your_num = int(input("Enter a number between 1 and 100: "))
    if num == your_num:
        print("Congratulations! You won...")
        break
    elif num > your_num:
        print("Your prediction is low")
    elif num < your_num:
        print("Your prediction is high")
    else:
        print("invalid prediction")
    
    