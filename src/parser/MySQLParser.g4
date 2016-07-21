parser grammar MySQLParser;

options {
	tokenVocab=MySQLLexer;
	language=Python2;
}



stat:select_clause|desc_clause;

schema_name:
    ID
    ;

desc_clause:
        DESC table_name;

select_clause:
            SELECT column_list_clause FROM table_name (where_clause)? (limit_clause)?
            ;

limit_clause:
            LIMIT limit_value
            ;

table_name:
	ID
	;

column_name:
    ID;

column_name_alias:
	ID
	;

column_list_clause:
        single_column|multi_column|all_column
        ;

single_column:
        ID
        ;

multi_column:
        ID (COMMA ID)+
        ;

all_column:
        ASTERISK
        ;

where_clause:
		hash_expression|hash_range_expression
		;

hash_expression:
        WHERE hash_key relational_op hash_value
        ;

hash_range_expression:
        WHERE hash_key relational_op hash_value expr_op range_key relational_op range_value
        ;

hash_key:
       ID
       ;

range_key:
        ID
        ;

hash_value:
        ID
        ;

range_value:
        ID
        ;

insert_value:
        ID
        ;

limit_value:
        INT
        ;

relational_op:
		EQ | LTH | GTH | NOT_EQ | LET | GET  ;

expr_op:
		AND | XOR | OR | NOT;

between_op:
		BETWEEN
	;

is_or_is_not:
		IS | IS NOT
	;

