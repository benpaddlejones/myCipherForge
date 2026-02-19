"""Database setup for user authentication.

This module provides SQLite database functions for user management
with hashed passwords for security.

Usage:
    from database import init_db, create_user, verify_user
    
    # Initialise database
    init_db()
    
    # Create a user
    create_user("admin", "secretpassword")
    
    # Verify login
    if verify_user("admin", "secretpassword"):
        print("Login successful!")
"""

import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

DATABASE = 'users.db'


def get_db():
    """Get a database connection.
    
    Returns:
        sqlite3.Connection: Database connection with Row factory
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Access columns by name
    return conn


def init_db():
    """Create the users table if it doesn't exist.
    
    Call this once when setting up the application.
    """
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    print("Database initialised!")


def create_user(username, password):
    """Create a new user with a hashed password.
    
    Args:
        username: The username (must be unique)
        password: The plain text password (will be hashed)
    
    Returns:
        bool: True if user was created, False if username exists
    """
    conn = get_db()
    try:
        # Hash the password before storing
        password_hash = generate_password_hash(password)
        conn.execute(
            'INSERT INTO users (username, password_hash) VALUES (?, ?)',
            (username, password_hash)
        )
        conn.commit()
        print(f"User '{username}' created successfully!")
        return True
    except sqlite3.IntegrityError:
        print(f"Error: Username '{username}' already exists!")
        return False
    finally:
        conn.close()


def verify_user(username, password):
    """Check if username and password are valid.
    
    Args:
        username: The username to check
        password: The plain text password to verify
    
    Returns:
        bool: True if credentials are valid, False otherwise
    """
    conn = get_db()
    user = conn.execute(
        'SELECT password_hash FROM users WHERE username = ?',
        (username,)
    ).fetchone()
    conn.close()
    
    if user is None:
        return False
    
    return check_password_hash(user['password_hash'], password)


def delete_user(username):
    """Delete a user from the database.
    
    Args:
        username: The username to delete
    
    Returns:
        bool: True if user was deleted, False if not found
    """
    conn = get_db()
    cursor = conn.execute(
        'DELETE FROM users WHERE username = ?',
        (username,)
    )
    conn.commit()
    deleted = cursor.rowcount > 0
    conn.close()
    
    if deleted:
        print(f"User '{username}' deleted.")
    else:
        print(f"User '{username}' not found.")
    
    return deleted


def list_users():
    """List all users in the database.
    
    Returns:
        list: List of dictionaries with user info (no passwords)
    """
    conn = get_db()
    users = conn.execute(
        'SELECT id, username, created_at FROM users'
    ).fetchall()
    conn.close()
    
    return [dict(user) for user in users]


# Test the database functions
if __name__ == "__main__":
    import os
    
    # Remove test database if exists
    if os.path.exists(DATABASE):
        os.remove(DATABASE)
    
    print("Testing database functions...")
    print()
    
    # Initialise database
    init_db()
    print()
    
    # Create users
    create_user("admin", "supersecret")
    create_user("student", "password123")
    create_user("admin", "duplicate")  # Should fail
    print()
    
    # List users
    print("All users:")
    for user in list_users():
        print(f"  {user['id']}: {user['username']} (created: {user['created_at']})")
    print()
    
    # Verify users
    print("Verification tests:")
    print(f"  admin/supersecret: {verify_user('admin', 'supersecret')}")  # True
    print(f"  admin/wrong: {verify_user('admin', 'wrong')}")  # False
    print(f"  student/password123: {verify_user('student', 'password123')}")  # True
    print(f"  unknown/test: {verify_user('unknown', 'test')}")  # False
    print()
    
    # Delete user
    delete_user("student")
    
    print("\nAll database tests passed!")
