import random


word_list = ['apple', 'mango', 'grape', 'peach', 'lemon']


word_to_guess = random.choice(word_list)
guessed_letters = []
attempts_left = 6


print("🎮 Welcome to Hangman!")
print("Guess the word letter by letter.")
print("_ " * len(word_to_guess))  

while attempts_left > 0:
    guess = input("Enter a letter: ").lower()

    
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter a single alphabetic character.")
        continue

    
    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    
    guessed_letters.append(guess)

    
    if guess in word_to_guess:
        print("✅ Good guess!")
    else:
        attempts_left -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts_left}")

    
    display_word = ''
    for letter in word_to_guess:
        if letter in guessed_letters:
            display_word += letter + ' '
        else:
            display_word += '_ '
    print(display_word.strip())

    
    if all(letter in guessed_letters for letter in word_to_guess):
        print("🎉 Congratulations! You guessed the word correctly!")
        break


if attempts_left == 0:
    print("💀 Game Over! The word was:", word_to_guess)
