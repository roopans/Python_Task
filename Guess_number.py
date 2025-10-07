
import random
random_int = random.randint(1, 10)
print(random_int)
guess = int(input("Enter any number: "))
while random_int != guess:
    if random_int < guess:
        print("Too high!")
        guess = int(input("Enter number again: "))
    elif random_int > guess:
        print("Too low!")
        guess = int(input("Enter any number: "))
print("You guessed it right!!")
	