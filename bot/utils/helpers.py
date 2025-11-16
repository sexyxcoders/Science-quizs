# bot/utils/helpers.py
import random

def shuffle_options(options):
    """
    Shuffle the order of options for a question.
    """
    random.shuffle(options)
    return options

def format_question(q):
    """
    Format a question dictionary to a string.
    """
    text = f"❓ {q['question']}\n"
    for idx, opt in enumerate(q['options'], start=1):
        text += f"{idx}. {opt}\n"
    return text
