import tkinter as tk

root = tk.Tk()

root.geometry("400x300")
root.title("My Application")
# root.iconbitmap("icon.ico")

label = tk.Label(root, text="Hello, World!")
label.pack()

button = tk.Button(root, text="Click me")
button.pack()

root.mainloop()
