# Matthew Homan - CMIS 102/6984 - Nov 4 2022 - Final Project

#Define ServiceSelection function which prompts user to select the service or services they want 
def ServiceSelection():

    #Display welcome message and prompt user for input
    print("\nWelcome to Ace Cleaning and Landscaping Company.\n")
    print("Would you like a quote for our cleaning service, landscaping service, or both?\n")
    print("1. Cleaning Service\n2. Landscaping Service\n3. Cleaning and Landscaping Services\n")
    customerSelection = float(input())

    #while loop to check if user selection was valid - if not, repeat - valid input is 1, 2, or 3
    while (not(customerSelection == 1 or customerSelection == 2 or customerSelection == 3)):
        print("\n *** Invalid selection. Please choose from 1, 2, or 3.")
        print("Would you like a quote for our cleaning service, landscaping service, or both?\n")
        print("1. Cleaning Service\n2. Landscaping Service\n3. Cleaning and Landscaping Services\n")
        customerSelection = float(input())
        if (customerSelection % 1 != 0):
            customerSelection = 0

    #Return customerSelection to main
    return customerSelection
    
#Define CalculateCleaningCost function
def CalculateCleaningCost():

    #Initialize variables - cost and sizes as follows
    #                                   small           medium          large
    #                                   1-2 rooms       3-5 rooms       6+ rooms
    #Floor/with                         $50/rm          $40/rm          $30/rm
    #Floor/windows/dusting              $60/rm          $50/rm          $40/rm
    #Floor/windows/dusting/ceiling      $70/rm          $60/rm          $50/rm
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
    numRooms = 0

    #Prompt the user for number of rooms in the house and get the user response
    print("\nHow many rooms do you need cleaning in your house: \n")
    numRooms = float(input())

    #Verify that user input is valid
    if ((numRooms % 1 != 0) or (numRooms <= 0)):
        while ((numRooms <= 0) or (numRooms % 1 != 0)):
            print("\nHow many rooms do you need cleaning in your house: \n")
            numRooms = float(input())
            if (numRooms % 1 != 0):
                numRooms = 0
    
    #Prompt the user for the type of cleaning they want (Floors and Windows / Floor, Windows, Dusting
    #/ Floors, Windows, Dusting, Ceiling Cleaning) and get the user response
    print("\nPlease select the type of cleaning you would like:\n1. $25 per room - Floors and Windows\n2. $37 per room - Floors, Windows, and Dusting\n3. $48 per room - Floors, Windows, Dusting, and Ceilings\n")
    customerOption = float(input())

    #Verify that user input is valid
    while (not(customerOption == 1 or customerOption == 2 or customerOption == 3)):
        print("\n *** Invalid selection. Please choose from 1, 2, or 3.")
        print("\nPlease select the type of cleaning you would like:\n1. $25 per room - Floors and Windows\n2. $37 per room - Floors, Windows, and Dusting\n3. $48 per room - Floors, Windows, Dusting, and Ceilings\n")
        customerOption = float(input())
        if (customerOption % 1 != 0):
            customerOption = 0

    
    #Calculate selections with number of rooms
    if (customerOption == 1 and numRooms <= smNumRoomsMax):
        price = option_1_Small
        totalCost = numRooms * price
        roundedTotal = round(totalCost,2)
        
    elif (customerOption == 2 and numRooms <= smNumRoomsMax):
        price = option_2_Small
        totalCost = numRooms * price
        roundedTotal = round(totalCost,2)
        
    elif (customerOption == 3 and numRooms <= smNumRoomsMax):
        price = option_3_Small
        totalCost = numRooms * price
        roundedTotal = round(totalCost,2)

    elif (customerOption == 1 and (smNumRoomsMax <= numRooms <= medNumRoomsMax)):
        price = option_1_Medium
        totalCost = numRooms * price
        roundedTotal = round(totalCost,2)
        
    elif (customerOption == 2 and (smNumRoomsMax <= numRooms <= medNumRoomsMax)):
        price = option_2_Medium
        totalCost = numRooms * price
        roundedTotal = round(totalCost,2)
        
    elif (customerOption == 3 and (smNumRoomsMax <= numRooms <= medNumRoomsMax)):
        price = option_3_Medium
        totalCost = numRooms * price
        roundedTotal = round(totalCost,2)

    elif (customerOption == 1 and (numRooms > medNumRoomsMax)):
        price = option_1_Large
        totalCost = numRooms * price
        roundedTotal = round(totalCost,2)
        
    elif (customerOption == 2 and (numRooms > medNumRoomsMax)):
        price = option_2_Large
        totalCost = numRooms * price
        roundedTotal = round(totalCost,2)
        
    elif (customerOption == 3 and (numRooms > medNumRoomsMax)):
        price = option_3_Large
        totalCost = numRooms * price
        roundedTotal = round(totalCost,2)

    #Print output - the cost of the house cleaning based on the number of rooms and the type of cleaning
    if (numRooms == 1):
        print("\nThe Ace Cleaning and Landscaping Company will be happy to clean your 1 room for $",roundedTotal,".")
    else:
        print("\nThe Ace Cleaning and Landscaping Company will be happy to clean your ",numRooms," rooms for $",roundedTotal,".")

    #Return roundedTotal to Main
    return(roundedTotal)

