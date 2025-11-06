import random

with open("words.txt", "r") as file:
    words = [line.strip().lower() for line in file if line.strip()]

word = random.choice(words)

guessed_word = list("_" * len(word))

display_guessed_word = "".join(guessed_word)

attempts = 10

while attempts > 0:

    print("Current Word:", " ".join(guessed_word))

    guess = (input("Guess a letter: ")).lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("Great guess!") 
    else:
        attempts -= 1
        print("Wrong guess! Attempts left ", attempts)

    if "_" not in guessed_word:
        print(f"Congratulations! You guessed the word: {word}")
        break

    if "_" in guessed_word and attempts == 0:
        print(f"You've run out of attempts! The word was: {word}")

    


