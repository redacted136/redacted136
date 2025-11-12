import tkinter as tk

def button_click():
    " when the button is clicked."""
    label.config(text="Button clicked!")

# Create the main window
root = tk.Tk()
root.title("Tkinter Example")
root.geometry("300x200") # Set initial window size

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20) # Add some padding

# Create a button widget
button = tk.Button(root, text="Click Me", command=button_click)
button.pack()

# Start the Tkinter event loop
root.mainloop()