# Expense Tracker

A Python-based application to manage and analyze daily expenses.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data Storage](#data-storage)
- [Error Handling](#error-handling)
- [Examples](#examples)
- [License](#license)

## Introduction

The Expense Tracker is a command-line application that helps users manage their daily expenses efficiently. Users can input their expenses, categorize them, and view detailed summaries of their spending patterns. The application stores expense data in a JSON file for easy retrieval and analysis.

## Features

- **User Input**: Allows users to input their daily expenses, including the amount spent and a brief description.
- **Expense Categories**: Users can categorize their expenses (e.g., food, transportation, entertainment, other).
- **Data Storage**: Expense data is stored and retrieved using JSON files.
- **Data Analysis**: Provides monthly summaries and category-wise expenditure.
- **User Interface**: Simple command-line interface for user interaction.
- **Error Handling**: Includes error handling mechanisms for user input and file operations.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/Expense-Tracker.git
   cd Expense-Tracker
2. **Ensure you have Python 3.x installed**:
    You can download Python from python.org.

## Usage

1. **Run the Application**:
    Expense_Tracker.py
2. **Add Expenses**:
    Enter the amount spent (in INR), a brief description, and select a category from the predefined list (food, transportation, entertainment, other).
3. **View Summaries**:
    Choose the option to view monthly summaries and category-wise expenditure.
4. **Exit**:
    Select the exit option to close the application.

## Data Storage

The application uses a JSON file (expenses.json) to store expense data. Each expense entry includes the following fields:

- **amount**: The amount spent (in INR).
- **description**: A brief description of the expense.
- **category**: The category of the expense (food, transportation, entertainment, other).
- **date**: The date when the expense was recorded (in YYYY-MM-DD format).

## Error Handling
The application includes error handling mechanisms to ensure smooth user interaction:

- **Invalid Input**: Prompts the user to re-enter data in case of invalid input.
- **File Operations**: Handles file not found and JSON decode errors during data loading.

## Examples

Adding an Expense

Expense Tracker Menu:
1. Add Expense
2. View Summary
3. Exit
Choose an option: 1
Enter the amount spent (INR): 250
Enter a brief description: Lunch at a restaurant
Enter the category (food, transportation, entertainment, other): food

Viewing Summeries

Expense Tracker Menu:
1. Add Expense
2. View Summary
3. Exit
Choose an option: 2

Monthly Summary:
2024-06: ₹250.00

Category Summary:
food: ₹250.00
transportation: ₹0.00
entertainment: ₹0.00
other: ₹0.00

## License 

This project is licensed under the MIT License. See the LICENSE file for details.