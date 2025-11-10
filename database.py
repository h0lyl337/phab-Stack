import sqlite3
from datetime import datetime, timedelta

def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT,
            email TEXT,
            subscription INTERGER,
            credits INTERGER,
            admin INTERGER
        )
    """)

    conn.commit()
    conn.close()

def create_user(username, password, email):
    username = str(username).lower()

    conn = sqlite3.connect("users.db")
    
    c = conn.cursor()

    try:
        c.execute("INSERT INTO users(username, password, email, subscription, credits, admin ) VALUES (?, ?, ?, ?, ?, ?)",
                  (username, password, email, 0, 100, 0))

        conn.commit()

    except Exception as e:
        print(e)
        pass

    conn.close()

def check_if_user_exists(username):
    username = str(username).lower()
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    
    try:
        c.execute("SELECT username FROM users WHERE username = '{0}' ".format(username))
        conn.commit()

        answer = c.fetchall()

        if answer:
            return True
        
    except Exception as e:
        print(e)
        pass

    conn.close()

def check_if_email_exists(email):
    username = str(email).lower()
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    try:
        c.execute("SELECT email FROM users WHERE email = '{0}' ".format(email))
        conn.commit()

        answer = c.fetchall()

        if answer:
            return True
        
    except Exception as e:
        print(e)
        pass

    conn.close()

def login(username, password):
    username = str(username).lower()
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    try:
        c.execute("SELECT username, password FROM users WHERE username = '{0}' AND password = '{1}'".format(username, password))
        conn.commit()

        answer = c.fetchone()

        db_username = answer[0]

        db_password = answer[1]

        if username == db_username and password == db_password:
            return True
    except Exception as e:
        print(e)
        pass
    conn.close()

def get_email(username):
    username = str(username).lower()
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    try:
        c.execute("SELECT email FROM users WHERE username = '{0}' ".format(username))
        conn.commit()

        answer = c.fetchone()[0]

        return answer
    except Exception as e:
        print(e)
        pass
    conn.close()

def get_history(username):
    username = str(username).lower()

    conn = sqlite3.connect("users.db")

    c = conn.cursor()

    c.execute("SELECT * FROM history WHERE username = '{0}' ".format(username))

    history = c.fetchall()

    conn.close()

    history.reverse()
    return history

def get_historys():
    

    conn = sqlite3.connect("users.db")

    c = conn.cursor()

    c.execute("SELECT username FROM users")

    history = c.fetchall()

    conn.close()

    for h in history:
        print(h)


init_db()
get_historys()

