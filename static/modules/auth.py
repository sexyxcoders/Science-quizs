# admin-panel/modules/auth.py
from functools import wraps
from flask import session, redirect, url_for, request, flash
import os

# Load admin credentials from environment variables
ADMIN_USER = os.getenv("ADMIN_USER", "admin")
ADMIN_PASS = os.getenv("ADMIN_PASS", "password")

def authenticate(username, password):
    """
    Check if provided username and password match the admin credentials.
    """
    return username == ADMIN_USER and password == ADMIN_PASS

def login_required(f):
    """
    Decorator to protect routes that require admin login.
    Redirects to login page if session not authenticated.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "admin" not in session:
            flash("Please login to access this page.", "warning")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function

def login_admin(username, password):
    """
    Log the admin in if credentials are correct.
    Returns True if successful, False otherwise.
    """
    if authenticate(username, password):
        session["admin"] = username
        return True
    return False

def logout_admin():
    """
    Log the admin out by clearing the session.
    """
    session.pop("admin", None)
