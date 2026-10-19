
import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

text_input = tk.Label(root, text="", font=("Arial", 16))
text_input.pack()

text_result = tk.Label(root, text="Result: ", font=("Arial", 14))
text_result.pack()

expression = ""

def press(value):
    global expression
    expression += str(value)
    text_input.config(text=expression)

def multiply():
    press("*")

def divide():
    press("/")

def summy():
    press("+")

def diff():
    press("-")

def result():
    global expression
    try:
        answer = eval(expression)
        text_result.config(text=f"Result: {answer}")
        expression = str(answer)
        text_input.config(text=expression)
    except:
        text_result.config(text="Error")

# 10 кнопок с цифрами
for i in range(10):
    tk.Button(root, text=str(i), command=lambda n=i: press(n)).pack()

# Матрица арифметических операций
operations = [
    ("*", multiply),
    ("/", divide),
    ("+", summy),
    ("-", diff),
    ("=", result)
]

# 5 кнопок операций
for text, command in operations:
    tk.Button(root, text=text, command=command).pack()

root.mainloop()
