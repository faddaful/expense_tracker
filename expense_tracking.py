import uuid
from datetime import datetime, timezone

class expense:
    def __init__(self, title: str, amount: float):
        """
        Initializes an expense with title and amount.

        Args:
            title (str): The title of the expense.
            amount (float): The amount of the expense.
        """
        
        self.id = uuid.uuid4()
        self.title = title
        self.amount = amount
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = self.created_at

    def update(self, title: str = None, amount: float = None):
        """
        Updates the expense title and amount of the expense.

        Args:
            title (str): The new title of the expense.
            amount (float): The new amount of the expense.
        """
        
        if title is not None:
            self.title = title
        if amount is not None:
            self.amount = amount
        self.updated_at = datetime.now(timezone.utc)

    
    def to_dict(self):
        """
        Returns the expenses as a dictionary.

        Returns:
            dict: The expenses as a dictionary.
        """
        
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
class expense_db:
    def __init__(self):
        """
        Initializes the expense database.
        """
        
        self.expenses = {}

    def add_expense(self, expense: expense):
        """
        Adds an expense to the expense database.

        Args:
            expense (expense): The expense to add.
        """
        
        self.expenses[expense.id] = expense

    def remove_expense(self, id: uuid):
        """
        Removes an expense from the expense database.

        Args:
            id (uuid): The id of the expense to remove.
        """
        
        for expense in list(self.expenses.values()):
            if expense.id == id:
                del self.expenses[expense.id]
                return     
        raise ValueError("Expense with the given ID does not exist.")
            
    def get_expense_by_id(self, id: uuid):
        """
        Returns the expense with the given id.

        Args:
            id (uuid): The id of the expense to return.

        Returns:
            expense: The expense with the given id.
        """
        
        for expense in self.expenses.values():
            if expense.id == id:
                return expense
        raise ValueError("Expense with the given ID does not exist.")
    
    def get_expense_by_title(self, title: str):
        """
        Returns the expense with the given title.

        Args:
            title (str): The title of the expense to return.

        Returns:
            expense: The expense with the given title.
        """
        
        for expense in self.expenses.values():
            if expense.title == title:
                return expense
        raise ValueError("Expense with the given title does not exist.")
    
    def to_dict(self):
        """
        Returns the expenses as a dictionary.

        Returns:
            dict: The expenses as a dictionary.
        """
        
        return {expense.id: expense.to_dict() for expense in self.expenses.values()}