Destination = input("Enter the Destination : ").strip() 

while not Destination:
    print("Destination can not be empty") 
    Destination = input("Enter the Destination : ").strip()  

#Enter trip duration 
while True:
    try:
        Trip_days = int(input("Enter the number of days for the trip: "))

        if Trip_days <= 0:
            print("Trip duration must be greater than zero.")  
        else :
            break
    except ValueError:
        print("Enter a valid number.") 

#Budget can not be zero or negative 
while True:
    try:
        Office_Budget = float(input("Enter the Planned Budget : ")) 

        if Office_Budget <= 0:
            print("Error: Budget can not be zero or negative") 
        else:
            break 
    except ValueError:
        print("Enter a valid number.") 

#Creating List of Categories 
categories = ["Travel", "Food", "Hotel", "Others"]
estimated_expenses = {} 

for category in categories:
    while True:
        try:
            amount = float(input("Enter the Estimated Expenses for  " + category + " : "))  
            if amount < 0:
                print("Expenses can not be negative")
            else:
                estimated_expenses[category] = amount
                break
        except ValueError:
            print("Enter a valid number.") 

estimated_total = sum(estimated_expenses.values())
remaining_budget = Office_Budget - estimated_total 

print("\n----Estimated Expenses Summary----") 
print("Destination : ", Destination)
print("number of days for the trip : ", Trip_days)
print("Planned Budget : $ ", Office_Budget)
print("Estimated Total : $ ", estimated_total)
print("Remaining Budget : $ ", remaining_budget)  

if estimated_total > Office_Budget:
    buffer_percentage = ((estimated_total - Office_Budget) / Office_Budget) * 100 
    print(f"Remaining Buffer: {buffer_percentage:.1f}%") 

if remaining_budget < 0:
    print("Warning : Estimated Expenses exceed the Planned Budget")
elif remaining_budget == 0:
    print("Estimated Expenses equal the Planned Budget")
else:
    print("Estimated Expenses are within the Planned Budget")


if estimated_total > 0 :
    highest_category = max(estimated_expenses, key=estimated_expenses.get) 
    highest_amount = estimated_expenses[highest_category] 
    highest_percentage = (highest_amount / estimated_total) * 100
    print(f"Highest Budget Category : {highest_category} with amount ${highest_amount:.2f} ({highest_percentage:.1f}%)")
else:
    print("No estimated expenses were entered.") 

print(f"estimated daily average: ${estimated_total / Trip_days:.2f}") 

#Actual Expenses 
actual_expenses = {} 
for category in categories:
    while True:
        try:
            amount = float(input("Enter the Actual Expenses for " + category + " : "))  
            if amount < 0:
                print("Expenses can not be negative")
            else:
                actual_expenses[category] = amount
                break 
        except ValueError:
            print("Enter a valid number.") 

#Calculating actual total and remaining budget
actual_total = sum(actual_expenses.values())
difference = actual_total - estimated_total
final_remaining_budget = Office_Budget - actual_total 

print("\n----Estimated vs Actual Expenses Comparison----") 
print(f"{'Category':<15}{'Estimated':<15}{'Actual':<15}{'Difference':<15}") 

print("-" * 60) 

for category in categories:
    estimated = estimated_expenses[category] 
    actual = actual_expenses[category]
    category_difference = actual - estimated
    print(f"{category:<15}${estimated:<14.2f}${actual:<14.2f}${category_difference:<14.2f}") 

print("-" * 60) 
print(f"{'Total':<15}${estimated_total:<14.2f}${actual_total:<14.2f}${difference:<14.2f}") 

#final acutal expenses summary 
print("\n----Actual Expenses Summary----") 
print(f"Actual Total : ${actual_total:.2f}")
print(f"Difference between Actual and Estimated Total : ${difference:.2f}")
print(f"Final Budget Balance : ${final_remaining_budget:.2f}")
print(f"actual daily average: ${actual_total / Trip_days:.2f}") 

#final budget warnings based on actual expenses
if final_remaining_budget > 0:
    print("Trip spending is within the planned budget.")
elif final_remaining_budget == 0:
    print("Trip spending is exactly equal to the planned budget.")
else:
    print("Warning: Trip spending exceeds the planned budget.")