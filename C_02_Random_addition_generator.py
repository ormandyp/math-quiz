import random


def random_addition_generator():
    num_1 = random.randint(0, 30)
    num_2 = random.randint(0, 30)
    correct_answer = num_1 + num_2

    print(f"What does {num_1} + {num_2} equal?")
    user_answer = int(input("Your answer: "))

    if user_answer == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")


