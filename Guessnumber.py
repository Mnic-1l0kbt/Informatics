#Gues number game
import random
comp_guess = random.randint(1,10)
number_of_attempts = 0
while True :
    try:
        user_guess = int(input("Please guess the number: "))

        if comp_guess == user_guess :
            number_of_attempts = number_of_attempts + 1
            print(f' You won in {number_of_attempts} attempts.')
            break 
        elif user_guess < comp_guess :
            print("Too Low")
            number_of_attempts = number_of_attempts + 1

        else:
            print("Too High")
            number_of_attempts = number_of_attempts + 1
    except:
            print("Choose number between 1 to 100")