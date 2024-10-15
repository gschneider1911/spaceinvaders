"""-------------------------------------------------------------
Name: Gabe Schneider
Course: CS 1430, Section X, Fall 2024
Purpose: Assignment 2 - Twist - A - Plot
         This program is an invader game where you navigate different branches
         1) Easy math game focused on addition.
         2) A randomized math game with various operations.
         3) TensorFlow output simulation for machine leraning results.

         Users provide input for mode selection (easy or hard)

Input:   Users input integers to answer math problems or select paths.
         Mode selection allows users to choose between easy/hard

Output: The program has three branches based on user input:
        Branch 1 (Addition Game): The user is presented with a series of addition problems. Correct answers earn points
        Branch 2 (Randomized Math Game): The user faces random math operations
        Branch 3 (Outputs and TensorFlow): The user can view TensorFlow outputs by simulating  predictions.
-------------------------------------------------------------"""

import os
import random
import sys

#############
# GABES AMAZING CONSTANTS
############
_CHAPTER_LINE = "=" * 50
_ADDITION = 1
_RANDOM = 2
_OUTPUTS = 3
_EASY = 1
_HARD = 2
_POINTS_TO_WIN = 1  # Changed the required points to win from 5 to 10


# Write problem and solution to a file
def log_problem_to_file(problem, user_answer, correct_answer, correct):
    with open("game_data.txt", "a") as f:
        f.write(f"{problem},{user_answer},{correct_answer},{correct}\n")


# Addition only game mode
def addition_algo(integer_a, integer_b):
    # Create and print the problem/pass the string to be returned
    problem = f"{integer_a} + {integer_b}"
    print(problem)

    # Get the correct answer
    correct_answer = integer_a + integer_b

    return correct_answer, problem

# Subtraction Algorithm
def subtraction_algo(integer_a, integer_b):
    # Some addition algo code with the operator changed
    problem = f"{integer_a} - {integer_b}"
    print(problem)
    correct_answer = integer_a - integer_b
    return correct_answer, problem

# Multiplication Algorithm
def multiplication_algo(integer_a, integer_b):
    # Some addition algo code with the operator changed
    problem = f"{integer_a} * {integer_b}"
    print(problem)
    correct_answer = integer_a * integer_b
    return correct_answer, problem

# Modulus Algorithm
def modulus_algo(integer_a, integer_b):
    # This took forever to figure out to resolve zerodivision
    if integer_b == 0:
        print("Cannot modulus by zero!")
        return None, None
    # Modulus this time
    problem = f"{integer_a} % {integer_b}"
    print(problem)
    correct_answer = integer_a % integer_b
    return correct_answer, problem


