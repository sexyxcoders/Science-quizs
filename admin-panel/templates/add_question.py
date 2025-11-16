<!-- admin-panel/templates/add_question.html -->
{% extends "base.html" %}

{% block title %}Add Question{% endblock %}

{% block content %}
<h2>Add New Question</h2>

<form method="POST" action="{{ url_for('add_q') }}">
    <div class="form-group">
        <label for="question">Question:</label>
        <input type="text" name="question" id="question" class="form-control" required>
    </div>

    <div class="form-group">
        <label>Options:</label>
        <input type="text" name="options" class="form-control mb-1" placeholder="Option 1" required>
        <input type="text" name="options" class="form-control mb-1" placeholder="Option 2" required>
        <input type="text" name="options" class="form-control mb-1" placeholder="Option 3" required>
        <input type="text" name="options" class="form-control mb-1" placeholder="Option 4" required>
    </div>

    <div class="form-group">
        <label for="answer">Correct Answer:</label>
        <input type="text" name="answer" id="answer" class="form-control" required>
    </div>

    <div class="form-group">
        <label for="category">Category:</label>
        <input type="text" name="category" id="category" class="form-control" placeholder="Optional">
    </div>

    <button type="submit" class="btn btn-primary mt-2">Add Question</button>
</form>
{% endblock %}
