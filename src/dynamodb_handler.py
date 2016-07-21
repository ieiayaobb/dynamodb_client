import boto3 as boto3


class DynamodbHandler:
    def __init__(self, endpoint_url, aws_access_key_id, aws_secret_access_key, region_name):
        self._scan_limit = 10

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

    def get_table(self, table_name, last_evaluated_key=None):
        try:
            table = self.dynamodb_client.describe_table(TableName=table_name)
            table_items = self.scan(table, last_evaluated_key)
            return table, table_items
        except Exception as e:
            print (e.message)

    def scan(self, table, last_evaluated_key):
        try:
            if last_evaluated_key != None:
                table_items = table.scan(Limit=self._scan_limit, ExclusiveStartKey=last_evaluated_key)
            else:
                table_items = table.scan(Limit=self._scan_limit)
            return table_items
        except Exception as e:
            print (e.message)