#Define CalculateLandscapingCost
def CalculateLandscapingCost():

    #Initialize variables - cost and sizes as follows
    #           small            medium                  large
    #Mowing     x<500:.15/sqft   500<=x<1000:.14/sqft    1000<=x:.13/sqft
    #Edging     x<30:2/lnft      30<=x<60:1.5/lnft       60<x:1/lnft
    #Pruning    x<5:15/shrub     5<=x<15:10/shrub        15<=x:7/shrub
    mowing_1_Small = .15
    mowing_2_Medium = .14
    mowing_3_Large = .13
    edging_1_Small = 2
    edging_2_Medium = 1.5
    edging_3_Large = 1
    pruning_1_Small = 15
    pruning_2_Medium = 10
    pruning_3_Large = 7
    
    mowing_Small_Max = 500
    mowing_Large_Min = 1000
    edging_Small_Max = 30
    edging_Large_Min = 60
    pruning_Small_Max = 5
    pruning_Large_Min = 15

    price = 0

    #Prompt user for type of landscaping needed
    print("\nPlease select the type of landscaping you would like:\n1. Mowing\n2. Edging\n3. Shrub Pruning\n4. Mowing and Edging\n5. Mowing and Shrub Pruning\n6. Edging and Shrub Pruning\n7. Mowing, Edging, and Shrub Pruning\n")
    customerOption = float(input())

    #while loop to check if input is valid - only valid input is 1,2,3,4,5,6, or 7
    while (not(customerOption == 1 or customerOption == 2 or customerOption == 3 or customerOption == 4 or customerOption == 5 or customerOption == 6 or customerOption == 7)):
        print("\n *** Invalid selection. Please choose from 1, 2, 3, 4, 5, 6, or 7.")
        print("\nPlease select the type of landscaping you would like:\n1. Mowing\n2. Edging\n3. Shrub Pruning\n4. Mowing and Edging\n5. Mowing and Shrub Pruning\n6. Edging and Shrub Pruning\n7. Mowing, Edging, and Shrub Pruning\n")
        customerOption = float(input())
        if (customerOption % 1 != 0):
            customerOption = 0

    #if statements to process calculation based on user selection - user is prompted to input sqft, lnft, or num of shrubs, or some mix of
    #the previous options to calculate the cost of landscaping needed
    #nested if statements will calculate based on input, which compares input to size variables and calculates accordingly
    #price summed at the end of each loop, adding multiple costs if necessary
    if (customerOption == 1):
        print("How large is your yard?  Please enter the square footage: ")
        sqftYard = float(input())
        if (sqftYard < mowing_Small_Max):
            price = round((sqftYard * mowing_1_Small),2)
        elif (sqftYard >= mowing_Small_Max and sqftYard < mowing_Large_Min):
            price = round((sqftYard * mowing_2_Medium),2)
        else:
            price = round((sqftYard * mowing_3_Large),2)

    elif (customerOption == 2):
        print("How long are your yard's edges?  Please enter the linear footage: ")
        lnftEdge = float(input())
        if (lnftEdge < edging_Small_Max):
            price = round((lnftEdge * edging_1_Small),2)
        elif (lnftEdge >= edging_Small_Max and lnftEdge < edging_Large_Min):
            price = round((lnftEdge * edging_2_Medium),2)
        else:
            price = round((lnftEdge * edging_3_Large),2)

    elif (customerOption == 3):
        print("How many shrubs do you need pruning?  Please enter the number of shrubs: ")
        numShrub = float(input())
        if (numShrub < pruning_Small_Max):
            price = round((numShrub * pruning_1_Small),2)
        elif (numShrub >= pruning_Small_Max and numShrub < pruning_Large_Min):
            price = round((numShrub * pruning_2_Medium),2)
        else:
            price = round((numShrub * pruning_3_Large),2)

    elif (customerOption == 4):
        print("How large is your yard?  Please enter the square footage: ")
        sqftYard = float(input())
        if (sqftYard < mowing_Small_Max):
            priceMow = round((sqftYard * mowing_1_Small),2)
        elif (sqftYard >= mowing_Small_Max and sqftYard < mowing_Large_Min):
            priceMow = round((sqftYard * mowing_2_Medium),2)
        else:
            priceMow = round((sqftYard * mowing_3_Large),2)

        print("How long are your yard's edges?  Please enter the linear footage: ")
        lnftEdge = float(input())
        if (lnftEdge < edging_Small_Max):
            priceEdge = round((lnftEdge * edging_1_Small),2)
        elif (lnftEdge >= edging_Small_Max and lnftEdge < edging_Large_Min):
            priceEdge = round((lnftEdge * edging_2_Medium),2)
        else:
            priceEdge = round((lnftEdge * edging_3_Large),2)

        price = priceMow + priceEdge

    elif (customerOption == 5):
        print("How large is your yard?  Please enter the square footage: ")
        sqftYard = float(input())
        if (sqftYard < mowing_Small_Max):
            priceMow = round((sqftYard * mowing_1_Small),2)
        elif (sqftYard >= mowing_Small_Max and sqftYard < mowing_Large_Min):
            priceMow = round((sqftYard * mowing_2_Medium),2)
        else:
            priceMow = round((sqftYard * mowing_3_Large),2)

        print("How many shrubs do you need pruning?  Please enter the number of shrubs: ")
        numShrub = float(input())
        if (numShrub < pruning_Small_Max):
            priceShrub = round((numShrub * pruning_1_Small),2)
        elif (numShrub >= pruning_Small_Max and numShrub < pruning_Large_Min):
            priceShrub = round((numShrub * pruning_2_Medium),2)
        else:
            priceShrub = round((numShrub * pruning_3_Large),2)

        price = priceMow + priceShrub

    elif (customerOption == 6):    
        print("How long are your yard's edges?  Please enter the linear footage: ")
        lnftEdge = float(input())
        if (lnftEdge < edging_Small_Max):
            priceEdge = round((lnftEdge * edging_1_Small),2)
        elif (lnftEdge >= edging_Small_Max and lnftEdge < edging_Large_Min):
            priceEdge = round((lnftEdge * edging_2_Medium),2)
        else:
            priceEdge = round((lnftEdge * edging_3_Large),2)

        print("How many shrubs do you need pruning?  Please enter the number of shrubs: ")
        numShrub = float(input())
        if (numShrub < pruning_Small_Max):
            priceShrub = round((numShrub * pruning_1_Small),2)
        elif (numShrub >= pruning_Small_Max and numShrub < pruning_Large_Min):
            priceShrub = round((numShrub * pruning_2_Medium),2)
        else:
            priceShrub = round((numShrub * pruning_3_Large),2)

        price = priceEdge + priceShrub

    elif (customerOption == 7): 
        print("How large is your yard?  Please enter the square footage: ")
        sqftYard = float(input())
        if (sqftYard < mowing_Small_Max):
            priceMow = round((sqftYard * mowing_1_Small),2)
        elif (sqftYard >= mowing_Small_Max and sqftYard < mowing_Large_Min):
            priceMow = round((sqftYard * mowing_2_Medium),2)
        else:
            priceMow = round((sqftYard * mowing_3_Large),2)

        print("How long are your yard's edges?  Please enter the linear footage: ")
        lnftEdge = float(input())
        if (lnftEdge < edging_Small_Max):
            priceEdge = round((lnftEdge * edging_1_Small),2)
        elif (lnftEdge >= edging_Small_Max and lnftEdge < edging_Large_Min):
            priceEdge = round((lnftEdge * edging_2_Medium),2)
        else:
            priceEdge = round((lnftEdge * edging_3_Large),2)

        print("How many shrubs do you need pruning?  Please enter the number of shrubs: ")
        numShrub = float(input())
        if (numShrub < pruning_Small_Max):
            priceShrub = round((numShrub * pruning_1_Small),2)
        elif (numShrub >= pruning_Small_Max and numShrub < pruning_Large_Min):
            priceShrub = round((numShrub * pruning_2_Medium),2)
        else:
            priceShrub = round((numShrub * pruning_3_Large),2)

        price = priceMow + priceEdge + priceShrub

    #Print total cost for customer to see
    print("\nAce Cleaning and Landscaping Company will be happy to landscape your property for $",price,".")

    #Return price to main
    return(price)

