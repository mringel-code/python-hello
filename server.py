import tkinter as tk
def display_text():
    label.config(text="Hello, AWS App Runner!")

root = tk.Tk()
root.title("Simple Python GUI App")

label = tk.Label(root, text="Press the button...")
label.pack()

button = tk.Button(root, text="Click Me!", command=display_text)
button.pack()

root.mainloop()ver.serve_forever()
