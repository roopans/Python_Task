
import random

unscramble_words = ['Python', 'javascript', 'java','automation','pytest','guvi','selenium']
scramble_word = random.choice(unscramble_words)
guess = input("Your guess: ")

if guess.lower() == scramble_word.lower():
    print("Correct!")
else:
    print(f"Wrong! The correct word was: {scramble_word}")