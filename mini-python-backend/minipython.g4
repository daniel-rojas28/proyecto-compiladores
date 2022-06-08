grammar minipython;

tokens { INDENT, DEDENT }

@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
from gen.minipythonParser import minipythonParser
}
@lexer::members {
class MyCoolDenter(DenterHelper):
    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
        self.lexer: miniPythonLexer = lexer

    def pull_token(self):
        return super(minipythonLexer, self.lexer).nextToken()

denter = None

def nextToken(self):
    if not self.denter:
        self.denter = self.MyCoolDenter(self, self.NEWLINE , minipythonParser.INDENT, minipythonParser.DEDENT, False)
    return self.denter.next_token()
}

program : statements EOF                                                            #astProgram;
statements : statement+                                                             #astStatementDef;
statement : defStatement | ifStatement | returnStatement | printStatement | whileStatement | forStatement | assignStatement | functionCallStatement | expressionStatement ;
defStatement : DEF IDENTIFIER BLEFT argList? BRIGHT COLON sequence                  #astDefStatment;
argList : IDENTIFIER ( COMMA IDENTIFIER)*                                           #astArgList;
whileStatement : WHILE expression COLON sequence                                    #astWhileStatment;
forStatement : FOR expression IN expressionList COLON sequence                      #astForStatement;
ifStatement : IF expression COLON sequence (ELSE COLON sequence)?                   #astIfStatment;
returnStatement : RETURN expression NEWLINE                                         #astReturnStatement;
printStatement : PRINT expression NEWLINE                                           #astPrintStatement;
assignStatement : IDENTIFIER ASSIGN expression NEWLINE                              #astAssignStatment;
functionCallStatement : IDENTIFIER BLEFT expressionList BRIGHT NEWLINE              #astFunctionCallStatement;
expressionStatement : expressionList NEWLINE                                        #astExpressionStatement;
sequence : INDENT moreStatements DEDENT                                             #astSequence;
moreStatements : statement+                                                         #astMoreStatements;
expression : additionExpression ((LESS|HIGHER| LESSOREQUAL| HIGHEROREQUAL|EQUAL) additionExpression)* #astExpression;
additionExpression : multiplicationExpression ((SUM|SUB) multiplicationExpression)* #astAdditionExpression;
multiplicationExpression : elementExpression ((MUL|DIV) elementExpression)*         #astMultiplicationExpression;
elementExpression : primitiveExpression (SQLEFT expression SQRIGHT)*                #astElementExpression;
expressionList : (expression (COMMA expression)* | )                                #astExpressionList;
primitiveExpression : '-'? NUM                                                      #astNumPEAST
            | STRING                                                                #astStringPEAST
            | designator                                                            #astDesignatorPEAST
            | BLEFT expression BRIGHT                                               #astBlockPEAST
            | SQLEFT expressionList SQRIGHT                                         #astListPEAST
            | LEN BLEFT expression BRIGHT                                           #astLenPEAST;
designator : IDENTIFIER (BLEFT expressionList BRIGHT)?                              #astDesignatorAST;

DEF     : 'def';
IF      : 'if';
ELSE    : 'else';
WHILE   : 'while';
FOR     : 'for';
IN      : 'in';
RETURN  : 'return';
PRINT   : 'print';
LEN     : 'len';

ASSIGN  : '=';
EQUAL   : '==';
BLEFT   : '(';
BRIGHT  : ')';
SQLEFT  : '[';
SQRIGHT : ']';
COMMA   : ',';
COLON   : ':';
SUM         : '+';
MUL         : '*';
SUB         : '-';
DIV         : '/';
HIGHER      : '>';
LESS        : '<';
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