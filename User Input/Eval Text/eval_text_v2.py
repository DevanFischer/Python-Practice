from string import punctuation
import platform


def main():
    welcomeMsg()
    userInput = getText()
    menu(userInput)


def welcomeMsg():
    clearScrn()
    print(
        '\nHello, this program will analyze some text for you.'
    )


def getText():
    userInput = ''
    userInput = input('\nEnter some text: ')
    return userInput


def menu(userInput):
    MENU_OPTIONS = {
        1: "Most Used Words",
        2: "Unique Pairs",
        3: "Enter New Text",
        4: "Quit"
    }
    clearScrn()
    while True:
        print(f"\n{'-'*15}MENU{'-'*15}")
        for pair in MENU_OPTIONS.items():
            print(": ".join(str(i) for i in pair))
        try:
            option = int(input("\nPlease choose an option: "))
            if option == 1:
                printTop(countWords(userInput))
            elif option == 2:
                printTop(findPairs(listWords(userInput)))
            elif option == 3:
                userInput = getText()
            elif option == 4:
                clearScrn()
                print("\nThank you for using this program. Goodbye!")
                break
            else:
                print(f"\nPlease enter 1 - {len(MENU_OPTIONS)}")
        except:
            print("\nInvalid Option. Please try again")


def listWords(text):
    output = ''
    text = text.lower()
    for char in text:
        if char not in punctuation:
            output += char
    # Convert output from a string to a list containing each word
    output = output.split()
    return output


def countWords(wordsList):
    wordsList = listWords(wordsList)
    wordCounts = {}
    for word in wordsList:
        if word not in wordCounts:
            wordCounts[word] = 1
        else:
            wordCounts[word] += 1
    return wordCounts


def findPairs(results):
    """ Finds all the pairs of words that occur, prints the top 10, and returns a dict. """
    unique_pairs = {}

    for word in range(len(results)-1):
        pair = str(results[word] + ' ' + results[word+1])
        if pair not in unique_pairs:
            unique_pairs[pair] = 1
        else:
            unique_pairs[pair] += 1
    return unique_pairs


def getValidInt():
    while True:
        try:
            return int(input("\nHow many would you like to see? "))
        except:
            print("\nPlease enter a valid integer.")


# Prints out the top ten words in the dictionary
def printTop(dict):
    count = getValidInt()
    clearScrn()
    # Set dictionary to a list of touples
    wordList = list(dict.items())
    # Sort the list in descending order based on value
    wordList.sort(key=lambda tup: tup[1], reverse=True)
    if len(wordList[0][0].split(" ")) == 1:
        print(f'\nThe top {count} words and their counts are:')
        for i in range(min(count, len(wordList))):
            print(
                f'\n"{wordList[i][0]}" which appeared {str(wordList[i][1])} time(s).'
            )
    else:
        print(f'\nThe top {count} pairs and their counts are:')
        for i in range(min(count, len(wordList))):
            print(
                f'\n"{wordList[i][0]}" which appeared {str(wordList[i][1])} time(s).'
            )


def clearScrn():
    systemOS = platform.system()
    if systemOS == "Windows":
        print(chr(12))
    elif systemOS == "Darwin" or "Linux":
        esc = chr(27)
        print(esc + '[2J' + esc + '[0;0H')
    else:
        return


main()
