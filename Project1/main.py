import tkinter as tk
from gui import CalculatorGUI

def main():
    # Initialize the application window
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
