# Science Quiz Bot

A **Telegram bot** for science quizzes with an **admin panel** to manage questions, categories, broadcasts, and view user statistics. Built with **Python**, **Pyrogram**, **Flask**, and **MongoDB**.

---

## Features

### Bot
- Telegram-based quiz bot.
- Supports **multiple-choice** and **text-based answers**.
- Tracks user scores and attempts.
- Leaderboard functionality.
- Supports **categories** for questions.

### Admin Panel
- Web-based panel built with Flask.
- Add, edit, delete **questions** and **categories**.
- Broadcast messages to all users.
- View **leaderboard** and user stats.
- Dark mode support.

### Deployment
- Fully **Dockerized**.
- Can be deployed with **Docker Compose**.
- Supports **systemd** or **Supervisor** for background services.
- MongoDB database with **initial backup and migrations**.

---

## Repository Structure

```text
science-quiz-bot/
│
├── README.md
├── .env.example
├── .gitignore
│
├── bot/
│   ├── main.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── __init__.py
│   ├── utils/
│   │   ├── db.py
│   │   └── helpers.py
│   ├── handlers/
│   │   ├── start.py
│   │   ├── quiz.py
│   │   ├── callback.py
│   │   ├── text_answer.py
│   │   └── user_stats.py
│   ├── models/
│   │   ├── user_model.py
│   │   ├── question_model.py
│   │   └── attempts_model.py
│   └── data/
│       └── sample_questions.json
│
├── admin-panel/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── templates/
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   └── modules/
│       ├── auth.py
│       ├── questions.py
│       ├── categories.py
│       ├── users.py
│       └── broadcast.py
│
├── deployment/
│   ├── docker-compose.yml
│   ├── nginx.conf
│   ├── supervisor/
│   └── systemd/
│
└── database/
    ├── init.js
    ├── backup/
    │   └── questions.json
    └── migrations/
        └── 001_init_collections.js
