
def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more."

        to_check = input(question)

        try:
            response = int(to_check)

            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main routine stats here

# Intialise game variables
mode = "regular"
rounds_played = 0


# Ask user for number of rounds?
num_rounds = int_check("How many rounds would you like? ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5


# game loop starts here
while rounds_played < num_rounds:

    # rounds headings
    if mode == "infinite":
        rounds_heading = f"\n Round {rounds_played + 1} (Infinite Mode) "
    else:
        rounds_heading = f"\n Round {rounds_played + 1} of {num_rounds} "

    print(rounds_heading)
    print()

    user_choice = input("choose : ")

    if user_choice == "xxx":
        break

    rounds_played += 1
    print("rounds played: ", rounds_played)

    # if user are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1


# Game loop ends here

# Game history / Statistics area
