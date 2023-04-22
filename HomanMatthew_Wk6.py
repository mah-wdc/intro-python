#Matthew Homan - CMIS 102/6984 - Oct 29 2022 - Week 6 Assignment: Password Check

#Define GetUserPassword function to get String input from user
def GetUserPassword():

    #Get user password
    userPassword = str(input("\nPlease enter a password to be checked for being secure.\nIt must be:\n\t-between 8 and 15 characters\n\t-must not include spaces\n\t-must contain at least one digit\n\t-must contain at least one alphabetic character\n\n==>  "))

    #Set to lowercase
    lowerUserPassword = userPassword.lower()

    #Return String
    return lowerUserPassword

#Define CheckPasswordLength function to check if the length requirement is met or not
def CheckPasswordLength(userPassword):

    #Get String length
    passwordLength = len(userPassword)

    #Set result to False
    lengthResult = False

    #if statement to check if the length meets the requirement or not and print messages for each outcome, too short, too long, meets
    if (passwordLength < 8):
        print("\nYour password is too short.")
    elif (passwordLength > 15):
        print("\nYour password is too long.")
    elif (passwordLength >= 8 and passwordLength <= 15):
        print("\nYour password meets the length requirement.")
        lengthResult = True

    #Returns length result
    return lengthResult

#Define CheckPasswordSpaces function to check if the no space requirement is met or not
def CheckPasswordSpaces(userPassword):

    #Set result to False and initialize variables
    spaceResult = False
    charCount = 0
    digitCount = 0

    #Remove (strip) empty area around the string
    userPasswordSpaceCheck = userPassword.strip()

    #Get length of original string and new string
    length_1 = len(userPassword)
    length_2 = len(userPasswordSpaceCheck)

    #for loop to get the number of characters (alpha and numerical)
    for char in userPasswordSpaceCheck:
        if (char.isalpha() == True):
            charCount = charCount + 1
        elif (char.isdigit() == True):
            digitCount = digitCount + 1

    #if statement to check if the original string length and new string length are the same as well as the length of the alpha and numerical digits which checks for internal spaces, which also must equal the new length post strip, and print results
    if (length_1 == length_2) and ((charCount + digitCount) == length_2):
        print("\nYour password meets the no spaces requirement.")
        spaceResult = True
    else:
        print("\nYour password contains a space and fails to meet the requirement.")

    #Return result
    return spaceResult

#Define CheckPasswordDigit function to check if the digit requirement is met or not
def CheckPasswordDigit(userPassword):

    #Set result to False and initialize variable
    digitResult = False
    digitCount = 0

    #for loop to check if at least one character in the string is a number
    for char in userPassword:
        if (char.isdigit() == True):
            digitResult = True

    #if statement to check if the result is True and print result
    if digitResult == True:
        print("\nYour password contains at least one digit which meets the requirement.")
    else:
        print("\nYour password does not contain a digit and fails to meet the requirement.")
        
    #Return result
    return digitResult

#Define CheckPasswordAlphabet function to check if the alphabet character requirement is met or not
def CheckPasswordAlphabet(userPassword):

    #Set result to False and initialize variable
    alphaResult = False
    alphaCount = 0

    #for loop to check if at least one character in the string is an alphabet letter
    for alpha in userPassword:
        if (alpha.isalpha() == True):
            alphaResult = True

    #if statement to check if the result is True and print result
    if alphaResult == True:
        print("\nYour password contains at least one alphabetic character which meets the requirement.")
    else:
        print("\nYour password does not contain an alphabetic character and fails to meet the requirement.")

    #Return result
    return alphaResult

#Define Main
def main():

    #Get User Password
    userPassword = GetUserPassword()

    #Check length
    lengthResult = CheckPasswordLength(userPassword)

    #Check for spaces
    spaceResult = CheckPasswordSpaces(userPassword)

    #Check for a digit
    digitResult = CheckPasswordDigit(userPassword)

    #Check for a letter
    alphaResult = CheckPasswordAlphabet(userPassword)

    #if statement to check if all of the requirements have been met or not, and prints a result respectively
    if ((lengthResult == True) and (spaceResult == True) and (digitResult == True) and (alphaResult == True)):
        print("\nYour password meets all the requirements and has been accepted.")
    else:
        print("\nYour password fails to meet all of the requirements and has not been accepted.")

#Executes the main
main()
