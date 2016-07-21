parser grammar MySQLParser;

options {
	tokenVocab=MySQLLexer;
	language=Python2;
}



stat:
		select_clause|desc_clause

	;

schema_name:
    ID
    ;

desc_clause:
        DESC table_name;

select_clause:
		SELECT
		column_list_clause
	    FROM table_name
		(where_clause)?
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



//table_references:
//        table_reference ( (COMMA table_reference) | join_clause )*
//;
//
//table_reference:
//	table_factor1 | table_atom
//;

//table_factor1:
//	table_factor2 (  (INNER | CROSS)? JOIN table_atom (join_condition)? )?
//;
//
//table_factor2:
//	table_factor3 (  STRAIGHT_JOIN table_atom (ON expression)?  )?
//;
//
//table_factor3:
//	table_factor4 (  (LEFT|RIGHT) (OUTER)? JOIN table_factor4 join_condition  )?
//;
//
//table_factor4:
//	table_atom (  NATURAL ( (LEFT|RIGHT) (OUTER)? )? JOIN table_atom )?
//;
//
//table_atom:
//	  ( table_name (partition_clause)? (table_alias)? (index_hint_list)? )
//	| ( subquery subquery_alias )
//	| ( LPAREN table_references RPAREN )
//	| ( OJ table_reference LEFT OUTER JOIN table_reference ON expression )
//;
//
//join_clause:
//        (  (INNER | CROSS)? JOIN table_atom (join_condition)? )
//    |
//        (  STRAIGHT_JOIN table_atom (ON expression)?  )
//    |
//        (  (LEFT|RIGHT) (OUTER)? JOIN table_factor4 join_condition  )
//    |
//        (  NATURAL ( (LEFT|RIGHT) (OUTER)? )? JOIN table_atom )
//    ;
//
//join_condition:
//	  (ON expression (expr_op expression)*) | (USING column_list)
//;
//
//index_hint_list:
//	index_hint (COMMA index_hint)*
//;
//
//index_options:
//	(INDEX | KEY) (FOR ((JOIN) | (ORDER BY) | (GROUP BY)))?
//;
//
//index_hint:
//	  USE    index_options LPAREN (index_list)? RPAREN
//	| IGNORE index_options LPAREN index_list RPAREN
//;
//
//index_list:
//	index_name (COMMA index_name)*
//;
//
//partition_clause:
//	PARTITION LPAREN partition_names RPAREN
//;
//
//partition_names:
//	partition_name (COMMA partition_name)* ;
//
//partition_name:
//    ID
//    ;
//
//subquery_alias:
//    ID
//    ;
//
//subquery:
//	LPAREN select_clause RPAREN
//;
