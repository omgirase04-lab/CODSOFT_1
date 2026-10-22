"""Expanded rule-based chatbot for CodSoft AI Internship Task 1.

This chatbot uses hand-written rules and Python's standard library only.
It does not use a language model or learn from conversations.
"""

import random
import re
from datetime import datetime
from difflib import get_close_matches


class RuleBasedChatbot:
    """Respond to common questions using intents and predefined responses."""

    def __init__(self):
        self.rules = [
            # Greetings and social conversation
            (r"\b(hi|hello|hey|hiya|howdy)\b", [
                "Hello! 👋 What would you like to talk about?",
                "Hey there! I'm CodBot. How can I help?",
                "Hi! Ask me something, or type 'help' to see what I can do.",
            ]),
            (r"\bgood morning\b", ["Good morning! 🌞 Hope your day starts well."]),
            (r"\bgood afternoon\b", ["Good afternoon! What can I help you with?"]),
            (r"\bgood evening\b", ["Good evening! How has your day been?"]),
            (r"\bhow are you\b|\bhow('s| is) it going\b", [
                "I'm running smoothly—thanks for asking! How are you?",
                "Doing well! I'm ready to answer one of my supported questions.",
            ]),
            (r"\bwhat is your name\b|\bwho are you\b|\bintroduce yourself\b", [
                "I'm CodBot, a rule-based chatbot created for CodSoft AI Internship Task 1.",
            ]),
            (r"\bwho made you\b|\bwho created you\b|\bwho built you\b", [
                "I was built as a Python project to demonstrate rule-based conversation and pattern matching.",
            ]),
            (r"\bhow old are you\b", [
                "I don't have a human age. I'm a small Python program, so I start whenever you run me!",
            ]),
            (r"\bwhere do you live\b|\bwhere are you from\b", [
                "I live wherever this Python program is running—right now, that's your computer!",
            ]),
            (r"\b(can you|do you) (hear|see) me\b", [
                "I can read the text you type here, but this command-line version doesn't use a microphone or camera.",
            ]),
            (r"\bwhat can you do\b|\bwhat are your features\b|\bcapabilities\b", [
                "I can chat about greetings, small talk, jokes, motivation, Python, AI, machine learning, study tips, and the date/time. Type 'help' for examples.",
            ]),
            (r"\bhelp\b|\bwhat can i ask\b|\bcommands\b", [
                "Try asking: 'What is Python?', 'Explain AI', 'What is machine learning?', 'Tell me a joke', 'Motivate me', 'What time is it?', or 'Give me study tips'. Type 'bye' to exit.",
            ]),

            # Gratitude, politeness, and mood
            (r"\b(thanks|thank you|thx|thankyou)\b", [
                "You're welcome! 😊",
                "Anytime! Happy to help.",
                "You're welcome. Keep being curious!",
            ]),
            (r"\b(sorry|i apologize|my apologies)\b", [
                "No worries! We can keep going.",
            ]),
            (r"\b(i am sad|i'm sad|feeling sad|i feel sad|i am stressed|i'm stressed|feeling stressed)\b", [
                "I'm sorry you're feeling that way. Take one small step at a time, and consider talking with someone you trust if things feel heavy.",
            ]),
            (r"\b(i am happy|i'm happy|feeling happy|i feel great)\b", [
                "That's great to hear! 🎉 Hold on to that good energy.",
            ]),
            (r"\b(motivate me|motivation|inspire me|i need motivation)\b", [
                "You don't need to solve everything today. Do the next useful thing, repeat it tomorrow, and let consistency build your progress.",
                "Small efforts compound. Start with 20 focused minutes, finish one task, and give yourself credit for showing up.",
            ]),
            (r"\b(study tips|how do i study|how to study|study advice)\b", [
                "Try this: choose one clear goal, study for 25–50 minutes without distractions, solve questions from memory, take a short break, and review the topic tomorrow.",
            ]),
            (r"\b(joke|make me laugh|tell me something funny)\b", [
                "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
                "Why did the computer go to the doctor? It caught a virus!",
                "A SQL query walks into a bar, walks up to two tables, and asks: 'Can I join you?'",
            ]),
            (r"\b(fun fact|interesting fact)\b", [
                "Fun fact: the word 'algorithm' comes from the name of the mathematician Muhammad ibn Musa al-Khwarizmi.",
                "Fun fact: a computer can follow instructions extremely quickly, but the quality of its output still depends on the instructions and data it receives.",
            ]),
            (r"\b(what is the meaning of life|meaning of life)\b", [
                "There's no single answer for everyone. Many people find meaning in relationships, learning, contribution, creativity, and the values they choose to live by.",
            ]),

            # Programming and AI concepts
            (r"\bwhat is python\b|\bdefine python\b|\bpython language\b", [
                "Python is a high-level, general-purpose programming language known for readable syntax. It's used in automation, web development, data analysis, and AI.",
            ]),
            (r"\bwhat is a variable\b|\bdefine variable\b", [
                "A variable is a name that refers to a value. In Python, for example, `score = 10` binds the name score to the integer 10.",
            ]),
            (r"\bwhat is a function\b|\bdefine function\b", [
                "A function is a reusable block of code. In Python, define one with `def`, give it a name, and call it when you need its behaviour.",
            ]),
            (r"\bwhat is an algorithm\b|\bdefine algorithm\b", [
                "An algorithm is a finite, ordered set of steps for solving a problem or completing a task.",
            ]),
            (r"\bwhat is artificial intelligence\b|\bdefine ai\b|\bwhat is ai\b|\bexplain ai\b", [
                "Artificial intelligence (AI) is a field focused on building systems that perform tasks associated with abilities such as perception, reasoning, language, and decision-making.",
            ]),
            (r"\bwhat is machine learning\b|\bdefine machine learning\b|\bwhat is ml\b", [
                "Machine learning (ML) is a branch of AI in which systems learn patterns from data to make predictions or decisions, rather than relying only on hand-written rules.",
            ]),
            (r"\bdifference between ai and machine learning\b|\bai vs ml\b", [
                "AI is the broader field of building intelligent systems. Machine learning is one approach within AI that learns patterns from data.",
            ]),
            (r"\bwhat is deep learning\b|\bdefine deep learning\b", [
                "Deep learning is a type of machine learning that uses neural networks with multiple layers to learn complex patterns from data.",
            ]),
            (r"\bwhat is nlp\b|\bnatural language processing\b", [
                "Natural language processing (NLP) helps computers process and work with human language, for example by classifying text, translating, or answering questions.",
            ]),
            (r"\bwhat is a chatbot\b|\bdefine chatbot\b", [
                "A chatbot is a program that communicates with users through text or voice. A rule-based chatbot like me selects responses using predefined patterns and rules.",
            ]),
            (r"\bwhat is a database\b|\bdefine database\b", [
                "A database is an organized collection of data that can be stored, queried, updated, and managed.",
            ]),
            (r"\bwhat is git\b|\bdefine git\b", [
                "Git is a version-control system that tracks changes to files and helps developers collaborate and return to earlier versions.",
            ]),
            (r"\bwhat is github\b|\bdefine github\b", [
                "GitHub is an online platform for hosting Git repositories and collaborating on software projects through tools such as issues and pull requests.",
            ]),
            (r"\bwhat is an api\b|\bdefine api\b", [
                "An API (Application Programming Interface) is a defined way for software components to communicate and request services or data from one another.",
            ]),
            (r"\bwhat is overfitting\b|\bdefine overfitting\b", [
                "Overfitting happens when a model learns the training data too specifically, including noise, and then performs poorly on new data.",
            ]),
            (r"\bwhat is a neural network\b|\bdefine neural network\b", [
                "A neural network is a machine-learning model made of connected computational units arranged in layers, which learn patterns by adjusting parameters during training.",
            ]),
            (r"\bwhat is data science\b|\bdefine data science\b", [
                "Data science combines programming, statistics, and domain knowledge to extract useful insights from data.",
            ]),
            (r"\bwhat is plagiarism\b|\bdefine plagiarism\b", [
                "Plagiarism is presenting someone else's words, ideas, or work as your own without appropriate acknowledgment.",
            ]),

            # Date, time, and conversation control
            (r"\b(what is the )?time\b|\bcurrent time\b", [
                lambda: f"The current local time is {datetime.now().strftime('%I:%M:%S %p')}.",
            ]),
            (r"\b(today'?s date|what is the date|current date|what day is it)\b", [
                lambda: f"Today is {datetime.now().strftime('%A, %d %B %Y')}.",
            ]),
            (r"\b(bye|goodbye|see you|exit|quit)\b", [
                "Goodbye! 👋 Keep learning, one step at a time.",
            ]),
        ]

    def get_response(self, message: str) -> str:
        """Return a response for a message using the first matching rule."""
        cleaned = re.sub(r"\s+", " ", message.strip().lower())
        if not cleaned:
            return "Please type a message so I can help."

        for pattern, responses in self.rules:
            if re.search(pattern, cleaned):
                response = random.choice(responses)
                return response() if callable(response) else response

        # Conservative typo-tolerant fallback for common single-word greetings.
        tokens = re.findall(r"[a-z']+", cleaned)
        known_short_words = ["hello", "hi", "hey", "thanks", "bye", "joke", "help"]
        for token in tokens:
            close = get_close_matches(token, known_short_words, n=1, cutoff=0.82)
            if close:
                alias = {
                    "hello": "hello",
                    "hi": "hi",
                    "hey": "hey",
                    "thanks": "thanks",
                    "bye": "bye",
                    "joke": "joke",
                    "help": "help",
                }[close[0]]
                for pattern, responses in self.rules:
                    if re.search(pattern, alias):
                        response = random.choice(responses)
                        return response() if callable(response) else response

        return (
            "I don't know that one yet. I'm a rule-based chatbot, so I answer "
            "questions covered by my rules. Try 'help', 'explain AI', "
            "'what is Python?', 'tell me a joke', or 'give me study tips'."
        )


def main():
    bot = RuleBasedChatbot()
    print("=" * 62)
    print("                         CODBOT")
    print("       Expanded Rule-Based Chatbot | CodSoft Task 1")
    print("=" * 62)
    print("CodBot: Hello! Type 'help' for examples or 'bye' to exit.")

    while True:
        try:
            user_message = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nCodBot: Goodbye! 👋 Keep learning, one step at a time.")
            break

        response = bot.get_response(user_message)
        print(f"CodBot: {response}")

        if re.search(r"\b(bye|goodbye|see you|exit|quit)\b", user_message.strip().lower()):
            break


if __name__ == "__main__":
    main()
