import random


def random_addition_generator():
    num_1 = random.randint(0, 30)
    num_2 = random.randint(0, 30)
    correct_answer = num_1 + num_2

    print(f"What does {num_1} + {num_2} equal?")

    while True:
        try:
            user_answer = int(input("Your answer: "))
            break  # Exit the loop if input is successfully converted to an integer
        except ValueError:
            print("Invalid input. Please enter a number.")

    if user_answer == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")
