import json
import random

# ==========================
# SAVE CHAT HISTORY
# ==========================

def save_chat(user_message, bot_response):
    with open("chat_history.txt", "a", encoding="utf-8") as file:
        file.write(f"User: {user_message}\n")
        file.write(f"Bot: {bot_response}\n\n")
# ==========================
# SAVE STATISTICS
# ==========================

def save_stats():
    stats = {
        "questions_asked": questions_asked,
        "quiz_attempts": quiz_attempts,
        "correct_answers": correct_answers
    }

    with open("stats.json", "w", encoding="utf-8") as file:
        json.dump(stats, file, indent=4)

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
# LOAD QUIZ QUESTIONS
# ==========================

with open("data/quiz.json", "r", encoding="utf-8") as file:
    quiz_questions = json.load(file)


# ==========================
# STATISTICS
# ==========================

# ==========================
# LOAD STATISTICS
# ==========================

with open("stats.json", "r", encoding="utf-8") as file:
    stats = json.load(file)

questions_asked = stats["questions_asked"]
quiz_attempts = stats["quiz_attempts"]
correct_answers = stats["correct_answers"]


# ==========================
# WELCOME MESSAGE
# ==========================

print("=" * 50)
print("      STUDENT ASSISTANT CHATBOT")
print("=" * 50)
print("Type 'help' for commands")
print("Type 'bye' to exit")
print("=" * 50)


# ==========================
# CHAT LOOP
# ==========================

while True:

    question = input("\nYou: ").lower().strip()
    questions_asked += 1
    save_stats()

    # EXIT
    if question == "bye":

        response = "Goodbye! Happy Learning!"
        print("Bot:", response)
        save_chat(question, response)
        break

    # HELP
    elif question == "help":

        response = """
Commands:
help     - Show commands
topics   - Show available subjects
quiz     - Start a quiz
history  - View chat history
stats    - View statistics
bye      - Exit chatbot
"""

        print(response)
        save_chat(question, response)

    # TOPICS
    elif question == "topics":

        response = """
Available Subjects:
- Health
- Programming
- Science
- Mathematics
- History
- Technology
"""

        print(response)
        save_chat(question, response)

    # CHAT HISTORY
    elif question == "history":

        try:
            with open("chat_history.txt", "r", encoding="utf-8") as file:
                print("\n===== CHAT HISTORY =====")
                print(file.read())
                print("========================")
        except FileNotFoundError:
            print("No chat history found.")

    # STATISTICS
    elif question == "stats":

        response = f"""
===== STATISTICS =====
Questions Asked : {questions_asked}
Quiz Attempts   : {quiz_attempts}
Correct Answers : {correct_answers}
======================
"""

        print(response)
        save_chat(question, response)

    # GREETINGS
    elif question in ["hello", "hi", "hey"]:

        response = "Hello! How can I help you today?"
        print("Bot:", response)
        save_chat(question, response)

    elif question == "good morning":

        response = "Good morning! Have a great day."
        print("Bot:", response)
        save_chat(question, response)

    elif question == "good afternoon":

        response = "Good afternoon!"
        print("Bot:", response)
        save_chat(question, response)

    elif question == "good evening":

        response = "Good evening!"
        print("Bot:", response)
        save_chat(question, response)

    # EMOTIONS
    elif "happy" in question:

        response = "That's wonderful to hear!"
        print("Bot:", response)
        save_chat(question, response)

    elif "sad" in question:

        response = "I hope things get better soon."
        print("Bot:", response)
        save_chat(question, response)

    elif "stressed" in question:

        response = "Try taking one task at a time."
        print("Bot:", response)
        save_chat(question, response)

    elif "tired" in question:

        response = "Make sure you get enough rest."
        print("Bot:", response)
        save_chat(question, response)

    # QUIZ MODE
    elif question == "quiz":

        quiz_attempts += 1
        save_stats()
        score = 0

        questions = random.sample(
            list(quiz_questions.keys()),
            min(5, len(quiz_questions))
        )

        print("\nStarting Quiz...")
        print("Type 'exit' anytime to leave the quiz.\n")

        for q in questions:

            print(q)

            answer = input("Your Answer: ").lower().strip()

            if answer == "exit":
                print("Exiting Quiz...")
                break

            if answer == quiz_questions[q]:

                print("Correct!\n")
                score += 1
                correct_answers += 1
                save_stats()

            else:

                print("Wrong!")
                print("Correct Answer:", quiz_questions[q])
                print()

        response = f"Quiz Finished! Your Score: {score}/{len(questions)}"

        print("=" * 30)
        print(response)
        print("=" * 30)

        save_chat(question, response)

    # EXACT MATCH
    elif question in knowledge:

        response = knowledge[question]
        print("Bot:", response)
        save_chat(question, response)

    # KEYWORD SEARCH
    else:

        found = False

        for key, answer in knowledge.items():

            key_words = key.lower().split()
            user_words = question.lower().split()

            for word in user_words:

                if word in key_words:

                    response = answer
                    print("Bot:", response)
                    save_chat(question, response)

                    found = True
                    break

            if found:
                break

        if not found:

            response = "Sorry, I don't know that answer yet."
            print("Bot:", response)
            save_chat(question, response)