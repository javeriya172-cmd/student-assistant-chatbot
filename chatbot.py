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
    with open(file_name, "r") as file:
        data = json.load(file)
        knowledge.update(data)

# ==========================
# LOAD QUIZ QUESTIONS
# ==========================

with open("data/quiz.json", "r") as file:
    quiz_questions = json.load(file)

# ==========================
# WELCOME MESSAGE
# ==========================

print("=" * 50)
print("     STUDENT ASSISTANT CHATBOT")
print("=" * 50)
print("Type 'help' for commands")
print("Type 'bye' to exit")
print("=" * 50)

# ==========================
# CHAT LOOP
# ==========================

while True:

    question = input("\nYou: ").lower().strip()

    # EXIT
    if question == "bye":
        print("Bot: Goodbye! Happy Learning!")
        break

    # HELP
    elif question == "help":
        print("\nCommands:")
        print("help   - Show commands")
        print("topics - Show available subjects")
        print("quiz   - Start a quiz")
        print("bye    - Exit chatbot")

    # TOPICS
    elif question == "topics":
        print("\nAvailable Subjects:")
        print("- Health")
        print("- Programming")
        print("- Science")
        print("- Mathematics")
        print("- History")
        print("- Technology")

    # GREETINGS
    elif question in ["hello", "hi", "hey"]:
        print("Bot: Hello! How can I help you today?")

    elif question == "good morning":
        print("Bot: Good morning! Have a great day.")

    elif question == "good afternoon":
        print("Bot: Good afternoon!")

    elif question == "good evening":
        print("Bot: Good evening!")

    # EMOTIONS
    elif "happy" in question:
        print("Bot: That's wonderful to hear!")

    elif "sad" in question:
        print("Bot: I hope things get better soon.")

    elif "stressed" in question:
        print("Bot: Try taking one task at a time.")

    elif "tired" in question:
        print("Bot: Make sure you get enough rest.")

    # QUIZ MODE
    elif question == "quiz":

        score = 0

        questions = random.sample(
            list(quiz_questions.keys()),
            min(5, len(quiz_questions))
        )

        print("\nStarting Quiz...\n")

        for q in questions:

            print(q)

            answer = input("Your Answer: ").lower().strip()

            if answer == quiz_questions[q]:
                print("Correct!\n")
                score += 1

            else:
                print("Wrong!")
                print("Correct Answer:", quiz_questions[q])
                print()
            if answer =="exit":
                print("Exiting quiz")
                break     

        print("=" * 30)
        print("Quiz Finished!")
        print(f"Your Score: {score}/{len(questions)}")
        print("=" * 30)

       # Exact Match
    elif question in knowledge:
        print("Bot:", knowledge[question])

      # Keyword Search
else:

    found = False

    for key, answer in knowledge.items():

        key_words = key.lower().split()
        user_words = question.lower().split()

        for word in user_words:

            if word in key_words:
                print("Bot:", answer)
                found = True
                break

        if found:
            break

    if not found:
        print("Bot: Sorry, I don't know that answer yet.")