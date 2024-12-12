import tkinter as tk
from tkinter import messagebox
from logic import Logic

class CalculatorGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Enhanced Calculator")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        # Input fields
        self.num_input = tk.Entry(root, width=30)
        self.num_input.grid(row=0, column=1, padx=10, pady=10)

        # Dropdown menu for operations
        self.operator_var = tk.StringVar(root)
        self.operator_var.set("add")  # Default value
        self.operator_menu = tk.OptionMenu(root, self.operator_var, "add", "subtract", "multiply", "divide")
        self.operator_menu.grid(row=1, column=1, padx=10, pady=10)

        # Calculate button
        self.calc_button = tk.Button(root, text="Calculate", command=self.calculate)
        self.calc_button.grid(row=2, column=1, padx=10, pady=10)

        # Output label
        self.result_label = tk.Label(root, text="Result: ", font=("Arial", 14))
        self.result_label.grid(row=3, column=1, padx=10, pady=10)

        # History button
        self.history_button = tk.Button(root, text="View History", command=self.view_history)
        self.history_button.grid(row=4, column=1, padx=10, pady=10)

        # Clear history button
        self.clear_history_button = tk.Button(root, text="Clear History", command=self.clear_history)
        self.clear_history_button.grid(row=5, column=1, padx=10, pady=10)

    def calculate(self):
        """Calculate the result of the selected operation."""
        try:
            numbers = list(map(float, self.num_input.get().split(',')))  # Accept input as comma-separated numbers
            operator = self.operator_var.get()

            # Perform operations based on user selection
            if operator == "add":
                result = Logic.add(numbers)
            elif operator == "subtract":
                result = Logic.subtract(numbers)
            elif operator == "multiply":
                result = Logic.multiply(numbers)
            elif operator == "divide":
                result = Logic.divide(numbers)
            else:
                raise ValueError("Invalid operator.")

            self.result_label.config(text=f"Result: {result:.2f}")
            self.save_to_history(operator, numbers, result)  # Save results to history
        except ZeroDivisionError as e:
            messagebox.showerror("Error", str(e))
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Enter numbers separated by commas.")

    def save_to_history(self, operator, numbers, result):
        """Save the operation and result to a history file."""
        with open("history.txt", "a") as file:
            file.write(f"{operator}({', '.join(map(str, numbers))}) = {result:.2f}\n")

    def view_history(self):
        """View calculation history."""
        try:
            with open("history.txt", "r") as file:
                history = file.read()
            messagebox.showinfo("History", history if history else "No history available.")
        except FileNotFoundError:
            messagebox.showerror("Error", "No history file found.")

    def clear_history(self):
        """Clear the history file."""
        with open("history.txt", "w") as file:
            file.write("")
        messagebox.showinfo("History", "Calculation history cleared.")
