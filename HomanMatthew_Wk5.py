#Matthew Homan - CMIS 102/6984 - Oct 22 2022 - Week 5 Assignment: Student Weighted Averages

#Define the function called StudentAverage receiving the variable 'student'
def StudentAverage(student):

    #Prints message showing who the following grades are for
    print("\nGrades for ",student,":")

    #User inputs grades
    discussionGrade = int(input("Please enter the Discussion Grade: "))
    quizGrade = int(input("Please enter the Quiz Grade: "))
    projGrade = int(input("Please enter the Project Grade: "))

    #Calculation for weighted average
    gradeAver = (discussionGrade * .1) + (quizGrade * .4) + (projGrade * .5)

    #Return the average to the main function
    return (gradeAver)

#Defines the function main
def main():

    #Initialize variables 
    students = ["Alina" , "Tim" , "Natasha", "Victor"]
    gradeAver = 0
    highestGrade = 0
    topStudent = None
    
    #Print welcome message
    print("\nThis program will compute the weighted average grade for four students.")

    #'for' loop start iterating 
    for student in students:

        #Set new variable to the rounded value of the student average
        currentAver = round(StudentAverage(student),2)

        #Set the current student whose grades are being calculated to currentStudent
        currentStudent = student
        print("\nThe grade for ",student," is: ",currentAver)

        #'if' loop checking to see if the current student average is greater than the highest grade
        if (currentAver > highestGrade):

            #Set the current student average to the highestGrade variable and currentStudent to topStudent
            highestGrade = currentAver
            topStudent = currentStudent

    #Print the final result, the student with the highest average (or first highest average), and the highest average
    print("The top student is ",topStudent," with a grade of ",highestGrade,".")

#Executes the main
main()
