import random
LOWER_BOUND = 1
UPPER_BOUND = 100
HIGH_SCORE_DEFAULT = 9999999
def start_game():
      # 2. Store a random number as the answer/solution.
    random_number_to_guess = random.randint(LOWER_BOUND, UPPER_BOUND)
    high_score = HIGH_SCORE_DEFAULT
    # write your code inside this function.
    # As a player of the game, I should see a some kind of text header, welcome or game intro message, before or above the menu.
    # 1. Display an intro/welcome message to the player.
    print("""Welcome to the Number Guessing Game...It is Guesstacular!
          The object is to guess a number between 1 and 100.
          """)
    while True:
        random_number_to_guess = random.randint(LOWER_BOUND, UPPER_BOUND)
        turns_taken = 1
        if high_score != HIGH_SCORE_DEFAULT:
            print("The current high score is: {}".format(high_score))
        #As a player of the game, I should be continuously prompted for a guess until I get it right.
        while True:
            #The following is pretty key for debugging
            #print("random number is: {}".format(random_number_to_guess))
            #Make sure your script runs without errors. Catch exceptions and report errors to the user in a meaningful way.
            try:
                current_guess = int(input("Please enter your guess between {} and {}: ".format(LOWER_BOUND,UPPER_BOUND)))
                #As a player of the game, my guess should be within the number range. If my guess is outside the guessing range I should be told to try again.
                if (current_guess > UPPER_BOUND or current_guess < LOWER_BOUND):
                    print('Please stay within the lower bound of {} and the upper bound of {}.'.format(LOWER_BOUND,UPPER_BOUND))
                    turns_taken += 1
                # 4. Once the guess is correct, stop looping, inform the user they "Got it" and show how many attempts it took them to get the correct number.
                elif (current_guess == random_number_to_guess):
                    #  5. Let the player know the game is ending, or something that indicates the game is over.
                    #As a player of the game, after the game ends I should be shown my number of attempts at guessing.
                    print('You got it and the game is over (you needed {} guesses) but remember: "It is one thing to be clever and another to be wise." '.format(turns_taken))
                    #As a player of the game, at the start of each game I should be shown the current high score (least amount of points), so that I know what I am supposed to beat.
                    if turns_taken < high_score:
                        high_score = turns_taken
                    break
                # As a player of the game, after an incorrect guess I should be told if my answer is higher or lower than the answer, so that I can narrow down my guesses.
                elif (current_guess > random_number_to_guess):
                    print('It is lower.')
                    turns_taken += 1
                elif (current_guess < random_number_to_guess):
                    print('It is higher.')
                    turns_taken += 1
            except ValueError:
                print("Not a number between 1 and 100...")
    #As a player of the game, after I guess correctly I should be prompted if I would like to play again.
        play_again = input("Enter 'Y' if you would like to play again, enter any other key(s) if you don't")
        if play_again.lower() != "y":
            print("Fare the well. History is a wheel, for the nature of man is fundamentally unchanging. What has happened before will perforce happen again.")
            break
if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
