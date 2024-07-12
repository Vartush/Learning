import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from collections import defaultdict

# Create the main application window
root = tk.Tk()
root.title("Button Press Recorder")

# Dictionary to keep track of button presses by date
press_counts = defaultdict(int)

def record_press():
    # Get the current date
    current_date = datetime.now().strftime("%Y-%m-%d")
    # Increment the count for the current date
    press_counts[current_date] += 1
    # Display the updated counts
    display_counts()

def display_counts():
    # Clear the text widget
    text_widget.delete(1.0, tk.END)
    # Display the counts in the text widget
    for date, count in press_counts.items():
        text_widget.insert(tk.END, f"{date}: {count} times\n")

# Create a button and attach the record_press function to it
button = tk.Button(root, text="Press Me", command=record_press)
button.pack(pady=20)

# Create a text widget to display the counts
text_widget = tk.Text(root, height=10, width=30)
text_widget.pack(pady=20)

# Run the application
root.mainloop()
