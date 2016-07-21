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

dynamodb = DynamodbHandler(DYNAMODB_ENDPOINT, AWS_ACCESS_KEY, AWS_ACCESS_SECRET, AWS_REGION)


class Parser(MySQLParserVisitor):
    @classmethod
    def parse(cls, statment):
        stream = InputStream(statment)
        lexer = MySQLLexer(stream);
        stream = CommonTokenStream(lexer)
        parser = MySQLParser(stream)
        tree = parser.stat()
        visitor = Visitor()
        if isinstance(visitor, ParseTreeVisitor):
            parsed_stat = visitor.visit(tree)
        return parsed_stat


class Visitor(MySQLParserVisitor):
    def visitSelect_clause(self, ctx):
        if isinstance(ctx, MySQLParser.Select_clauseContext):
            # handle table name
            table_name = ctx.table_name().getText()
            columns = []
            table_exist = dynamodb.desc_table(table_name)
            if table_exist:
                # handle columns
                column_clause = ctx.column_list_clause()
                if isinstance(column_clause, MySQLParser.Column_list_clauseContext):
                    if column_clause.single_column():
                        pass
                    elif column_clause.multi_column():
                        pass
                    elif column_clause.all_column():
                        pass
                    else:
                        raise ParseException("Illegal column : %s" % column_clause.getText())
            else:
                raise ParseException("table %s not exist" % table_name)
            # handle columns
            print(ctx.table_name().getText())
            print(ctx.column_list_clause().getText())
        return self.visitChildren(ctx)

    def visitDesc_clause(self, ctx):
        if isinstance(ctx, MySQLParser.Desc_clauseContext):
            table_name = ctx.table_name().getText()
            if table_name:
                result = dynamodb.desc_table(table_name)
        return result


if __name__ == "__main__":
    print(Parser.parse("desc matrix_resu"))
