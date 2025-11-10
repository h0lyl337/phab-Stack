from flask import Flask, request, render_template, Response, session, redirect, send_file, make_response, send_from_directory, flash, jsonify
import os
import database
from datetime import datetime

app = Flask(__name__, static_folder=f"{os.getcwd()}/static", template_folder=f"{os.getcwd()}/templates")

app.secret_key = os.urandom(24).hex()

ip = '0.0.0.0'

port = '5000'

@app.route('/')
def mainn():
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    print(client_ip)

    return render_template("index.html")

### LOGIN ###

@app.route('/login', methods=["POST", "GET"])
def login():
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    print(client_ip)

    if request.method == "POST":

        username = request.form['username']

        password = request.form['password']

        if database.login(username, password) == True:

            print(True)

            session['username'] = username

            session['logged_in'] = True

            session['email'] = database.get_email(username)

            print(username + " " + "has logged in")

            return redirect("/")

    return render_template("login.html")

### REGISTER ###

@app.route('/register', methods=["POST", "GET"])
def register():
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    print(client_ip)

    if request.method == "POST":

        username = request.form['username'].lower()

        password = request.form['password']

        confirm_password = request.form['confirm-password']

        if password != confirm_password:

            flash("passwords do not match")

        email = request.form['email']

        if "@" not in email:
            flash("email has no @ symbol")

        print(database.check_if_user_exists(username))

        if database.check_if_user_exists(username) == None and database.check_if_email_exists(email) == None:

                database.create_user(username, password, email)

                session['username'] = username

                session['logged_in'] = True

                return redirect("/")

        else:
            flash('email or username already registered!')

    return render_template("register.html")

### LOG-OUT ###

@app.route('/logout', methods=["POST", "GET"])
def logout():
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    print(client_ip)

    session.pop('logged_in', None)

    session.pop('username', None)

    return render_template("login.html")

app.run(host=ip, port=port, threaded=True, debug=True)
