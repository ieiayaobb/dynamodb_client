import threading
import logging

import collections
from flask import Flask, url_for, redirect
from flask import render_template
from flask import request

from dynamodb_handler import DynamodbHandler
from src.config.Constant import *


app = Flask(__name__)
logger = logging.getLogger("")

dynamodb_handler = DynamodbHandler(endpoint_url = 'http://192.168.3.66:80', aws_access_key_id = '', aws_secret_access_key = '', region_name = '')

@app.route("/dashboard")
def dashboard():
    tables = dynamodb_handler.list_tables()
    return render_template('dashboard.html', tables=tables)


@app.route("/connect")
def connect():
    return render_template('connect.html')


@app.route("/")
def index():
    return redirect(url_for('connect'))

@app.route("/table/<table_name>", methods=['POST', 'GET'])
def table_view(table_name):
    tables = dynamodb_handler.list_tables()
    last_evaluated_key = None

    if request.method == "GET":
        last_evaluated_key =  request.form.get('last_evaluated_key', None)

    current_table, table_items = dynamodb_handler.get_table(table_name, last_evaluated_key)

    table_headers = collections.OrderedDict()

    for attribute in current_table['AttributeDefinitions']:
        table_headers[attribute['AttributeName']] = attribute['AttributeType']

    for table_item in table_items['Items']:
        keys = table_item.keys()
        for key in keys:
            if table_headers.has_key(key):
                table_headers[key] = table_item[key].items()[0][0]

    return render_template('table_detail.html', tables=tables, current_table=current_table, table_items=table_items['Items'], table_headers=table_headers)


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
    app.run()

