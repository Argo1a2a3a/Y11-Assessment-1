import random
import requests

words_text = requests.get("https://raw.githubusercontent.com/tabatkins/wordle-list/refs/heads/main/words").content
words = words_text.decode('utf-8').split()  
word_to_guess = random.choice(words)

guessed_word = ["="] * len(word_to_guess)
attempts = 12

print("Welcome to Hangman!")
print("Guess the word:", " ".join(guessed_word))

while attempts > 0 and "=" in guessed_word:
    guess = input("Guess a letter: ").lower()

    if guess in word_to_guess:
        for i, letter in enumerate(word_to_guess):
            if letter == guess:
                guessed_word[i] = guess
        print("Correct!")
    else:
        attempts -= 1
        print(f"Incorrect! {attempts} attempts remaining.")

    print("Guess the word:", " ".join(guessed_word))

if "=" not in guessed_word:
    print("Congratulations! You guessed the word:", word_to_guess)
else:
    print("Game over! The word was:", word_to_guess)