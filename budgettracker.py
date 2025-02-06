import tkinter as tk
from tkinter import messagebox

class User:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary 

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

class Expenses:
    def __init__(self):
        self.expenses = []  # Stores expense records as (price, category) 

    def log_expense(self, price, category):
        self.expenses.append((price, category))

    def get_total_expenses(self):
        return sum(price for price, _ in self.expenses)

class BudgetTracker:
    def __init__(self, window):
        self.window = window
        self.window.title("Your Budget Bestie")

        self.user = None
        self.expenses = Expenses()

        self.create_user_frame()
        self.create_expenses_frame()
        self.create_summary_frame()

    def create_user_frame(self):
        user_frame = tk.Frame(self.window)
        user_frame.pack(pady=10)

        tk.Label(user_frame, text="Name").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(user_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(user_frame, text="Age").grid(row=1, column=0, padx=5, pady=5)
        self.age_entry = tk.Entry(user_frame)
        self.age_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(user_frame, text="Salary").grid(row=2, column=0, padx=5, pady=5)
        self.salary_entry = tk.Entry(user_frame)
        self.salary_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(user_frame, text="Set Budget", command=self.set_budget).grid(row=3, column=0, columnspan=2, pady=5)

    def create_expenses_frame(self):
        expenses_frame = tk.Frame(self.window)
        expenses_frame.pack(padx=10, pady=10)

        tk.Label(expenses_frame, text="Price").grid(row=0, column=0, padx=5, pady=5)
        self.price_entry = tk.Entry(expenses_frame)
        self.price_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(expenses_frame, text="Category").grid(row=1, column=0, padx=5, pady=5)
        self.category_entry = tk.Entry(expenses_frame)
        self.category_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(expenses_frame, text="Add Expense", command=self.add_expense).grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        tk.Button(expenses_frame, text="View Expenses", command=self.view_expenses).grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def create_summary_frame(self):
        self.summary_frame = tk.Frame(self.window)
        self.summary_frame.pack(pady=10)

        self.savings_label = tk.Label(self.summary_frame, text="Your Savings: $0", font=("Arial", 12, "bold"))
        self.savings_label.pack()

    def set_budget(self):
        try:
            name = self.name_entry.get()
            age = int(self.age_entry.get())
            salary = float(self.salary_entry.get())

            self.user = User(name, age, salary)
            messagebox.showinfo("Budget Set", f"Budget set for {self.user.name} with a salary of ${self.user.salary:.2f}")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for age and salary.")

    def add_expense(self):
        if not self.user:
            messagebox.showwarning("No Budget Set", "Please enter your budget details first.")
            return

        try:
            price = float(self.price_entry.get())
            category = self.category_entry.get()

            if price <= 0:
                raise ValueError

            self.expenses.log_expense(price, category)
            messagebox.showinfo("Expense Logged", f"Added ${price:.2f} under {category}.")

            self.update_savings()

        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid price.")

    def view_expenses(self):
        if not self.expenses.expenses:
            messagebox.showinfo("No Expenses", "You have not logged any expenses yet.")
            return

        expense_list = "\n".join([f"${price:.2f} - {category}" for price, category in self.expenses.expenses])
        messagebox.showinfo("Expenses", f"Your Expenses:\n{expense_list}")

    def update_savings(self):
        if self.user:
            total_expenses = self.expenses.get_total_expenses()
            savings = self.user.salary - total_expenses
            self.savings_label.config(text=f"Your Savings: ${savings:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="White")
    app = BudgetTracker(root)
    root.mainloop()


        

