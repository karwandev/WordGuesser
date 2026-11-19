import random
with open("word_list.txt", "r", encoding="utf-8") as file:
    content = file.read().splitlines()

secret_word = random.choice(content).casefold() #1.1.2 BUG FIXED

lives = 6
score = 0
version = "1.2.0"

def game():
    lives_remaining = lives
    print(f"Game Started\nRules: you have {lives_remaining} lives to guess the 5-letter word.")
    # Keep each guess's letters and feedback so earlier rows stay visible on later turns.
    guess_history = []
    while lives_remaining > 0:
        display = ["_", "_", "_", "_", "_"]
        guess = input("Enter a 5-letter guess: ").strip().casefold()
       # If Guess exceeds the number of words allowed (5). Will be called out and dismissed. 
        if len(guess) != 5:
            print("Your guess must be 5 letters. No life lost.")
            continue

        for i in range(5):
            # If Guess word, here represented by  "[i]" is in the word AND in correct position ("==")
            if guess[i] == secret_word[i]:
                display[i] = "🟢"
            elif guess == "karwa":
                print(f"Pss, dont tell anyone but the word is: ", secret_word)
            # If Guess word, here represented by  "[i]" is in ("in") the word but IS NOT in correct positon    
            elif guess[i] in secret_word:
                display[i] = "🟨"
            # If Guess word, here represented by  "[i]" is NOT in the word AT ALL.
            else:
                display[i] = "⬜"

        # Match each letter's cell width to its square so the feedback sits beneath it.
        letters_row = "".join(f" {letter.upper()} " for letter in guess)
        feedback_row = "".join(f"{feedback} " for feedback in display)
        guess_history.append(f"{letters_row}\n{feedback_row}")
        # Redraw all rows after each guess so previous feedback remains on the board.
        print("\n".join(guess_history))

        if guess == secret_word:
            print("You guessed the word! You win!")
            global score
            score += 1
            print(f"Your score is", score)
            lobby()
            return

        # Only valid guesses that do not solve the word use a life.
        lives_remaining -= 1
        print(f"Lives remaining: {lives_remaining}")

    print(f"You're out of lives! The word was {secret_word.upper()}.")
    lobby()


def lobby():
    while True:
        welcome = input("Hello, welcome to MyWordle by Karwan, start game?\n1. Yes\n2. No\n3. View My Score.\n4. Version\n").casefold()
        if welcome in {"1", "yes"}:
            print("started")
            game()
            break

        elif welcome in ("2", "no"):
            print("Game Not Started. but you can alwasy start.")
        elif welcome in ("3", "View My Score"):
            print(f"your score is",score)    
        elif welcome in ("4", "version"):
            print(f"\nThe game version is: ",version)


lobby()
