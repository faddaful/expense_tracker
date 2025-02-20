# Expense Tracker System

This project implements an expense tracking system using Object-Oriented Programming in Python. It consists of two main classes: `Expense` for representing individual expenses and `ExpenseDB` for managing a collection of expenses.

## Features

- Create expenses with titles and amounts
- Generate unique IDs for each expense
- Track creation and update timestamps
- Update expense details
- Store and manage multiple expenses
- Search expenses by ID or title
- Convert expenses to dictionary format

## Requirements

- Python 3.10+
- Import UUID and Datetime from python.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/expense-tracker.git
cd expense-tracker
```

## Usage

Here's a simple example of how to use the expense tracker:

```python
from expense_tracking import expense, expense_db

# Create an expense database
db = expense_db()

# Create some expenses
expense1 = expense("Lunch", 15.50)
expense2 = expense("Office Supplies", 45.00)

# Add expenses to the database
db.add_expense(expense1)
db.add_expense(expense2)

# Update an expense
expense1.update(amount=20.00)

# Get an expense by ID
found_expense = db.get_expense_by_id(expense1.id)

# Get expenses by title
office_expenses = db.get_expense_by_title("Office Supplies")

# Convert all expenses to dictionary format
all_expenses = db.to_dict()
print(all_expenses)
```

## Testing

You can test the implementation by looking the the test.py file and run the code as follows:

```python
python test.py
```

Thank you.