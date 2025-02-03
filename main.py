import logging
from math import log
from flask import Flask, render_template, request

app = Flask(__name__)
log = app.logger
log.setLevel(logging.INFO)

users = {
    "user1": "password1",
    "user2": "password2"
}

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username in users and users.get(username) == password:
        log.info("Login successful!")
        
    else:
        log.warning("Invalid username or password")
        return "Invalid username or password"

if __name__ == "__main__":
    app.run(debug=True)