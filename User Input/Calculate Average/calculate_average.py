# *****************************************************************************
# Author:           Devan Fischer
# Lab:              Assignment 03 - Conditional Statements
# Date:             2021 Jul 13
# Description:      This program adds up entered numbers and outputs the sum
#                   and average
# Input:            Variable userNum accepts float, int or the string "done"
# Output:           Print statement containing average and sum of user input
#                   (floats or integers)
# Sources:          Assignment 3 Guidlines, W3schools.com, stackoverflow.com
# *****************************************************************************


"""
SAMPLE RUN:

This program will let you enter two or more numbers then prints the average
and sum

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

"""
PSEUDOCODE:

Module main()
    Call welcomeMsg()
    Declare List numList
    Set numList = getNums()
    Declare Real numSum
    Set numSum = addNums(numList)
    Declare Real avg
    Set avg = getAvg(numsList)
    Call printNums(numList)
    Display "The total is", numSum
    Display "The average is", avg
End Module

Function String welcomeMsg()
    Display "This program will let you enter two or more numbers then prints \
    the average and sum"
End Function

Function List getNums()
    Declare List numList
    Declare Real userNum
    while True
        Display "Enter a number, or done: "
        Input userNum
        If userNum = "done" Then
            If length of numList < 2 Then
                Display "You did not enter enough numbers. Please try again."
            Else
                Display "Thank You!"
                Break
            End If
        Else If userNum = "" Then
            Display "Invalid Entry"
        Else
            Try
                Declare Real num
                Set num = Float userNum
                If num is a Integer Then
                    Set num = Integer num
                End If
                Add num to numList
            Except
                Display "Invalid entry, please try again"
        End If
    Return NumList
End Function

Function Real addNums(numList)
    Declare Real total
    For each num in numList Do
        Set total = total + num
    End For
    If total is a Integer Then
        Return Integer total
    Else
        Return Real total
    End If
End Function

Function Real getAvg(numList)
    Declare Real avg
    Set avg = addNums(numList) / length of NumList
    If avg is a Integer then
        Return Integer avg
    Else
        Return Real avg
    End If
End Function

Function String printNums(numList)
    Display "You entered the numbers", (number for number in numList)
End Function

Call main()
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


main()
