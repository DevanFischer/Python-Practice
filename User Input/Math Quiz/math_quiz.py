"""
Welcome to the math practice app

    4
+   4
Enter answer: 8

Correct!

More practice? Enter 'y' to continue: y

    9
+   6
Enter answer: 7

Not correct. Answer: 15

More practice? Enter 'y' to continue: n

Keep practicing!
"""

import random

# main function
def main():
    # Local variables
    num1 = 0
    num2 = 0
    correctAnswer = 0
    userAnswer = 0
    flag = "y"

    # Display welcome message
    welcome()

    while flag == "y":

        # Get two random numbers
        num1, num2 = get2Nums(1, 100)

        # Display math problem
        displayProblem(num1, num2)

        # Get user answer
        userAnswer = getAnswer(num1, num2)

        # Calculate correct answer
        correctAnswer = num1 + num2

        # Display result
        showResult(correctAnswer, userAnswer)

        # Ask user if they want to continue
        flag = input(
            "\nMore practice?\nEnter 'y' to continue or 'n' to quit: "
        ).lower()
        if flag != "y" and flag != "n":
            print("\nPlease enter 'y' or 'n'")
            flag = input(
                "\nMore practice?\nEnter 'y' to continue or 'n' to quit: "
            ).lower()

    print("\nKeep practicing!")


# Show a welcome message
def welcome():
    print("Welcome to the math practice app!")


# The get2Nums function takes in two arguments, min and max.
# Then returns two random integers in that range.
def get2Nums(min, max):
    num1 = random.randint(min, max)
    num2 = random.randint(min, max)
    return num1, num2


# The displayProblem function accepts the numbers
# and displays them
def displayProblem(num1, num2):
    print()
    print(format(num1, "5"))
    print("+", end="")
    print(format(num2, "4"))


# The getAnswer function gets and returns the user answer
def getAnswer(num1, num2):
    while True:
        try:
            userAnswer = int(input("Enter answer: "))
            return userAnswer
        except:
            print("\nInvalid entry. Enter a valid integer.\n")
            displayProblem(num1, num2)


# The showResult function tells if user answer is correct or not
def showResult(correctAnswer, answer):
    if answer == correctAnswer:
        print("\nCorrect!")
    else:
        print(f"\nNot correct. Answer: {correctAnswer}")


# Call the main function.
main()
