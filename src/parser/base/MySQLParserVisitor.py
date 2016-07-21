# Generated from C:/pyprojects/hackathon/src/parser\MySQLParser.g4 by ANTLR 4.5.3
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by MySQLParser.

class MySQLParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MySQLParser#stat.
    def visitStat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#schema_name.
    def visitSchema_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#desc_clause.
    def visitDesc_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#select_clause.
    def visitSelect_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#insert_clause.
    def visitInsert_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#insert_expression.
    def visitInsert_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#limit_clause.
    def visitLimit_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#table_name.
    def visitTable_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#column_name.
    def visitColumn_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#column_name_alias.
    def visitColumn_name_alias(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#column_list_clause.
    def visitColumn_list_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#single_column.
    def visitSingle_column(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#multi_column.
    def visitMulti_column(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#all_column.
    def visitAll_column(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#where_clause.
    def visitWhere_clause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#hash_expression.
    def visitHash_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#hash_range_expression.
    def visitHash_range_expression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#hash_key.
    def visitHash_key(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#range_key.
    def visitRange_key(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#hash_value.
    def visitHash_value(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#range_value.
    def visitRange_value(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#insert_value.
    def visitInsert_value(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#limit_value.
    def visitLimit_value(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#relational_op.
    def visitRelational_op(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#eq_op.
    def visitEq_op(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#expr_op.
    def visitExpr_op(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#between_op.
    def visitBetween_op(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySQLParser#is_or_is_not.
    def visitIs_or_is_not(self, ctx):
        return self.visitChildren(ctx)


