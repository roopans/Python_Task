
import random

words = ['Python', 'javascript', 'java','automation','pytest','guvi','selenium']
word = random.choice(words)
jumbled = ''.join(random.sample(word, len(word)))

print("Unscramble the word:", jumbled)
guess = input("Your guess: ")

if guess.lower() == word.lower():
    print("Correct!")
else:
    print(f"Wrong! The correct word was: {word}")