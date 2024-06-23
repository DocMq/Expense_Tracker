import json
from datetime import datetime

# Define the categories
categories = ["food", "transportation", "entertainment", "other"]

def get_expense():
    """
    Prompt the user to enter the expense details and return them as a dictionary.
    Returns:
        dict: A dictionary with keys 'amount', 'description', 'category', and 'date'.
    """
    while True:
        try:
            amount = float(input("Enter the amount spent (INR): "))
            if amount < 0:
                raise ValueError("Amount must be non-negative")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")
    
    description = input("Enter a brief description: ")
    
    while True:
        category = input(f"Enter the category ({', '.join(categories)}): ")
        if category in categories:
            break
        print("Invalid category")
    
    return {"amount": amount, "description": description, "category": category, "date": datetime.now().strftime("%Y-%m-%d")}

def save_expenses(expenses, filename="expenses.json"):
    """
    Save the expenses to a JSON file.
    Args:
        expenses (list): A list of expense dictionaries.
        filename (str): The name of the file to save the expenses to.
    """
    with open(filename, 'w') as file:
        json.dump(expenses, file)

def load_expenses(filename="expenses.json"):
    """
    Load the expenses from a JSON file.
    Args:
        filename (str): The name of the file to load the expenses from.
    Returns:
        list: A list of expense dictionaries.
    """
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error reading the file. Starting with an empty expense list.")
        return []

def get_monthly_summary(expenses):
    """
    Calculate the monthly summary of expenses.
    Args:
        expenses (list): A list of expense dictionaries.
    Returns:
        dict: A dictionary with the total expenses for each month.
    """
    summary = {}
    for expense in expenses:
        month = expense["date"][:7]  # Extract the YYYY-MM part of the date
        if month not in summary:
            summary[month] = 0
        summary[month] += expense["amount"]
    return summary

def get_category_summary(expenses):
    """
    Calculate the category-wise summary of expenses.
    Args:
        expenses (list): A list of expense dictionaries.
    Returns:
        dict: A dictionary with the total expenses for each category.
    """
    summary = {category: 0 for category in categories}
    for expense in expenses:
        summary[expense["category"]] += expense["amount"]
    return summary

def main():
    """
    The main function to drive the Expense Tracker application.
    """
    expenses = load_expenses()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            expense = get_expense()
            expenses.append(expense)
            save_expenses(expenses)
        elif choice == '2':
            print("\nMonthly Summary:")
            for month, total in get_monthly_summary(expenses).items():
                print(f"{month}: ₹{total:.2f}")
            print("\nCategory Summary:")
            for category, total in get_category_summary(expenses).items():
                print(f"{category}: ₹{total:.2f}")
        elif choice == '3':
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
