# ******************************************************************************
# Author:           Devan Fischer
# Lab:              Assignment 04
# Date:             2021-08-06
# Description:      This program lets the user enter student names and GPAs
#                   then prints out the top student and the class average
# Input:            studentName = string, studentGPA = float
# Output:           The top students name and GPA. The class average
# Sources:          Assignment 04 Specs, w3schools, python docs
# ******************************************************************************

"""
SAMPLE RUN:
Enter a list of student names and GPAs when prompted and the program will
display the student with the highest GPA and the class average GPA.

Enter student name: Devan

Enter student's GPA: 4.0

Add another? (y/n): t
Not a valid option. Try again.

Add another? (y/n): 3
Not a valid option. Try again.

Add another? (y/n): Y

Enter student name: 5
Not a valid name. Try again

Enter student name: Mike

Enter student's GPA: 4.8
Not a valid GPA

Enter student's GPA: -1
Not a valid GPA

Enter student's GPA: cat
Not a GPA. Try again.

Enter student's GPA: 3.5

Add another? (y/n): n

Devan has the highest GPA: 4.0
The average GPA is: 3.75

Goodbye!
"""
import math

def main():
    studentNames = []
    studentGPAs = []
    goAgain = True

    welcomeMsg()

    while goAgain:
        studentNames.append(getStudentName())
        studentGPAs.append(getStudentGPA())
        goAgain = askIfDone()

    # calling getValuesAtIndex(studentList, gpaList, index) function with the 
    # indexHighestGPA() function as the index argument to get the index of the 
    # highest GPA then assign the output to topStudentName and topStudentGPA
    topStudentName, topStudentGPA = getValuesAtIndex(
        studentNames, studentGPAs, indexHighestGPA(studentGPAs)
        )
    print(f'\n{topStudentName} has the highest GPA: {topStudentGPA}')

    classAverage = calcClassAvg(studentGPAs)
    print(f'The average GPA is: {truncateFloat(classAverage, 1)}')
    print('\nGoodbye!')


def welcomeMsg():
    print(
'Enter a list of student names and GPAs when prompted and the program will\n\
display the student with the highest GPA and the class average GPA.'
)


def getStudentName():
    '''The getStudentName() function prompts the user to enter a valid student
    name and returns a validated name.'''
    while True:
        name = input("\nEnter student's name: ")
        if name == "":
            print("Not a valid name... Try again.")
        else:
            try:
                name = float(name)
                print('Not a valid name. Try again')
            except:
                return name


def getStudentGPA():
    ''' The getStudentGPA() function prompts the user to enter a valid GPA
    (0.0 - 4.0) and returns a validated GPA'''
    while True:
        try:
            gpa = float(input("\nEnter student's GPA: "))
            if gpa >= 0.0 and gpa <= 4.0:
                return truncateFloat(gpa, 1)
            else:
                print("Not a valid GPA. Try again.")
        except:
            print("Not a GPA.")


def askIfDone():
    '''The askIfDone() function prompts the user to enter "y" or "n" to continue.
    Returns True if "y" and False if "n".'''
    while True:
        goAgain = input("\nAdd another? (y/n): ").lower()
        if goAgain not in ["y", "n"]:
            print("Not a valid option. Try again.")
        elif goAgain == "y":
            return True
        elif goAgain == "n":
            return False


def calcClassAvg(gpaList):
    '''The calcClassAvg(gpaList) function accepts a list of floats and 
    returns the average'''
    total = 0.0
    for gpa in gpaList:
        total += gpa
    return total / len(gpaList)


def indexHighestGPA(gpaList):
    '''The indexHighestGPA(gpaList) function accepts a list of floats and 
    returns the index of the largest float'''
    maxGPA = 0.0
    indexOfMax = None
    for i in range(len(gpaList)):
        if gpaList[i] > maxGPA:
            maxGPA = gpaList[i]
            indexOfMax = i
    return indexOfMax


def getValuesAtIndex(studentList, gpaList, index):
    '''The getValuesAtIndex(studentList, gpaList, index) function accepts two 
    parallel lists and an index integer then returns corresponsing value of 
    each list at the index argument'''
    return studentList[index], gpaList[index]


def truncateFloat(f, n):
    '''The truncateFloat(f,n) shortens a float to n decimal places without rounding'''
    return math.floor(f * 10 ** n) / 10 ** n


main()
