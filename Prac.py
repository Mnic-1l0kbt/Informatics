#Variables
#camel case
#snakecase
#pascalcase
#global key word, number
#strings len slicing
#Logical operators and, or, and not
#comparison operators 

from calendar import c


user_weight=input("Weight:")
unit_of_weight=input("(L)bs or (K)Kg:")

if unit_of_weight.upper=="L":
    converted=unit_of_weight * 0.45
    print(f"You are {converted} Kgs")

else:
    converted=unit_of_weight/ 0.45
    print(f"You are {converted} bs")

