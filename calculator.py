import tkinter as tk
from functools import partial

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        # Entry widget to display expressions and results
        self.display = tk.Entry(master, font=("Arial", 18), borderwidth=2, relief="ridge", justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")
        
        # Create a list of button labels for the calculator
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('/', 4, 3),
        ]

        # Add a clear button (C) at the bottom
        buttons.append(('C', 5, 0))
        
        # Create buttons and place them in the grid
        for (text, row, col) in buttons:
            action = partial(self.on_button_click, text)
            tk.Button(master, text=text, width=5, height=2, command=action, font=("Arial", 14)).grid(row=row, column=col, padx=5, pady=5)
        
        # Make columns and rows stretch with window resizing
        for i in range(4):
            master.columnconfigure(i, weight=1)
        for i in range(6):
            master.rowconfigure(i, weight=1)

    def on_button_click(self, char):
        # If the '=' is pressed, evaluate the expression
        if char == '=':
            expr = self.display.get()
            try:
                # Evaluate the expression safely
                # Note: eval is dangerous if used with untrusted input.
                # For a calculator, it's generally fine since the input is restricted to digits and operators.
                result = eval(expr)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception:
                # If an error occurred (like division by zero), display an error message
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif char == 'C':
            # Clear the display
            self.display.delete(0, tk.END)
        else:
            # For numbers and operators, append them to the display
            current = self.display.get()
            # Replace 'Error' if currently displayed
            if current == "Error":
                current = ""
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, current + char)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
