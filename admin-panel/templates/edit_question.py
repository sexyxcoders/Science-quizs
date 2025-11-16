<!-- admin-panel/templates/edit_question.html -->
{% extends "base.html" %}

{% block title %}Edit Question{% endblock %}

{% block content %}
<h2>Edit Question</h2>

<form method="POST" action="{{ url_for('edit_q', id=question['_id']) }}">
    <div class="form-group">
        <label for="question">Question:</label>
        <input type="text" name="question" id="question" class="form-control" value="{{ question['question'] }}" required>
    </div>

    <div class="form-group">
        <label>Options:</label>
        {% for opt in question['options'] %}
        <input type="text" name="options" class="form-control mb-1" value="{{ opt }}" required>
        {% endfor %}
    </div>

    <div class="form-group">
        <label for="answer">Correct Answer:</label>
        <input type="text" name="answer" id="answer" class="form-control" value="{{ question['answer'] }}" required>
    </div>

    <div class="form-group">
        <label for="category">Category:</label>
        <input type="text" name="category" id="category" class="form-control" value="{{ question.get('category','') }}">
    </div>

    <button type="submit" class="btn btn-primary mt-2">Update Question</button>
</form>
{% endblock %}