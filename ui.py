import tkinter as tk
from tkinter import scrolledtext
from chat import chat  # Import the chat function from chatbot.py

def send_message():
    user_message = user_input.get()
    history.insert(tk.END, f"You: {user_message}\n")
    response = chat(user_message)  # Call the chatbot function
    history.insert(tk.END, f"Psychologist: {response}\n")
    user_input.delete(0, tk.END)

# Initialize the window
window = tk.Tk()
window.title("Friendly Psychologist Chatbot")

# Text area for chat history
history = scrolledtext.ScrolledText(window, wrap=tk.WORD, height=15, width=50)
history.grid(row=0, column=0, padx=10, pady=10)

# Text box for user input
user_input = tk.Entry(window, width=40)
user_input.grid(row=1, column=0, padx=10, pady=10)

# Send button
send_button = tk.Button(window, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

window.mainloop()
