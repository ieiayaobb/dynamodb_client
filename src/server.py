import ast
import collections
from flask import Flask, url_for, redirect, session
from flask import render_template
from flask import request

from src.config import Constant
from src.parser.Parser import *

# sio = socketio.Server(logger=True)
app = Flask(__name__)
app.secret_key = "hackthon"

# app.wsgi_app = socketio.Middleware(sio, app.wsgi_app)

logger = logging.getLogger("")

dynamodb_handler_dic = {}

@app.route("/login", methods=['GET'])
def get_connect():
    return render_template('connect.html')


@app.route("/login", methods=['POST'])
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
    if not 'messages' in session:
        session['messages'] = ['connect...']

    return redirect(url_for('table_view'))


@app.route("/")
def index():
    return redirect(url_for('get_connect'))


@app.route("/update/", methods=['POST'])
def update():
    endpoint = session['endpoint']
    if endpoint in dynamodb_handler_dic:
        dynamodb_handler = dynamodb_handler_dic[endpoint]
    else:
        return redirect(url_for('get_connect'))

    table_name = request.form.get('table_name', None)
    hash_key_field = request.form.get('hash_key_field', None)
    hash_key = request.form.get('hash_key', None)

    range_key_field = request.form.get('range_key_field', None)
    range_key = request.form.get('range_key', None)

    update_field = request.form.get('update_field', None)
    update_value = request.form.get('update_value', None)

    dynamodb_handler.get_dynamodb().Table(table_name).update_item(
        Key={
            hash_key_field: hash_key
        },
        AttributeUpdates={
            update_field: {
                'Value': update_value,
                'Action': 'PUT'
            }
        }
    )
    return 'success'

@app.route("/table/", methods=['POST', 'GET'])
@app.route("/table/<table_name>", methods=['POST', 'GET'])
def table_view(table_name=None):
    endpoint = session['endpoint']
    if endpoint in dynamodb_handler_dic:
        dynamodb_handler = dynamodb_handler_dic[endpoint]
        Parser.init(dynamodb_handler)
    else:
        return redirect(url_for('get_connect'))

    tables = dynamodb_handler.list_tables()

    if not table_name:
        table_name = tables[0]

    # get parameters from page
    pagination_type = request.form.get("pagination", None)
    current_page_size = request.form.get("current_page_size", 0, type=int)

    last_evaluated_key = request.form.get('last_evaluated_key', None)
    if last_evaluated_key:
        last_evaluated_key = ast.literal_eval(last_evaluated_key)

    page_items_history = request.form.get("page_items_history", [])
    if page_items_history:
        page_items_history = ast.literal_eval(page_items_history)

    current_table = dynamodb_handler.get_table(table_name)

    table_headers = collections.OrderedDict()
    for attribute in current_table['AttributeDefinitions']:
        table_headers[attribute['AttributeName']] = attribute['AttributeType']

    page_items = None

    count = dynamodb_handler.count(table_name)

    messages = session['messages']
    if request.method == 'POST':
        hash_key_field = request.form.get('hash_key_field', None)
        logger.info("hash_key_field:%s" % (hash_key_field))

        if hash_key_field:
            index_name = request.form.get('index_name', None)
            logger.info("index_name:%s" % (index_name))

            range_key_field = request.form.get('range_key_field', None)
            logger.info("range_key_field:%s" % (range_key_field))

            hash_key = request.form.get('hash_key', None)
            logger.info("hash_key:%s" % (hash_key))

            range_key = request.form.get('range_key', None)
            logger.info("range_key:%s" % (range_key))

            dynamodb_client = dynamodb_handler.get_dynamodb_client()

            if not range_key:
                if index_name:
                    table_items = dynamodb_client.query(
                        TableName=table_name,
                        IndexName=index_name,
                        KeyConditions={
                            hash_key_field: {
                                'AttributeValueList': [{
                                    'S': hash_key
                                }],
                                'ComparisonOperator': 'EQ'
                            }
                        }
                    )
                else:
                    table_items = dynamodb_client.query(
                        TableName=table_name,
                        KeyConditions={
                            hash_key_field: {
                                'AttributeValueList': [{
                                    'S': hash_key
                                }],
                                'ComparisonOperator': 'EQ'
                            }
                        }
                    )
            else:
                if index_name:
                    table_items = dynamodb_client.query(
                        TableName=table_name,
                        IndexName=index_name,
                        KeyConditions={
                            hash_key_field: {
                                'AttributeValueList': [{
                                    'S': hash_key
                                }],
                                'ComparisonOperator': 'EQ'
                            },
                            range_key_field: {
                                'AttributeValueList': [{
                                    'S': range_key
                                }],
                                'ComparisonOperator': 'EQ'
                            }
                        }
                    )
                else:
                    table_items = dynamodb_client.query(
                        TableName=table_name,
                        KeyConditions={
                            hash_key_field: {
                                'AttributeValueList': [{
                                    'S': hash_key
                                }],
                                'ComparisonOperator': 'EQ'
                            },
                            range_key_field: {
                                'AttributeValueList': [{
                                    'S': range_key
                                }],
                                'ComparisonOperator': 'EQ'
                            }
                        }
                    )

            for page_item in table_items['Items']:
                keys = page_item.keys()
                for key in keys:
                    if not table_headers.has_key(key):
                        table_headers[key] = page_item[key].items()[0][0]

        else:
            terminal_text = request.form.get('terminal_text', None)
            logger.info("terminal_text:%s" % (terminal_text))
            table_items = Parser.parse(terminal_text)
            if table_items:
                messages.append(terminal_text)
                session['messages'] = messages

        if table_items and 'Items' in table_items:
            return render_template('table_detail.html',
                                   tables=tables,
                                   current_table=current_table,
                                   query_operation=True,
                                   table_items=table_items['Items'],
                                   current_page_size=current_page_size,
                                   page_item_limit=Constant.TABLE_SCAN_LIMIT,
                                   last_evaluated_key=last_evaluated_key,
                                   page_items_history=page_items_history,
                                   count=count,
                                   table_headers=table_headers,
                                   table_name=table_name,
                                   messages=messages)



    if pagination_type == "previous":
        if current_page_size > 1:
            current_page_size -= 1
            page_items = page_items_history[current_page_size-1]
        else:
            page_items = page_items_history[0]
    elif pagination_type == "next" or not pagination_type:
        if current_page_size == len(page_items_history):
            current_page_size += 1
            page_items, last_evaluated_key = dynamodb_handler.paginate_scan(table_name, ExclusiveStartKey=last_evaluated_key)
            if page_items:
                page_items_history.append(page_items)
        else:
            current_page_size += 1
            page_items = page_items_history[current_page_size-1]

    for page_item in page_items:
        keys = page_item.keys()
        for key in keys:
            if not table_headers.has_key(key):
                table_headers[key] = page_item[key].items()[0][0]

    return render_template('table_detail.html',
                           tables=tables,
                           current_table=current_table,
                           query_operation=False,
                           table_items=page_items,
                           current_page_size=current_page_size,
                           page_item_limit=Constant.TABLE_SCAN_LIMIT,
                           last_evaluated_key=last_evaluated_key,
                           page_items_history=page_items_history,
                           count=count,
                           table_headers=table_headers,
                           table_name=table_name,
                           messages=messages)


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

