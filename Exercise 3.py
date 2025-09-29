Python 3.13.6 (v3.13.6:4e665351082, Aug  6 2025, 11:22:35) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> from functools import reduce
... 
... def main():
...     expenses = []
... 
...     print("Enter your monthly expenses. Type 'done' when finished.\n")
... 
...     while True:
...         expense_type = input("Enter expense type (or 'done' to finish): ")
...         if expense_type.lower() == "done":
...             break
... 
...         try:
...             amount = float(input(f"Enter amount for {expense_type}: "))
...             expenses.append((expense_type, amount))
...         except ValueError:
...             print("Invalid amount. Please enter a number.")
... 
...     if not expenses:
...         print("\nNo expenses entered.")
...         return
... 
...     # Calculate total expense
...     total = reduce(lambda acc, x: acc + x[1], expenses, 0)
... 
...     # Find highest expense
...     highest = reduce(lambda a, b: a if a[1] > b[1] else b, expenses)
... 
...     # Find lowest expense
...     lowest = reduce(lambda a, b: a if a[1] < b[1] else b, expenses)
... 
...     print("\nExpense Analysis:")
...     print(f"Total Expenses: ${total:.2f}")
...     print(f"Highest Expense: {highest[0]} - ${highest[1]:.2f}")
...     print(f"Lowest Expense: {lowest[0]} - ${lowest[1]:.2f}")
... 
... if __name__ == "__main__":
