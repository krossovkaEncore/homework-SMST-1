import tkinter as tk

root = tk.Tk()
root.geometry("300x300")

buttons = [tk.Button(root, text=str(i)) for i in range(8)]
positions = [(1, 1), (1, 2), (1, 3), (2, 3),
             (3, 3), (3, 2), (3, 1), (2, 1)]

i = 0
while i < len(buttons):
    buttons[i].grid(row=positions[i][0], column=positions[i][1])
    i += 1

root.mainloop()
