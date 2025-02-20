from expense_tracking import expense, expense_db
# Create a database
db = expense_db()

# Create and add some expenses
lunch = expense("Lunch", 15.50)
dinner = expense("Dinner", 25.00)
db.add_expense(lunch)
db.add_expense(dinner)

# Update an expense
lunch.update(amount=18.50)

# Find expenses
lunch_expenses = db.get_expense_by_title("Lunch")
specific_expense = db.get_expense_by_id(lunch.id)

# Get all expenses as dictionaries
all_expenses = db.to_dict()
print(all_expenses)