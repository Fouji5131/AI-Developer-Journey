import random

def get_valid_guess():
     while True:                          # keep asking until valid input
        try:
            guess = int(input("Guess the number between 1 and 10: "))
            return guess                 # only reaches here if int() succeeded
        except ValueError:
            print("Please enter a valid number!")

def check_guess(guess_value, secret_number, attempts, max_attempts):
        remaining = max_attempts - attempts
        
        if guess_value == secret_number:
            print(f"Congratulations! You got it in {attempts} attempt(s)!")
            return "win"
        elif guess_value < secret_number:
            print(f"Too low! {remaining} attempt(s) left.")
            return "low"
        else:
            print(f"Too high! {remaining} attempt(s) left.")
            return "high"
            
def play_game():
    secret_number = random.randint(1, 10)
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        # Step 1: get valid input only
        guess = get_valid_guess()

        attempts += 1

        # Step 2: now process the guess (only reaches here if input was valid)
        result = check_guess(guess, secret_number, attempts, max_attempts)

        if result == "win":
            break   
    else:
        # Runs only if the inner while finishes without break (no win)
        print(f"Sorry, out of attempts! The number was {secret_number}.")

def main():
    while True:
        try:
            play_game()

            play_again = input("If you want to play again, type 'y' or 'n': ").strip().lower()

            if play_again != 'y':
                print("Thanks for playing. Goodbye!")
                break
            
        except KeyboardInterrupt:
            print("\nGame interrupted. Goodbye!")
            break

if __name__ == "__main__":
    main()