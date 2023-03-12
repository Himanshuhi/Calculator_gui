import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        
        # Entry widget to display the result
        self.result = tk.Entry(master, width=24, font=('Arial', 16))
        self.result.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # List of calculator buttons and their positions
        buttons = [
            {'text': '7', 'row': 1, 'col': 0},
            {'text': '8', 'row': 1, 'col': 1},
            {'text': '9', 'row': 1, 'col': 2},
            {'text': '/', 'row': 1, 'col': 3},
            {'text': '4', 'row': 2, 'col': 0},
            {'text': '5', 'row': 2, 'col': 1},
            {'text': '6', 'row': 2, 'col': 2},
            {'text': '*', 'row': 2, 'col': 3},
            {'text': '1', 'row': 3, 'col': 0},
            {'text': '2', 'row': 3, 'col': 1},
            {'text': '3', 'row': 3, 'col': 2},
            {'text': '-', 'row': 3, 'col': 3},
            {'text': '0', 'row': 4, 'col': 0},
            {'text': '.', 'row': 4, 'col': 1},
            {'text': '=', 'row': 4, 'col': 2},
            {'text': '+', 'row': 4, 'col': 3},
        ]
        
        # Create and place the calculator buttons
        for button in buttons:
            text = button['text']
            row = button['row']
            col = button['col']
            cmd = lambda text=text: self.button_click(text)
            tk.Button(master, text=text, width=6, height=2, font=('Arial', 16), command=cmd).grid(row=row, column=col, padx=5, pady=5)
        
        # Clear button
        tk.Button(master, text='C', width=6, height=2, font=('Arial', 16), command=self.clear_result).grid(row=5, column=0, padx=5, pady=5)
        
    def button_click(self, text):
        if text == '=':
            # Evaluate the expression and update the result
            try:
                result = str(eval(self.result.get()))
            except:
                result = 'Error'
            self.result.delete(0, tk.END)
            self.result.insert(0, result)
        else:
            # Add the clicked button text to the expression
            self.result.insert(tk.END, text)
        
    def clear_result(self):
        self.result.delete(0, tk.END)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
