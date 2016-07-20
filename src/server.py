import threading

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/connect")
def connect():
    return render_template('connect.html')

if __name__ == "__main__":
    app.run()

