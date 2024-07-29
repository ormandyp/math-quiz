import random

def random_addition_generator():
    num_1 = random.randint(0, 20)
    num_2 = random.randint(0, 20)
    correct_answer = num_1 + num_2

    print()
    print(f"What does {num_1} + {num_2} equal?")
    user_answer = int(input("Your answer: "))

    if user_answer == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")

def string_checker(question, valid_ans=('yes', 'no')):
    error = f"Please enter a valid option from the list: {valid_ans}"

    while True:
        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # Check if the user response is a word in the list
            if item == user_response:
                return item

            # Check if the user response is the same as the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # Print error if user does not enter something that is valid
        print(error)
        print()

def instruction():
    print('''
    Welcome to the quiz! Here are the instructions:
    1. You will be asked to answer some questions.
    2. Provide your answers as prompted.
    3. The quiz will continue based on the number of rounds you choose.
    4. Enjoy the quiz and try to get all answers correct!
    ''')

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

# Main routine starts here
print()
print("Welcome to my quiz")
print()

# Ask user if they want to see the instructions
want_instructions = string_checker("Do you want to read the instructions? ")

if want_instructions == "yes":
    instruction()

    print("And now we start")
else:

    print("I hope you know what you're doing")

# Initialize game variables
mode = "regular"
rounds_played = 0

# Ask user for number of rounds
num_rounds = int_check("How many rounds would you like? ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:
    # Round headings
    if mode == "infinite":
        rounds_heading = f"\nRound {rounds_played + 1} (Infinite Mode)"
    else:
        rounds_heading = f"\nQuestion {rounds_played + 1} of {num_rounds}"

    print(rounds_heading)
    print()

    random_addition_generator()

    rounds_played += 1
    print(f"Rounds played: {rounds_played}")

    # If users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

    # Output Game Statistics
    print(" Game Statistics ")
    print(f"👍 Won: {percent_won:.2f} \t "
          f"😥 lost: {percent_lost:.2f} \t "
          f" Tied: {percent_tied:.2f}")

    # ask user if thay want to see their game history and output it if requested.
    see_history = string_checker("\nDo you want to see your game history? ")
    if see_history == "yes":
        for item in game_history:
            print(item)

    print()
    print("Thanks for playing.")

else:
    print("oops - You chickened out!")


print("Game over. Thanks for playing!")