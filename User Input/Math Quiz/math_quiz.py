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


def main():
    num1 = 0
    num2 = 0
    correctAnswer = 0
    userAnswer = 0
    isActive = True
    welcome()

    while isActive:
        num1, num2 = get2Nums(1, 100)
        displayProblem(num1, num2)
        userAnswer = getAnswer(num1, num2)
        correctAnswer = num1 + num2
        showResult(correctAnswer, userAnswer)
        isActive = tryAgain()
    print("\nKeep practicing!")


def welcome():
    print("Welcome to the math practice app!")


def tryAgain() -> bool:
    while True:
        flag = input(
            "\nMore practice?\nEnter 'y' to continue or 'n' to quit: "
        ).lower()
        if flag == "y":
            return True
        elif flag == "n":
            return False
        else:
            print("\nPlease enter 'y' or 'n'")


def get2Nums(min: int, max: int) -> int:
    num1 = random.randint(min, max)
    num2 = random.randint(min, max)
    return num1, num2


def displayProblem(num1: int, num2: int) -> None:
    print()
    print(format(num1, "5"))
    print("+", end="")
    print(format(num2, "4"))


def getAnswer(num1: int, num2: int) -> None:
    while True:
        try:
            userAnswer = int(input("Enter answer: "))
            return userAnswer
        except:
            print("\nInvalid entry. Enter a valid integer.\n")
            displayProblem(num1, num2)


def showResult(correctAnswer: int, answer: int) -> None:
    if answer == correctAnswer:
        print("\nCorrect!")
    else:
        print(f"\nNot correct. Answer: {correctAnswer}")


if __name__ == '__main__':
    main()
