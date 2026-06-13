import tkinter as tk
from tkinter import scrolledtext
import json
import random

# ==========================
# LOAD KNOWLEDGE BASE
# ==========================

knowledge = {}

files = [
    "data/health.json",
    "data/programming.json",
    "data/science.json",
    "data/mathematics.json",
    "data/history.json",
    "data/technology.json"
]

for file_name in files:
    with open(file_name, "r", encoding="utf-8") as file:
        data = json.load(file)
        knowledge.update(data)

# ==========================
# CHATBOT RESPONSE FUNCTION
# ==========================

def get_response(question):

    question = question.lower().strip()

    # Greetings
    if question in ["hello", "hi", "hey"]:
        greetings = [
            "Hello! How can I help you today?",
            "Hi there!",
            "Welcome back!",
            "Nice to see you!"
        ]
        return random.choice(greetings)

    elif question == "good morning":
        return "Good morning! Have a great day."

    elif question == "good afternoon":
        return "Good afternoon!"

    elif question == "good evening":
        return "Good evening!"

    # Emotions
    elif "happy" in question:
        return "That's wonderful to hear!"

    elif "sad" in question:
        return "I hope things get better soon."

    elif "stressed" in question:
        return "Try taking one task at a time."

    elif "tired" in question:
        return "Make sure you get enough rest."

    # Exact Match
    elif question in knowledge:
        return knowledge[question]

    # Keyword Search
    else:

        for key, answer in knowledge.items():

            key_words = key.lower().split()
            user_words = question.lower().split()

            for word in user_words:

                if word in key_words:
                    return answer

        return "Sorry, I don't know that answer yet."

# ==========================
# SEND MESSAGE FUNCTION
# ==========================

def send_message():

    user_message = message_entry.get().strip()

    if user_message == "":
        return

    # Show User Message
    chat_area.insert(tk.END, f"You: {user_message}\n")

    # Get Bot Response
    bot_response = get_response(user_message)

    # Show Bot Response
    chat_area.insert(tk.END, f"Bot: {bot_response}\n\n")

    # Clear Input Box
    message_entry.delete(0, tk.END)

    # Auto Scroll
    chat_area.see(tk.END)

# ==========================
# SEND ON ENTER KEY
# ==========================

def enter_key(event):
    send_message()

# ==========================
# MAIN WINDOW
# ==========================

root = tk.Tk()

root.title("Student Assistant Chatbot")

root.geometry("800x600")

# Chat Area

chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    font=("Arial", 11)
)

chat_area.pack(
    padx=10,
    pady=10,
    fill=tk.BOTH,
    expand=True
)

# Input Frame

input_frame = tk.Frame(root)

input_frame.pack(
    fill=tk.X,
    padx=10,
    pady=10
)

# Entry Box

message_entry = tk.Entry(
    input_frame,
    font=("Arial", 11)
)

message_entry.pack(
    side=tk.LEFT,
    fill=tk.X,
    expand=True,
    padx=(0, 10)
)

message_entry.bind("<Return>", enter_key)

# Send Button

send_button = tk.Button(
    input_frame,
    text="Send",
    command=send_message
)

send_button.pack(side=tk.RIGHT)

# Welcome Message

chat_area.insert(
    tk.END,
    "Bot: Welcome to Student Assistant Chatbot!\n"
    "Ask me questions about Health, Programming, Science, Mathematics, History and Technology.\n\n"
)

# Run App

root.mainloop()