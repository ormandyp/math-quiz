import random


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


def string_checker(question, valid_answer=('yes', 'no')):
    error = f"Please enter a valid option from the list: {valid_answer}"
    while True:
        user_response = input(question).lower()
        if user_response in valid_answer or user_response in [answer[0] for answer in valid_answer]:
            return valid_answer[0] if user_response == valid_answer[0][0] else user_response
        print(error)


def instruction():
    print('''
    Welcome to the quiz! Here are the instructions:
    1. You will be asked to answer some questions.
    2. Provide your answers as prompted.
    3. The quiz will continue based on the number of questions you choose.
    4. Enjoy the quiz and try to get all answers correct!
    ''')


def random_addition_generator():
    num_1 = random.randint(0, 30)
    num_2 = random.randint(0, 30)

    correct_answer = num_1 + num_2
    print(f"What does {num_1} + {num_2} equal?")
    while True:
        try:
            user_answer = int(input("Your answer: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    return user_answer, correct_answer


# Main routine starts here
print()
print("Welcome to my quiz")
print()

# Ask user if they want to see the instructions
want_instructions = string_checker("Do you want to read the instructions? (yes/no): ")
if want_instructions in ("yes", "y"):
    instruction()

print("And now we start")

# Initialize quiz variables
rounds_played = 0
correct_answers = 0
quiz_history = []

# Ask user for number of rounds
num_rounds = int_check("How many questions would you like? ")

# Game loop starts here
while rounds_played < num_rounds:
    rounds_played += 1
    print(f"\nQuestion {rounds_played} of {num_rounds}")

    user_answer, correct_answer = random_addition_generator()

    if user_answer == correct_answer:
        print("Correct!")
        quiz_history.append(f"Round {rounds_played}: Correct")
        correct_answers += 1
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")
        quiz_history.append(f"Round {rounds_played}: Incorrect")

# Display quiz history after all Question are completed
print("\nQuiz History:")
for item in quiz_history:
    print(item)

# Calculate and display quiz statistics
total_attempts = rounds_played
percent_correct = (correct_answers / total_attempts) * 100
print("\nQuiz Statistics:")
print(f"Correct Answers: {correct_answers}")
print(f"Incorrect Answers: {total_attempts - correct_answers}")
print(f"Percentage Correct: {percent_correct:.2f}%")

print("\nQuiz over. Thanks for playing!")
