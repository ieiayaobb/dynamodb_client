import threading

from flask import Flask
from flask import render_template

from src.dynamodb_handler import DynamodbHandler

app = Flask(__name__)

dynamodb_handler = DynamodbHandler(endpoint_url = 'http://192.168.3.66:80', aws_access_key_id = '', aws_secret_access_key = '', region_name = '')

@app.route("/dashboard")
def dashboard():
    tables = dynamodb_handler.list_tables()
    return render_template('dashboard.html', tables=tables)

@app.route("/connect")
def connect():
    return render_template('connect.html')

if __name__ == "__main__":
    app.run()

