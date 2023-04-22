# Matthew Homan - CMIS 102/6984 - Oct 12 2022 - Week 4 Assignment: Cleaning Company with function


def CalculateCleaningCost(numRooms, customerOption):
    #Accepts two arguments to perform calculations from user input in Main
    #Initialize variables: cleaningOptionPrice_1, cleaningOptionPrice_2, cleaningOptionPrice_3, smNumRoomsMax, medNumRoomsMax
    
    option_1_Small = 50
    option_1_Medium = 40
    option_1_Large = 30
    option_2_Small = 60
    option_2_Medium = 50
    option_2_Large = 40
    option_3_Small = 70
    option_3_Medium = 60
    option_3_Large = 50
    smNumRoomsMax = 2
    medNumRoomsMax = 5
    price = 0
    
    #Calculate selections with number of rooms
    
    if (customerOption == 1 and numRooms <= smNumRoomsMax):
        price = option_1_Small
        totalCost = numRooms * price
        round(totalCost,2)
        
    elif (customerOption == 2 and numRooms <= smNumRoomsMax):
        price = option_2_Small
        totalCost = numRooms * price
        round(totalCost,2)
        
    elif (customerOption == 3 and numRooms <= smNumRoomsMax):
        price = option_3_Small
        totalCost = numRooms * price
        round(totalCost,2)

    elif (customerOption == 1 and (smNumRoomsMax <= numRooms <= medNumRoomsMax)):
        price = option_1_Medium
        totalCost = numRooms * price
        round(totalCost,2)
        
    elif (customerOption == 2 and (smNumRoomsMax <= numRooms <= medNumRoomsMax)):
        price = option_2_Medium
        totalCost = numRooms * price
        round(totalCost,2)
        
    elif (customerOption == 3 and (smNumRoomsMax <= numRooms <= medNumRoomsMax)):
        price = option_3_Medium
        totalCost = numRooms * price
        round(totalCost,2)

    elif (customerOption == 1 and (numRooms > medNumRoomsMax)):
        price = option_1_Large
        totalCost = numRooms * price
        round(totalCost,2)
        
    elif (customerOption == 2 and (numRooms > medNumRoomsMax)):
        price = option_2_Large
        totalCost = numRooms * price
        round(totalCost,2)
        
    elif (customerOption == 3 and (numRooms > medNumRoomsMax)):
        price = option_3_Large
        totalCost = numRooms * price
        round(totalCost,2)

    #Return totalCost to Main
    return(totalCost)

def main():
    
    #Display welcome message
    print("\nWelcome to Ace Cleaning Company.")
    
    #Prompt the user for number of rooms in the house and get the user response
    print("\nPlease enter the number of rooms you need cleaning in your house: \n")
    numRooms = int(input())

    #Verify that user input is valid
    if (numRooms <= 0):
        print("\n *** Invalid number. Please enter a positive whole number.")
        print("Please enter the number of rooms you need cleaning in your house: ")
        numRooms = int(input())
    
    #Prompt the user for the type of cleaning they want (Floors and Windows / Floor, Windows, Dusting / Floors, Windows, Dusting, Ceiling Cleaning) and get the user response
    print("\nPlease select the type of cleaning you would like:\n1. $25 per room - Floors and Windows\n2. $37 per room - Floors, Windows, and Dusting\n3. $48 per room - Floors, Windows, Dusting, and Ceilings\n")
    customerOption = int(input())

    #Verify that user input is valid and set the price according to user selection
    if (not(customerOption == 1 or customerOption == 2 or customerOption == 3)):
        print("\n *** Invalid selection. Please choose from 1, 2, or 3.")
        print("\nPlease select the type of cleaning you would like:\n1. $25 per room - Floors and Windows\n2. $37 per room - Floors, Windows, and Dusting\n3. $48 per room - Floors, Windows, Dusting, and Ceilings")
        customerOption = int(input())

    #Call CalculateCleaningCost function sending 2 arguments to the function to be calculated
    totalCost = CalculateCleaningCost(numRooms, customerOption)

    #Print output - the cost of the house cleaning based on the number of rooms and the type of cleaning
    if (numRooms == 1):
        print("\nAce Cleaning Company will be happy to clean your 1 room for $",totalCost,".")

    else:
        print("\nAce Cleaning Company will be happy to clean your ",numRooms," rooms for $",totalCost,".")
    

main() #executes the main, running the program


