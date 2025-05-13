import random

words = ['python', 'internship', 'hangman', 'programming', 'codealpha']
word = random.choice(words)
guesses = ''
turns = 6

print("Welcome to Hangman!")
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    print()

    if failed == 0:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Guess a letter: ").lower()
    if guess in guesses:
        print("You already guessed that!")
        continue

    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong guess. You have", turns, "guesses left.")
        if turns == 0:
            print("Game Over! The word was:", word)
