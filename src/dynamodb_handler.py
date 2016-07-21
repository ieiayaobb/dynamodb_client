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

    def get_table(self, table_name):
        try:
            table = self.dynamodb_client.describe_table(TableName=table_name)
            return table['Table']
        except Exception as e:
            logging.error(e.message)

    def scan(self, table_name, page_size=None, next_token=None):
        paginator = self.dynamodb_client.get_paginator('scan')

        try:
            paginate_result = paginator.paginate(TableName=table_name, PaginationConfig={'MaxItems': self._scan_limit, 'PageSize': page_size, "NextToken": next_token })
            return paginate_result
        except Exception as e:
            logging.error(e.message)

    def desc_table(self, table_name):
        try:
            return self.dynamodb_client.describe_table(TableName=table_name)
        except Exception as e:
            logging.error(e.message)
