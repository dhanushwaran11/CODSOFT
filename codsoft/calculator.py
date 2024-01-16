import tkinter as tk

def on_click(button_text):
    current_text = entry_var.get()

    if button_text == "=":
        try:
            result = eval(current_text)
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif button_text == "C":
        entry_var.set("")
    else:
        entry_var.set(current_text + button_text)


calculator = tk.Tk()
calculator.title("python Calculator")
calculator.geometry("500x700")

entry_var = tk.StringVar()
entry = tk.Entry(calculator, textvariable=entry_var, font=("Helvetica", 35), justify="right",bg="grey")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

row_val = 1
col_val = 0

for button_text in buttons:
    tk.Button(calculator, text=button_text, width=10, height=5, bg="orange", command=lambda b=button_text: on_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

for i in range(1, 5):
    calculator.grid_rowconfigure(i, weight=1)
    calculator.grid_columnconfigure(i, weight=1)

calculator.mainloop()
