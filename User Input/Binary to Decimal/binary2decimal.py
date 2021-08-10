'''
SAMPLE RUN:

  BINARY TO DECIMAL CONVERTER
-------------------------------
This program will convert binary
numbers to base 10 decimal form.

Enter a binary number: 1111 1111
11111111 in base ten decimal is: 255

Do you want to enter another?
Enter Y/n: Y

Enter a binary number: 1200
Not a valid binary.

Enter a binary number: one
Not a valid binary.

Enter a binary number: 1100 1101
11001101 in base ten decimal is: 205

Do you want to enter another?
Enter Y/n: no
Not a valid option. Try again.

Do you want to enter another?
Enter Y/n: 5
Not a valid option. Try again.

Do you want to enter another?
Enter Y/n: y

Enter a binary number:
Not a valid binary.

Do you want to enter another?
Enter Y/n: n

Thank you. Goodbye!
'''


def main():
    isActive = True
    welcome()
    while isActive:
        binary = getBinary()
        decimal = calculateBinary(binary)
        print(f'{binary} in base ten decimal is: {decimal}')
        isActive = promptToCont()
    print('\nThank you. Goodbye!')


def welcome():
    print('\n  BINARY TO DECIMAL CONVERTER')
    print('-'*31)
    print('This program will convert binary\nnumbers to base 10 decimal form.')


def getBinary() -> str:
    binaryNum = None
    while True:
        binaryNum = input('\nEnter a binary number: ').replace(' ', '')
        try:
            if len(binaryNum) < 1:
                raise ValueError
            for i in binaryNum:
                if i in '01':
                    pass
                else:
                    raise ValueError
            return binaryNum
        except Exception:
            print('Not a valid binary.')


def calculateBinary(binary: str) -> int:
    value = 0
    binaryValues = listBinaryValues(len(binary))
    for i in range(len(binary)):
        if binary[i] == "1":
            value += binaryValues[i]
    return value


def listBinaryValues(n: int) -> list:
    binValues = []
    for i in range(n):
        binValues.insert(0, 2**i)
    return binValues


def promptToCont() -> bool:
    option = None
    while True:
        print('\nDo you want to enter another?')
        option = input('Enter Y/n: ').lower()
        if option == 'y':
            return True
        elif option == 'n':
            return False
        else:
            print('Not a valid option. Try again.')


if __name__ == '__main__':
    main()
