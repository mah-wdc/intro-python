#Matthew Homan - CMIS 102/6984 - Oct 2 2022 - Week 2 Assignment: Calulating newspaper carriers weekly salary plus tips

def main():
    
    #Initialize variables: newspaperCost = 1.5 , commissionPercentage = .5
    newsPaperCost = float(1.5)
    commissionPercentage = float(.5)

    #Display welcome message
    print("Hello NewsPaper Carrier! Input your information and this program will calculate")
    print("your weekly number of newspapers delivered, salary, and total pay including tips.\n")

    #Prompt the user for number of papers on route
    numOfNewsPapers = int(input("Enter the number of newspapers you deliver on your route: "))
                 
    #Prompt the user for number of days in a week they deliver papers
    numOfDays = int(input("Enter the number of days you deliver papers in a week: "))

    #Prompt the user for amount of tips received for week
    amountOfTips = float(input("Enter the amount of weekly tips: $"))

    #Calculate the total number of newspapers delivered in a week
    totalNewsPapers = numOfNewsPapers * numOfDays

    #Calculate the weekly salary
    weeklySalary = (totalNewsPapers * newsPaperCost) * commissionPercentage
    
    #Calculate the total pay for the week

    totalPay = amountOfTips + weeklySalary
          
    #Display the total number of newspapers delivered in a week
    print("\nThe number of newspapers you deliver in a week is ",totalNewsPapers,".")

    #Display the weekly salary
    print("Your weekly salary is $",weeklySalary,".")

    #Display the tips received for the week
    print("Your weekly tip amount is $",amountOfTips,".")

    #Display the total pay for the week
    print("Your total pay for the week is $",totalPay,".")

main() #executes the main, running the program

