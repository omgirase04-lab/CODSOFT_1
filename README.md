# CodBot — Expanded Rule-Based Chatbot
### CodSoft Artificial Intelligence Internship · Task 1

CodBot is a command-line chatbot built with Python. It uses predefined responses, regular expressions, and a small typo-tolerant fallback to answer a wider range of common questions.

## Features

- Greetings, small talk, identity, capabilities, and help
- Thanks, apologies, mood support, jokes, fun facts, and motivation
- Study tips
- Introductory explanations of Python, variables, functions, algorithms, AI, machine learning, deep learning, NLP, chatbots, databases, Git, GitHub, APIs, neural networks, overfitting, data science, and plagiarism
- Current local date and time
- Unknown-question fallback that suggests supported prompts
- Basic typo tolerance for common short words
- Automated unit tests
- No third-party dependencies

## Requirements

Python 3.9 or newer. No `pip install` step is required.

## Run

```bash
python chatbot.py
```

Type `help` for example questions. Type `bye`, `goodbye`, `exit`, or `quit` to end the session.

## Run tests

```bash
python -m unittest -v
```

## Example prompts

```text
Hello!
What can you do?
What is Python?
Explain AI.
What is the difference between AI and machine learning?
What is overfitting?
Tell me a joke.
Motivate me.
Give me study tips.
What time is it?
What is today's date?
bye
```

## How it works

1. Normalizes the message by trimming and collapsing whitespace, then converts it to lowercase.
2. Checks the message against an ordered list of regular-expression rules.
3. Returns one of the predefined responses for the first matching rule. Date and time responses are generated at runtime.
4. Uses a conservative fuzzy match for common short words if no rule matches.
5. Returns a helpful fallback if no rule matches.

## Important limitation

CodBot is still a **rule-based** chatbot, not a generative AI system. It does not understand every question, learn from conversations, or verify factual answers online. It can only answer patterns covered by its rules. The typo-tolerant fallback is intentionally limited.

## Project structure

```text
CODSOFT_TASK1/
├── chatbot.py
├── test_chatbot.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Push to GitHub

Create a repository with the name required by your internship coordinator. The PDF asks interns to keep tasks in a separate repository named according to the `CODSOFT_TASKSNO` convention. If one repository must hold all tasks, place this project in a `Task1/` subfolder.

```bash
git init
git add .
git commit -m "Expand CodSoft Task 1 rule-based chatbot"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/CODSOFT_TASKSNO.git
git push -u origin main
```

Replace `YOUR_USERNAME` and the repository name with your actual details.

## Demo video outline (60–90 seconds)

1. Introduce the project as CodSoft AI Internship Task 1.
2. Explain rule-based responses and regular-expression matching.
3. Run the chatbot and demonstrate greeting, Python/AI explanation, a joke, study tips, date/time, and an unknown question.
4. Run `python -m unittest -v`.
5. Show the real GitHub repository URL.

## Suggested LinkedIn caption

> I expanded my CodSoft AI Internship Task 1 project: CodBot, a rule-based chatbot built with Python. It handles greetings, small talk, motivation, study tips, jokes, and introductory programming and AI questions using predefined patterns and responses. I also added unit tests and a helpful fallback for unsupported questions.
>
> GitHub: [add your real repository link]
>
> @CODSOFT #codsoft #artificialintelligence #python #internship #chatbot
