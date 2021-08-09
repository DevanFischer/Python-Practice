from string import punctuation


# Formatting class with bold, color, and end constants
# Added this afterwards for better readability
class Formatting:
    BOLD = '\033[1m'
    RED = '\033[91m'
    END = '\033[0m'


def main():
    print(
        'Hello, this program will tell you the top ten \
words used in a body of text.'
    )
    userInput = ''
    userInput = input('Enter some text: ')
    printTopTen(countWords(userInput))


def listWords(text: str) -> list:
    output = ''
    text = text.lower()
    for char in text:
        if char not in punctuation:
            output += char
    # Convert output from a string to a list containing each word
    output = output.split()
    return output


# Count the occurrence of each word in a list
def countWords(wordsList: list) -> dict:
    wordsList = listWords(wordsList)
    wordCounts = {}
    for word in wordsList:
        if word not in wordCounts:
            wordCounts[word] = 1
        else:
            wordCounts[word] += 1
    return wordCounts


# Prints out the top n words in the dictionary
def printTopTen(dict: dict, n: int) -> None:
    # Set dictionary to a list of touples
    wordList = list(dict.items())
    # Sort the list in descending order based on value
    wordList.sort(key=lambda tup: tup[1], reverse=True)
    print('\nThe top then words and their counts are:')
    for i in range(min(n, len(wordList))):
        print(
            f'\nThe word \
{Formatting.BOLD + Formatting.RED + wordList[i][0] + Formatting.END} appeared \
{Formatting.BOLD + Formatting.RED + str(wordList[i][1]) + Formatting.END} \
time(s).'
        )


main()
