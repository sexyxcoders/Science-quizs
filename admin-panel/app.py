# admin-panel/app.py
from flask import Flask, render_template, redirect, url_for, request, session
from modules.auth import login_required, authenticate
from modules.questions import get_questions, add_question, edit_question, delete_question
from modules.users import get_all_users
from modules.broadcast import send_broadcast

import os

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET", "supersecretkey")

# Login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if authenticate(username, password):
            session["admin"] = username
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

# Dashboard
@app.route("/dashboard")
@login_required
def dashboard():
    users = get_all_users()
    questions = get_questions()
    return render_template("dashboard.html", users=users, questions=questions)

# Questions management
@app.route("/questions")
@login_required
def questions():
    questions = get_questions()
    return render_template("questions.html", questions=questions)

@app.route("/questions/add", methods=["GET", "POST"])
@login_required
def add_q():
    if request.method == "POST":
        question = request.form["question"]
        options = request.form.getlist("options")
        answer = request.form["answer"]
        category = request.form["category"]
        add_question(question, options, answer, category)
        return redirect(url_for("questions"))
    return render_template("add_question.html")

@app.route("/questions/edit/<id>", methods=["GET", "POST"])
@login_required
def edit_q(id):
    if request.method == "POST":
        question = request.form["question"]
        options = request.form.getlist("options")
        answer = request.form["answer"]
        category = request.form["category"]
        edit_question(id, question, options, answer, category)
        return redirect(url_for("questions"))
    q = get_questions(id)
    return render_template("edit_question.html", question=q)

@app.route("/questions/delete/<id>")
@login_required
def delete_q(id):
    delete_question(id)
    return redirect(url_for("questions"))

# Broadcast message
@app.route("/broadcast", methods=["GET", "POST"])
@login_required
def broadcast():
    if request.method == "POST":
        message = request.form["message"]
        send_broadcast(message)
        return render_template("broadcast.html", success="Message sent successfully")
    return render_template("broadcast.html")

# Logout
@app.route("/logout")
@login_required
def logout():
    session.pop("admin", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=True)
