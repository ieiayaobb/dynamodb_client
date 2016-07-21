import boto3 as boto3
import logging

from src.config import Constant


class DynamodbHandler:
    def __init__(self, endpoint_url, aws_access_key_id, aws_secret_access_key, region_name):
        self._scan_limit = Constant.TABLE_SCAN_LIMIT

        self.dynamodb = boto3.resource('dynamodb',
                                       # endpoint_url='http://s-identity-qa-public-elb-1977034329.cn-north-1.elb.amazonaws.com.cn:8000'
                                       endpoint_url=endpoint_url,
                                       aws_access_key_id=aws_access_key_id,
                                       aws_secret_access_key=aws_secret_access_key,
                                       region_name=region_name)

        self.dynamodb_client = boto3.client('dynamodb',
                                            endpoint_url=endpoint_url,
                                            aws_access_key_id=aws_access_key_id,
                                            aws_secret_access_key=aws_secret_access_key,
                                            region_name=region_name)

        self.dynamodb.region_name = region_name

    def list_tables(self):
        return self.dynamodb_client.list_tables()['TableNames']

    def get_dynamodb_client(self):
        return self.dynamodb_client

    def get_table(self, table_name):
        try:
            table = self.dynamodb_client.describe_table(TableName=table_name)
            return table['Table']
        except Exception as e:
            logging.error(e.message)

    def paginate_scan(self, table_name, **kwargs):
        change_kwargs = kwargs.copy()
        for k, v in kwargs.items():
            if not v:
                change_kwargs.pop(k)

        try:
            table_items = self.dynamodb_client.scan(TableName=table_name, Limit=self._scan_limit, **change_kwargs)

            last_evaluated_key = table_items.get('LastEvaluatedKey', None)
            return table_items['Items'], last_evaluated_key
        except Exception as e:
            logging.error(e.message)

    def scan(self, table_name, **kwargs):
        change_kwargs = kwargs.copy()
        for k, v in kwargs.items():
            if not v:
                change_kwargs.pop(k)

        try:
            table_items = self.dynamodb_client.scan(TableName=table_name, **change_kwargs)
            return table_items
        except Exception as e:
            logging.error(e.message)

    def get_item(self, table_name, key, attributes_to_get):
        try:
            talbe = self.dynamodb.Table(table_name)
            if attributes_to_get:
                return talbe.get_item(TableName=table_name, Key=key, AttributesToGet=attributes_to_get)
            else:
                return talbe.get_item(TableName=table_name, Key=key)
        except Exception as e:
            logging.error(e.message)

    def put_item(self, table_name, item):
        try:
            table = self.dynamodb.Table(table_name)
            return table.put_item(Item=item)
        except Exception as e:
            logging.error(e.message)


    def desc_table(self, table_name):
        try:
            return self.dynamodb_client.describe_table(TableName=table_name)
        except Exception as e:
            logging.error(e.message)

    def count(self, table_name):
        target_table = self.dynamodb.Table(table_name)
        result = target_table.scan(Select='COUNT')
        lastEvaluatedKey = result.get("LastEvaluatedKey")
        count = result.get("Count")

        while (lastEvaluatedKey != None):
            result = target_table.scan(ExclusiveStartKey=lastEvaluatedKey, Select='COUNT')
            lastEvaluatedKey = result.get("LastEvaluatedKey")
            count = count + result.get("Count")

        return count
