
# Travel Budget Planner and Expense Analyzer 

## Project Overview
The Travel Budget Planner is a Python program that helps users
plan travel expenses and compare estimated costs with actual
spending. It calculates totals, remaining budget, category-wise
variances, and budget status.

## Features
- Accepts destination, trip duration, and planned budget.
- Records estimated expenses for Travel, Food, Hotel, and Others.
- Records actual expenses for each category.
- Calculates estimated and actual totals.
- Identifies the largest estimated expense category.
- Calculates the remaining budget and daily spending averages.
- Compares estimated expenses with actual expenses.
- Displays warnings when spending exceeds the budget.
- Validates numeric inputs and rejects negative amounts.

## Technologies Used
- Python 3
- Dictionaries and lists
- Loops and conditional statements
- Exception handling

## Requirements
- Python 3 installed on your computer.
- A Python editor or terminal.

No external packages are required.

## How to Run
1. Download or clone this repository.
2. Open the project folder in a terminal.
3. Run the following command:

   python main.py

4. Enter the destination, trip duration, and planned budget.
5. Enter estimated expenses for each category.
6. Enter actual expenses for each category.
7. Review the financial summary and budget warnings.

## Calculation Logic
- Estimated Total = Sum of all estimated expenses.
- Actual Total = Sum of all actual expenses.
- Variance = Actual Total - Estimated Total.
- Remaining Budget = Planned Budget - Actual Total.
- Daily Average = Total Expenses / Trip Duration.
- Largest Category Percentage = Largest Category Amount /Total Expenses * 100.

## Input Validation
- Destination cannot be empty.
- Trip duration must be a positive whole number.
- Planned budget must be greater than zero.
- Expense amounts must be non-negative numeric values.
- Invalid numeric input is rejected.

## Testing
Test the program with:
1. Normal expense values.
2. Actual expenses equal to the planned budget.
3. Actual expenses exceeding the budget.
4. Invalid text entered as an amount.
5. Negative expense amounts.
6. Zero expense amounts.

## Project Structure
- main.py: Main Python program.
- README.md: Project documentation.
- test_cases.md: Test scenarios and expected results.
- sample_output.txt: Example program execution.

## Author
UDAY KISHORE LINGAMPALLY 