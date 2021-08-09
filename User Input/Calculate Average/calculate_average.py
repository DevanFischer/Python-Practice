"""
SAMPLE RUN:

This program will let you enter two or more numbers then prints the average and sum

Enter a number, or done: 5

Enter a number, or done: 3

Enter a number, or done: 7

Enter a number, or done: g
Invalid entry, please try again.

Enter a number, or done: 4.6

Enter a number, or done: done

Thank you!
You entered the numbers 5, 3, 7, 4.6

The total is 19.6

The average is 4.90
"""


def main():
    welcomeMsg()
    numList = getNums()
    numSum = addNums(numList)
    avg = getAvg(numList)
    printNums(numList)
    print(f"\nThe total is {numSum}")
    print(f"\nThe average is {avg}")


def welcomeMsg():
    print(
        "\nThis program will let you enter two or more numbers then prints \
the average and sum"
    )


def getNums():
    numList = []
    while True:
        userNum = input("\nEnter a number, or done: ")
        if userNum == "done":
            if len(numList) < 2:
                print(
                    f"You did not enter enough numbers.\
        \nPlease try again."
                )
            else:
                print("\nThank you!")
                break
        elif userNum == "":
            print("Invalid entry.")
        else:
            try:
                num = float(userNum)
                if num.is_integer():
                    num = int(num)
                numList.append(num)
            except:
                print("Invalid entry, please try again.")
    return numList


def addNums(numList):
    total = 0.0
    for num in numList:
        total += num
    if total.is_integer():
        return int(total)
    else:
        return total


def getAvg(numsList):
    avg = 0.0
    avg = addNums(numsList) / len(numsList)
    if avg.is_integer():
        return int(avg)
    else:
        return format(avg, ".2f")


def printNums(numList):
    print(f'You entered the numbers {", ".join(str(n) for n in numList)}')


if __name__ == '__main__':
    main()
