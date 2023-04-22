#Matthew Homan - CMIS 102/6984 - Nov 4 2022 - Week 7 Assignment: Road Trip

#Define NumPeople which gets the number of people who went on the trip
def NumPeople():

    #Initialize variable numPeople and get value from user
    numPeople = float(input("\nHow many people went on your trip?  "))

    #Return numPeople to main
    return(numPeople)

#Define NumDays which gets the number of days of the trip
def NumDays():

    #Initialize variable numDays and get value from user
    numDays = float(input("\nHow many days was your trip?  "))


    #Return numDats to main
    return(numDays)

#Define FoodCostCalc which gets the cost each day of food for the trip and sums it
def FoodCostCalc(numDays):

    #Initialize variables foodCostArray and count
    foodCostArray = list()
    count = 0
    print("")
    
    #while loop to get user input on cost of food for each day of trip
    while (numDays != count):
        count = count + 1
        print("Enter the amount spent on food on day",count,": ")
        dailyFoodCost = float(input())
        foodCostArray.append(dailyFoodCost)

    #Sum total cost of food and print total
    totalFoodCost = sum(foodCostArray)
    print("\nThe total amount spent on food during the trip was $",round(totalFoodCost,2),".\n")

    #Return totalFoodCost to main
    return totalFoodCost

#Define GasCostCalc which gets the cost each day of gas for the trip and sums it
def GasCostCalc(numDays):

    #Initialize variables gasCostArray and count
    gasCostArray = list()
    count = 0
    print("")

    #while loop to get user input on cost of gas for each day of trip
    while (numDays != count):
        count = count + 1
        print("Enter the amount spent on gas on day",count,": ")
        dailyGasCost = float(input())
        gasCostArray.append(dailyGasCost)

    #Sum total cost of food and print total
    totalGasCost = sum(gasCostArray)
    print("\nThe total amount spent on gas during the trip was $",round(totalGasCost,2),".\n")

    #Return totalFoodCost to main
    return totalGasCost

#Define IndividualCost to calculate what each person owes for the trip
def IndividualCost(grandTotal, numPeople):

    #Calculate and Print what each person owes
    owePerPerson = grandTotal / numPeople
    print("\nEach person owes $",round(owePerPerson,2),"for their portion of the food and gas.")

#Define main
def main():

    #Call NumPeople function
    numPeople = NumPeople()

    #Call NumDays function
    numDays = NumDays()

    #Call FoodCostCalc function
    totalFoodCost = FoodCostCalc(numDays)

    #Call GasCostCalc function
    totalGasCost = GasCostCalc(numDays)

    #Initialize variable grandTotal and sum totalFoodCost and totalGasCost
    grandTotal = totalFoodCost + totalGasCost

    #Print grandTotal
    print("\nThe total cost of the trip is $",round(grandTotal,2),".")

    #Call IndividualCost function
    IndividualCost(grandTotal, numPeople)    

main()
