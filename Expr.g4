grammar Expr;

prog: expr EOF;

expr: create_stmt
    | insert_stmt
    | select_stmt
    ;

create_stmt : 'CREATE' 'table' ID '(' colum_index ',' row_index ')' ;

select_stmt : 'SELECT' colum_index ',' row_index 'FROM' ID ;

insert_stmt : 'INSERT' 'INTO' ID '(' colum_index ',' row_index ',' colum_var ')' ;

colum_var   : STRING ;

colum_index : COL ':' COL
            | COL
            ;

row_index   : ROW ':' ROW
            | ROW
            ;

ROW     : [1-9]+ ;
COL     : [A-Z]+ ;
ID      : [a-z][a-z0-9]+ ;
STRING  : ["][A-Za-z0-9]+["];
WS      : [ \t\r\n] -> channel(HIDDEN) ;
NEWLINE : [\r\n]+ ;