# Main addition game function
def addition_game(mode, user_points=0):
    os.system("cls")
    print(f"Total points: {user_points}")

    if user_points >= _POINTS_TO_WIN:  # Use the defined constant here
        print(f"Game over! You reached {_POINTS_TO_WIN} points and exterminated the aliens. Final score: {user_points}")
        sys.exit()
    # Automatically switches to 100 so code isn't so redundant
    max_num = 10 if mode == _EASY else 100

    integer_a = random.randint(1, max_num)
    integer_b = random.randint(1, max_num)

    print("Exterminate the aliens with addition!")
    correct_answer, problem = addition_algo(integer_a, integer_b)

    while True:
        try:
            user_answer = int(input("Fire away ==> "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    correct = user_answer == correct_answer
    log_problem_to_file(problem, user_answer, correct_answer, int(correct))
    # Check if correct
    if correct:
        user_points += 1
        print("Correct! You've earned a point.")
    else:
        print("Incorrect! No points earned this round.")

    addition_game(mode, user_points)


# Random algo game mode
def random_algo(mode, user_points=0):
    os.system("cls")
    print(f"Total points: {user_points}")

    if user_points >= _POINTS_TO_WIN:  # Use the defined constant here
        print(f"Game over! You reached {_POINTS_TO_WIN} points and exterminated the aliens. Final score: {user_points}")
        sys.exit()
    # Automatically switches to 100 so code isn't so redundant
    max_num = 10 if mode == _EASY else 100
    # Random int generator
    integer_a = random.randint(1, max_num)
    integer_b = random.randint(1, max_num)

    # Specify the operators and use random function again to choose
    operators = ['+', '-', '*', '%']
    selected_operator = random.choice(operators)

    # If elif sign shenanigans
    if selected_operator == '+':
        correct_answer, problem = addition_algo(integer_a, integer_b)
    elif selected_operator == '-':
        correct_answer, problem = subtraction_algo(integer_a, integer_b)
    elif selected_operator == '*':
        correct_answer, problem = multiplication_algo(integer_a, integer_b)
    elif selected_operator == '%':
        correct_answer, problem = modulus_algo(integer_a, integer_b)
        if correct_answer is None:
            random_algo(mode, user_points)
            return

    print(f"Operation: {integer_a} {selected_operator} {integer_b}")

    # Very painful to program without crashing :(
    while True:
        try:
            user_answer = int(input("Fire away ==> "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    correct = user_answer == correct_answer
    # Log problem to the file for later use in TensorFlow
    log_problem_to_file(problem, user_answer, correct_answer, int(correct))

    # Check if correct and add a point
    if correct:
        user_points += 1
        print("Correct! You've earned a point.")
    else:
        print("Incorrect! No points earned this round.")

    random_algo(mode, user_points)


# Outputs and TensorFlow algorithm
def outputs_algo():
    os.system("cls")
    os.system("python train.py")
    print("Thank you for using adding data into the TensorFlow Algorithm!")


def main():
    # Start by allowing the user to choose easy and hard mode
    print(_CHAPTER_LINE)
    print("Welcome to Space Invaders 2.0 :))))")
    print(_CHAPTER_LINE)
    print("1: Easy Mode\n"
          "2: Hard Mode\n")
    mode = int(input("Please Select Mode (1 = Easy, 2 = Hard) ==> "))

    # Basic inclusion statement to prevent people from choosing invalid mode
    if mode not in [_EASY, _HARD]:
        print("Invalid mode. Please enter 1 for Easy or 2 for Hard.")
        return

    print(_CHAPTER_LINE)
    print("1: Addition = Only use input\n"
          "2: Random = Use all the firepower\n"
          "3: Outputs = View TensorFlow predictions")
    print(_CHAPTER_LINE)
    # I forgot to cast this to an int at first and had a bug that lasted hours
    game_mode = int(input("Please Select Game Mode (1,2,3) ==> "))
    # Check gamemodes
    if game_mode == _ADDITION:
        addition_game(mode)
    elif game_mode == _RANDOM:
        random_algo(mode)
    elif game_mode == _OUTPUTS:
        outputs_algo()
    else:
        print("Please enter an integer between 1 and 3")

# This rubber duck will take up most of the program hehe
"""                           
                                            ██████████                                  
                                      ░░  ██░░░░░░░░░░██                                
                                        ██░░░░░░░░░░░░░░██                              
                                        ██░░░░░░░░████░░██████████                      
                            ██          ██░░░░░░░░████░░██▒▒▒▒▒▒██                      
                          ██░░██        ██░░░░░░░░░░░░░░██▒▒▒▒▒▒██                      
                          ██░░░░██      ██░░░░░░░░░░░░░░████████                        
                        ██░░░░░░░░██      ██░░░░░░░░░░░░██                              
                        ██░░░░░░░░████████████░░░░░░░░██                                
                        ██░░░░░░░░██░░░░░░░░░░░░░░░░░░░░██                              
                        ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                            
                        ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                            
                        ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                            
                        ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                            
                        ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                            
                        ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                              
                          ██░░░░░░░░░░░░░░░░░░░░░░░░░░██                                
                            ██████░░░░░░░░░░░░░░░░████                                  
                                  ████████████████                                      

"""

if __name__ == "__main__":
    main()
