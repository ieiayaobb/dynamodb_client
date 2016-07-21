# -*- coding: utf-8 -*-

"""

"""
import logging
import sys
import json

from antlr4 import *
from antlr4.InputStream import InputStream

from src.parser.base.MySQLParserVisitor import MySQLParserVisitor
from src.parser.base.MySQLLexer import MySQLLexer
from src.parser.base.MySQLParser import MySQLParser
from src.config.Constant import *

from src.dynamodb_handler import DynamodbHandler
from src.exception.ParseException import *


class Parser(MySQLParserVisitor):
    @classmethod
    def init(cls, dynamodb):
        cls.dynamodb = dynamodb

    @classmethod
    def parse(cls, statment):
        stream = InputStream(statment)
        lexer = MySQLLexer(stream);
        stream = CommonTokenStream(lexer)
        parser = MySQLParser(stream)
        tree = parser.stat()
        visitor = Visitor(cls.dynamodb)
        if isinstance(visitor, ParseTreeVisitor):
            parsed_stat = visitor.visit(tree)
        return parsed_stat


class Visitor(MySQLParserVisitor):
    def __init__(self, dynamodb):
        self.dynamodb = dynamodb

    def visitSelect_clause(self, ctx):
        if isinstance(ctx, MySQLParser.Select_clauseContext):
            # handle table name
            table_name = ctx.table_name().getText()
            columns = []
            key = {}
            limit = TABLE_SCAN_LIMIT
            table_exist = self.dynamodb.desc_table(table_name)
            if table_exist:
                # handle columns
                column_clause = ctx.column_list_clause()
                if isinstance(column_clause, MySQLParser.Column_list_clauseContext):
                    if column_clause.single_column():
                        columns.append(column_clause.single_column().getText())
                    elif column_clause.multi_column():
                        columns = str(column_clause.multi_column().getText()).split(",")
                    elif column_clause.all_column():
                        pass
                    else:
                        raise ParseException("Illegal column : %s" % column_clause.getText())
                        # handle where clause
                    where_clause = ctx.where_clause();  # where id=3 and user=lyc
                    if where_clause:
                        if isinstance(where_clause, MySQLParser.Where_clauseContext):
                            if where_clause.hash_expression():
                                hash_expression = where_clause.hash_expression()
                                if isinstance(hash_expression, MySQLParser.Hash_expressionContext):
                                    key[hash_expression.hash_key().getText()] = hash_expression.hash_value().getText()
                            elif where_clause.hash_range_expression():
                                hash_range_expression = where_clause.hash_range_expression();
                                if isinstance(hash_range_expression, MySQLParser.Hash_range_expressionContext):
                                    key[
                                        hash_range_expression.hash_key().getText()] = hash_range_expression.hash_value().getText()
                                    key[
                                        hash_range_expression.range_key().getText()] = hash_range_expression.range_value().getText()
                            else:
                                raise ParseException("Illegal where clause : %s" % where_clause.getText())
                    limit_clause = ctx.limit_clause();
                    if limit_clause:
                        if isinstance(limit_clause, MySQLParser.Limit_clauseContext):
                            if limit_clause.limit_value():
                                limit = int(limit_clause.limit_value().getText())

            else:
                raise ParseException("table %s not exist" % table_name)
            # get items
            result = None
            if where_clause:
                result = self.dynamodb.get_item(table_name, key, columns)
            else:
                if columns:
                    result = self.dynamodb.scan(table_name, AttributesToGet=columns, Limit=limit)
                else:
                    result = self.dynamodb.scan(table_name,Limit=limit)

        return result

    def visitDesc_clause(self, ctx):
        if isinstance(ctx, MySQLParser.Desc_clauseContext):
            table_name = ctx.table_name().getText()
            if table_name:
                result = self.dynamodb.desc_table(table_name)
        return result


if __name__ == "__main__":
    # print(Parser.parse("select message from matrix_result where id=0m3vfiesDmYMsvx34CcH55jgKdPipyOn"))
    Parser.init(AWS_ACCESS_KEY, AWS_ACCESS_SECRET, AWS_REGION, DYNAMODB_ENDPOINT)
    print(
        Parser.parse("select * from patent"))
    print(
        Parser.parse("desc matrix_result"))
