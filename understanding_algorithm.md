# TITLE : TRAVEL BUDGET PLANNER AND EXPENSE ANALYZER 
    ## Problem Statement
Planning a trip requires managing expenses carefully to ensure that the total spending does not exceed the available budget. Travelers need to estimate expenses for different categories and compare these estimates with actual expenses after or during the trip.

The Travel Budget Analyzer is a Python program that accepts the destination, trip duration, and planned budget from the user. It records estimated and actual expenses for Travel, Food, Hotel, and Others. It calculates the total estimated cost, total actual cost, remaining budget, and the difference between estimated and actual expenses.

The program also identifies the category with the highest estimated expense and displays warnings when estimated or actual expenses exceed the planned budget. It calculates the average daily spending based on the trip duration and validates user inputs to avoid invalid financial calculations. 

    ##Objectives
1. Accept the travel destination, trip duration, and planned budget.
2. Record estimated expenses for each travel category.
3. Calculate the total estimated expenses and remaining budget.
4. Record actual expenses for the same categories.
5. Compare estimated and actual expenses category-wise.
6. Calculate total actual spending and budget variance.
7. Identify the highest estimated expense category.
8. Calculate estimated and actual daily spending averages.
9. Display budget status and overspending warnings.
10. Handle invalid numeric inputs and negative expense values. 

   ## Algorithm
An algorithm is a sequence of logical steps used to solve a problem.
1. Start the program.
2. Read the destination name.
3. Read and validate the trip duration.
4. Read and validate the planned budget.
5. Create a list of expense categories: Travel, Food, Hotel, and Others.
6. Create an empty dictionary to store estimated expenses.
7. For each category:
   - Accept the estimated amount.
   - Validate that the amount is numeric and non-negative.
   - Store the amount in the estimated expenses dictionary.
8. Calculate the total estimated expenses by adding all estimated amounts.
9. Calculate the remaining estimated budget by subtracting estimated expenses from the planned budget.
10. Display the estimated expense summary and budget status.
11. Identify the category with the highest estimated expense and calculate its percentage of the total estimated expenses.
12. Create an empty dictionary to store actual expenses.
13. For each category:
- Accept the actual expense.
- Validate the input.
- Store the amount in the actual expenses dictionary.
14. Calculate the total actual expenses.
15. Calculate the difference between actual and estimated expenses.
16. Calculate the final budget balance by subtracting actual expenses from the planned budget.
17. Compare estimated and actual expenses for each category.
18. Calculate the estimated and actual daily spending averages.
19. Display the formatted financial summary.
20. If the final budget balance is negative, display an overspending warning.
21. If the final budget balance is zero, display that the budget is exactly exhausted.
22. Otherwise, display that spending is within budget.
23. Stop the program.