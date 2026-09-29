import random

# List of 5 predefined words
words = ["python", "computer", "program", "science", "college"]

# Select a random word
word = random.choice(words)

# Display underscores for each letter
guessed_word = ["_"] * len(word)

# Maximum incorrect guesses
max_wrong = 6
wrong_guesses = 0

# Store guessed letters
guessed_letters = []

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.")

while wrong_guesses < max_wrong and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Wrong guesses:", wrong_guesses, "/", max_wrong)

    guess = input("Enter a letter: ").lower()

    # Check for valid input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check whether letter is in the word
    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        wrong_guesses += 1
        print("Wrong guess!")

# Game result
if "_" not in guessed_word:
    print("\nCongratulations! 🎉")
    print("You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The correct word was:", word)