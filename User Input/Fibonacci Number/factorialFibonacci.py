def getFactorial(num):
    n = 1
    for i in range(1, num + 1):
        n = n * i
    return n


def getFibonacci(position):
    fibCurrent = 1
    fibLast = 1

    for i in range(1, position):
        fibNext = fibCurrent + fibLast
        fibLast = fibCurrent
        fibCurrent = fibNext
    return fibCurrent


def getInt():
    while True:
        try:
            return int(input(': '))
        except:
            print('\nPlease enter a valid integer.')


def playAgain():
    print('Would you like to go again?')
    while True:
        choice = input("Enter Y/n: ").lower()
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("Not a valid answer.")


def mainMenu():
    active = True
    while active:
        print(f"\n{'-'*10} MENU {'-'*10}")
        print("1. Find a factorial\n2. Find a fibonacci number\n3. Exit")
        choice = getInt()
        if choice not in range(1, 4):
            print("Not a valid option.")
            continue
        if choice == 1:
            print('\nEnter a number to find the factorial.')
            print(f'The factorial is {getFactorial(getInt())}')
        elif choice == 2:
            print('\nEnter a number to find the fibonacci number.')
            print(f'The fibonacci number is {getFibonacci(getInt())}')
        elif choice == 3:
            print('\nThank you. Bye')
            break
        else:
            print('\nPlease enter a valid option.')
        active = playAgain()


def main():
    '''This program asks for an interger and prints the factorial of the integer'''
    # print(f"The factorial of {num} is {'{:,}'.format(getFactorial(num))}")
    # print(f'The number {getFactorial(num)} is {len(str(getFactorial(num)))} digits long.')
    print("Hello, let's do some stuff!")
    mainMenu()


if __name__ == '__main__':
    main()