#Define Discount to check if user is eligible for 15% discount - receive grandTotalCost variable from main
def Discount(grandTotalCost):

    #Prompt user to enter age to see if eligible for discount
    print("\nPlease enter your age to see if you are eligible for a discount: ")
    userAge = float(input())

    #Check if input is valid with while loop
    while (userAge <= 0):
        print("\n *** Invalid age")
        print("\nPlease enter your age to see if you are eligible for a discount: ")
        userAge = float(input())

    #if statement to check if user is 65 or older - if TRUE, reduce price by 15%
    #if FALSE, print apology and price remains unchanged
    if (userAge >= 65):
        print("\nA 15% discount will be automatically subtracted from your total.")
        grandTotalCost = round((grandTotalCost - (grandTotalCost * .15)),2)
    else:
        print("\nSorry, you are not eligible for a discount.")

    #Return grandTotalCost
    return grandTotalCost

#Define Main
def main():

    #Initialize variables cleaningTotal and landscapingTotal for costs
    cleaningTotal = 0
    landscapingTotal = 0

    #Call CustomerSelection function and set equal to customerSelection variable
    customerSelection = ServiceSelection()

    #if statements to manage customerSelection - if 1, call CalculateCleaningCost - if 2, call CalculateLandscapingCost - if 3, call first CalculateCleaningCost and then CalculateLandscapingCost   
    if (customerSelection == 1):
        cleaningTotal = CalculateCleaningCost()

    elif (customerSelection == 2):
        landscapingTotal = CalculateLandscapingCost()

    elif (customerSelection == 3):
        cleaningTotal = CalculateCleaningCost()
        landscapingTotal = CalculateLandscapingCost()
    
    #Sum grandTotalCost of cleaning and landscaping totals
    grandTotalCost = cleaningTotal + landscapingTotal

    #Call Discount function and pass grandTotalCost
    grandTotalCost = Discount(grandTotalCost)

    #Print final grand total cost for customer
    print("\nThe grand total for our services comes to $",grandTotalCost,"and we thank you for choosing The Ace Cleaning and Landscaping Company.")

    
#Executes the main
main() 

