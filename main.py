expenseslist = []
print("Welcome to the Expense Tracker!")
#Menu
while True:
    print("=====Menu=====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Exit")
# User Input    
    choice  = int(input("Enter Your Choice:"))
# Add Expenses
    if (choice == 1):
        date = input("Enter The Date when you made the expense : ")
        category = input("Enter The Expense Category(food, Travel, Shopping,etc):")
        description = input("Enter The Description Of The Expense:")
        amount = float(input("enter The Amount spent: "))
        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        } 
        expenseslist.append(expense)
        print("Expense Added Successfully!")
#View Expenses
    elif (choice == 2):
        if (len (expenseslist)==0):
            print("No Expense Yet Added: ")
        else:
            print("===Here's Your Expenses===")
            count = 1
            for eachexpense in expenseslist:
                print(f"Expense Number{count} -> {eachexpense["date"]},{eachexpense["category"]},{eachexpense["description"]},{eachexpense["amount"]}")
                count +=1
# View Total Expense
    elif (choice == 3):
        total = 0
        for eachexpense in expenseslist:
            total = total + eachexpense["amount"]
        print("/n Total Expense =", total)    

# Exit
    elif (choice == 4):
        print("!===Thankyou For Using This System===!")
        break

    else:
        print("Invalid Choice, Try Again ")
         

 

