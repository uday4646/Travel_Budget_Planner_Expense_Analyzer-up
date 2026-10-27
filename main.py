Destination = input("Enter the Destination : ")
Office_Budget = float(input("enter the Planned Budget : ")) 
print("Planned Budget is : ", Office_Budget)  

# Budget canot be zero or negitive 
if Office_Budget <= 0 :
    print("Error : Budget can not be zero or negative") 
    exit()
else :
    print("Budget is Valid") 

# Creating List of Categories 

Categories = ["Travel", "Food", "Hotel", "Others"] 
Estimated_Expenses = {} 

for Category in Categories : 
    Amount = float(input("Enter the Estimated Expenses for " + Category + " : ")) 
    if Amount < 0 :
        print("Expenses can not be negative") 

    Estimated_Expenses[Category] = Amount   

# Calculating estamiting total and remaining budget 
estimated_total = sum(Estimated_Expenses.values()) 
remaining_budget = Office_Budget - estimated_total 

#Printing the estimated totals 
print("\n----Estimated Expenses Summary----") 
print("Destination : ", Destination)
print("Planned Budget : $ ", Office_Budget)
print("Estimated Total : $ ", estimated_total)
print("Remaining Budget : $ ", remaining_budget)

#Adding budget warnings 
if remaining_budget < 0 :
    print("Warning : Estimated Expenses exceed the Planned Budget") 
elif remaining_budget == 0 :
    print("Estimated Expenses equal the Planned Budget") 
else :
    print("Estimated Expenses are within the Planned Budget") 

#Highest budget category 
highest_category = max(Estimated_Expenses, key=Estimated_Expenses.get) 
highest_amount = Estimated_Expenses[highest_category] 
print("Highest Budget Category : ", highest_category, "with amount $", highest_amount) 

#Actual Expenses 
Actual_Expenses = {}
for Category in Categories :
    Amount = float(input("Enter the Actual Expenses for " + Category + " : ")) 
    if Amount < 0 :
        print("Expenses can not be negative") 

    Actual_Expenses[Category] = Amount 

actual_total = sum(Actual_Expenses.values()) 
difference = actual_total - estimated_total 
final_remaining_budget = Office_Budget - actual_total 

#printing the actual totals

print("\n----Estimated vs Actual Expenses Comparison----") 
for Category in Categories :
    category_difference = Actual_Expenses[Category] - Estimated_Expenses[Category] 

    print(f"{Category}:") 
    print(f"  Estimated: ${Estimated_Expenses[Category]:.2f}") 
    print(f"  Actual: ${Actual_Expenses[Category]:.2f}") 
    print(f"  Difference: ${category_difference:.2f}")  

#final Wanrings based on actual expenses 
print(f"\nActual Total : ${actual_total:.2f}") 
print(f"difference between Actual and Estimated Total : ${difference:.2f}") 
print(f"Final Budget Balance : ${final_remaining_budget:.2f}") 

if final_remaining_budget > 0 :
    print("Trip spending is within the planned budget.") 
elif final_remaining_budget == 0 :
    print("Trip spending is exactly equal to the planned budget.") 
else :
    print("Warning: Trip spending exceeds the planned budget.")  

print("\n----End of Budget Report----")