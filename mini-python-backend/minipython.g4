grammar minipython;

tokens { INDENT, DEDENT }

@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
from minipythonParser import minipythonParser
}
@lexer::members {
class MiniPyDenter(DenterHelper):
    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
        self.lexer: minipythonLexer = lexer

    def pull_token(self):
        return super(minipythonLexer, self.lexer).nextToken()

denter = None

def nextToken(self):
    if not self.denter:
        self.denter = self.MiniPyDenter(self, self.NEWLINE, minipythonParser.INDENT,minipythonParser.DEDENT, False)
    return self.denter.next_token()

}

program : statements EOF                                                            #astProgram;
statements : statement+                                                             #astStatementDef;
statement : defStatement | ifStatement | returnStatement | printStatement | whileStatement | forStatement | assignStatement | functionCallStatement | expressionStatement ;
defStatement : DEF IDENTIFIER LEFTPARENT argList? RIGTHPARENT COLON sequence        #astDefStatment;
argList : IDENTIFIER ( COMMA IDENTIFIER)*                                           #astArgList;
ifStatement : IF expression COLON sequence (ELSE COLON sequence)?                   #astIfStatment;
whileStatement : WHILE expression COLON sequence                                    #astWhileStatment;
forStatement : FOR expression IN expressionList COLON sequence                      #astForStatement;
returnStatement : RETURN expression NEWLINE                                         #astReturnStatement;
printStatement : PRINT expression NEWLINE                                           #astPrintStatement;
assignStatement : IDENTIFIER EQUAL expression NEWLINE                               #astAssignStatment;
functionCallStatement : IDENTIFIER LEFTPARENT expressionList RIGTHPARENT NEWLINE    #astFunctionCallStatement;
expressionStatement : expressionList NEWLINE                                        #astExpressionStatement;
sequence : INDENT moreStatements DEDENT                                             #astSequence;
moreStatements : statement+                                                         #astMoreStatements;
expression : additionExpression ((LESS|HIGHER| LESSOREQUAL| HIGHEROREQUAL|COMPARISON) additionExpression)* #astExpression;
additionExpression : multiplicationExpression ((SUM|SUBTRACTION) multiplicationExpression)* #astAdditionExpression;
multiplicationExpression : elementExpression ((MULTIPLICATION|DIVISION) elementExpression)* #astMultiplicationExpression;
elementExpression : primitiveExpression (LEFTKICK expression RIGTHKICK)*            #astElementExpression;
expressionList : (expression (COMMA expression)* | )                                #astExpressionList;
primitiveExpression : '-'? NUM                                                      #astNumPEAST
            | STRING                                                                #astStringPEAST
            | designator                                                            #astDesignatorPEAST
            | LEFTPARENT expression RIGTHPARENT                                     #astBlockPEAST
            | LEFTKICK expressionList RIGTHKICK                                     #astListPEAST
            | LEN LEFTPARENT expression RIGTHPARENT                                 #astLenPEAST;
designator : IDENTIFIER (LEFTPARENT expressionList RIGTHPARENT)?                    #astDesignatorAST;


DEF     : 'def';
LEN     : 'len';
IF      : 'if';
FOR     : 'for';
IN      : 'in';
ELSE    : 'else';
WHILE   : 'while';
RETURN  : 'return';
PRINT   : 'print';
EQUAL   : '=';
COMMA          : ',';
COMPARISON     : '==';
LEFTPARENT     : '(';
RIGTHPARENT    : ')';
SUM            : '+';
MULTIPLICATION    : '*';
DIVISION          : '/';
HIGHER            : '>';
LESS              : '<';
COLON             : ':';
SUBTRACTION       : '-';
LEFTKICK          : '[';
RIGTHKICK         : ']';
LESSOREQUAL       : '<=';
HIGHEROREQUAL     : '>=';

fragment L : [a-zA-Z_];
fragment N : [0-9] ;

CHAR         : '\'' (L|[0-9]|' ')? '\'';
NUM          :'0' | ([1-9] N* ) | ([0-9]+)?(('.'[0-9]+));
IDENTIFIER : L(L|N)*;

STRING : '"' ('""'|~'"')* '"' ;

NEWLINE : ('\r'? '\n' (' ' | '\t')* );

WS : [ +\r\n\t] -> skip ;
BLOK_COMMENT : '"""' .+? ' """ ' ->skip;
COMMENT : '#' ~[\r\n\f]+ ->skip;