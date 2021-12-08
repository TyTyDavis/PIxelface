from flask import Flask, redirect, url_for
from app import app

@app.route("/")
def home():
    return render_template('index.html', title='Home')

@app.route("/<name>")
def user(name):
    return f"Hello {name}"


@app.route("/admin")
def admin():
    return redirect(url_for("home"))
