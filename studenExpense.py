studentTripExpenses = {}

def dictCreate(studentAmount):
    for i in range(0, studentAmount):
        studentName = input("What is the name of the student? ")
        expenseList = []
        print("Enter 'done' to move to the next student.")
        while True:
            expense = input("What is the cost of this expense? ")
            if expense.lower() == 'done':
                break
            elif (float(expense) >= 0) or (float(expense) < 0):
                expenseList.append(float(expense))
            elif not expense.isdigit():
                print("Please enter a number or enter 'done' to move on.")
        studentTripExpenses[studentName] = expenseList
    return studentTripExpenses

def studentCost(dct):
    for i in dct:
        #Variable for individual costs of student
        personalCost = 0
        #Determines the total cost for each student
        for x in dct[i]:
            personalCost = personalCost + x
        #Sets each students value to their total cost to two decimal places
        dct[i] = float("%.2f" % personalCost)
    return dct

def amountsDue(expenseLst, studentAvgPrice):
        #Runs through the dictionary of students and individual total trip costs
        for key in expenseLst:
            maxPerson = max(expenseLst, key=expenseLst.get)
            costDifference = 0
            #Determines who owes who how much money
            if max(expenseLst.values()) > expenseLst[key]:
                costDifference = studentAvgPrice-expenseLst[key]
                if (costDifference < 0):
                    costDifference = costDifference * -1
                print("%s owes %s $%.2f" % (key, maxPerson, costDifference))

def main():
    numOfStudents = int(input("How many students are going on the trip? "))
    studentCostDict = dictCreate(numOfStudents)
    studentTripExpenses = studentCost(studentCostDict)

    totalCost = 0

    #Gets the total cost for all students
    for key in (studentTripExpenses):
        totalCost = totalCost + studentTripExpenses[key]

    #Changes the total cost to 2 decimal places
    totalCost = float("%.2f" % totalCost)

    #Determines the average amount spent per student
    avgCost = float("%.2f" % (totalCost/len(studentTripExpenses)))

    amountsDue(studentTripExpenses, avgCost)

main()