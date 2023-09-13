import random
def check_guess(secret, guess):
    correct_digits = sum(
        [1 for i in range(len(secret)) if secret[i] == guess[i]])
    return correct_digits

def main():
    print("\nWelcome to the Sync Interns Mastermind game!")
    print("--------------------------------------------------\n")

    # Player 1 sets a multi-digit number
    player1_number = input("Player 1,  Enter a Number :- ")

    # Player 2 guesses Player 1's number
    player2_attempts = 0
    while True:
        player2_guess = input("Player 2 , Guess the Number :- ")
        player2_attempts += 1

        if player2_guess == player1_number:
            print(
                f"Player 2 makes the guess in {player2_attempts} attempts!\n")
            break
        else:
            correct_digits = check_guess(player1_number, player2_guess)
            print(f"Hint: {correct_digits} Digits are correct in your Guess\n")

    # Player 2 sets a multi-digit number
    player2_number = input("Player 2,  Enter a Number :- ")

    # Player 1 guesses Player 2's number
    player1_attempts = 0
    while True:
        player1_guess = input("Player 1, Guess the Number :- ")
        player1_attempts += 1

        if player1_guess == player2_number:
            print(
                f"Player 1 makes the guess in {player1_attempts} attempts!")
            break
        else:
            correct_digits = check_guess(player2_number, player1_guess)
            print(f"Hint: {correct_digits} Digits are correct in your Guess\n")

    # Determine the winner
    if player1_attempts < player2_attempts:
        print("\nPlayer 1 Wins and Crowned Mastermind !\n")
    elif player1_attempts > player2_attempts:
        print("\nPlayer 2 Wins and Crowned Mastermind !\n")
    else:
        print("Match Draw !! ")


if __name__ == "__main__":
    main()
