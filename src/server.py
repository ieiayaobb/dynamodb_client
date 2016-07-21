import threading
import logging

from flask import Flask, url_for, redirect, session
from flask import render_template
from flask import request

from dynamodb_handler import DynamodbHandler
from src.config.Constant import *


app = Flask(__name__)
app.secret_key = "hackthon"

logger = logging.getLogger("")

dynamodb_handler_dic = {}

@app.route("/connect", methods=['GET'])
def get_connect():
    return render_template('connect.html')


@app.route("/connect", methods=['POST'])
def post_connect():
    endpoint = request.form['endpoint']
    access_key = request.form['access_key']
    access_secret = request.form['access_secret']
    logger.info("endpoint:%s" % (endpoint))
    logger.info("access_key:%s" % (access_key))
    logger.info("access_secret:%s" % (access_secret))

    if not endpoint in dynamodb_handler_dic:
        dynamodb_handler_dic[endpoint] = DynamodbHandler(endpoint_url=endpoint, aws_access_key_id=access_key,
                                           aws_secret_access_key=access_secret, region_name='')

    session['endpoint'] = endpoint

    return redirect(url_for('table_view'))


@app.route("/")
def index():
    return redirect(url_for('get_connect'))

@app.route("/table/", methods=['POST', 'GET'])
@app.route("/table/<table_name>", methods=['POST', 'GET'])
def table_view(table_name=None):
    dynamodb_handler = dynamodb_handler_dic[session['endpoint']]

    tables = dynamodb_handler.list_tables()

    if not table_name:
        table_name = tables[0]
    last_evaluated_key = None

    if request.method == "GET":
        last_evaluated_key =  request.form.get('last_evaluated_key', None)

    current_table, table_items = dynamodb_handler.get_table(table_name, last_evaluated_key)

    return render_template('table_detail.html', tables=tables, current_table=current_table, table_items=table_items)


def init_logger():
    """
    initialize logger
    :return:
    """
    logger.setLevel(logging.INFO)

    # create a file handler
    log_path = LOG_PATH
    # handler = logging.FileHandler(log_path)
    # handler.setLevel(logging.INFO)

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)

    # create a logging format

    formatter = logging.Formatter('%(asctime)s - %(filename)s:%(lineno)s - %(levelname)s - %(message)s')
    # handler.setFormatter(formatter)
    console.setFormatter(formatter)

    # add the handlers to the logger

    # logger.addHandler(handler)
    logger.addHandler(console)
    logger.info("Logger initialization done, current log path is %s" % (log_path))

if __name__ == "__main__":
    init_logger()
    app.run(debug=True)

