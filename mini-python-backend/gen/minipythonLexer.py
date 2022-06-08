# Generated from C:/Users/geral/Desktop/proyecto-compiladores/mini-python-backend\minipython.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from antlr_denter.DenterHelper import DenterHelper
from gen.minipythonParser import minipythonParser



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2#")
        buf.write("\u00f2\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\3\2\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20")
        buf.write("\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35\5\35\u009e\n")
        buf.write("\35\3\35\3\35\3\36\3\36\3\36\7\36\u00a5\n\36\f\36\16\36")
        buf.write("\u00a8\13\36\3\36\6\36\u00ab\n\36\r\36\16\36\u00ac\5\36")
        buf.write("\u00af\n\36\3\36\3\36\6\36\u00b3\n\36\r\36\16\36\u00b4")
        buf.write("\5\36\u00b7\n\36\3\37\3\37\3\37\7\37\u00bc\n\37\f\37\16")
        buf.write("\37\u00bf\13\37\3 \3 \3 \3 \7 \u00c5\n \f \16 \u00c8\13")
        buf.write(" \3 \3 \3!\5!\u00cd\n!\3!\3!\7!\u00d1\n!\f!\16!\u00d4")
        buf.write("\13!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\6#\u00df\n#\r#\16")
        buf.write("#\u00e0\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$\6$\u00ed\n$\r$\16")
        buf.write("$\u00ee\3$\3$\3\u00e0\2%\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\2\67\29\34;\35")
        buf.write("=\36?\37A C!E\"G#\3\2\n\5\2C\\aac|\3\2\62;\4\2\"\"\62")
        buf.write(";\3\2\63;\3\2$$\4\2\13\13\"\"\6\2\13\f\17\17\"\"--\4\2")
        buf.write("\f\f\16\17\2\u00ff\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\3I\3\2\2\2\5M\3\2\2")
        buf.write("\2\7P\3\2\2\2\tU\3\2\2\2\13[\3\2\2\2\r_\3\2\2\2\17b\3")
        buf.write("\2\2\2\21i\3\2\2\2\23o\3\2\2\2\25s\3\2\2\2\27u\3\2\2\2")
        buf.write("\31x\3\2\2\2\33z\3\2\2\2\35|\3\2\2\2\37~\3\2\2\2!\u0080")
        buf.write("\3\2\2\2#\u0082\3\2\2\2%\u0084\3\2\2\2\'\u0086\3\2\2\2")
        buf.write(")\u0088\3\2\2\2+\u008a\3\2\2\2-\u008c\3\2\2\2/\u008e\3")
        buf.write("\2\2\2\61\u0090\3\2\2\2\63\u0093\3\2\2\2\65\u0096\3\2")
        buf.write("\2\2\67\u0098\3\2\2\29\u009a\3\2\2\2;\u00b6\3\2\2\2=\u00b8")
        buf.write("\3\2\2\2?\u00c0\3\2\2\2A\u00cc\3\2\2\2C\u00d5\3\2\2\2")
        buf.write("E\u00d9\3\2\2\2G\u00ea\3\2\2\2IJ\7f\2\2JK\7g\2\2KL\7h")
        buf.write("\2\2L\4\3\2\2\2MN\7k\2\2NO\7h\2\2O\6\3\2\2\2PQ\7g\2\2")
        buf.write("QR\7n\2\2RS\7u\2\2ST\7g\2\2T\b\3\2\2\2UV\7y\2\2VW\7j\2")
        buf.write("\2WX\7k\2\2XY\7n\2\2YZ\7g\2\2Z\n\3\2\2\2[\\\7h\2\2\\]")
        buf.write("\7q\2\2]^\7t\2\2^\f\3\2\2\2_`\7k\2\2`a\7p\2\2a\16\3\2")
        buf.write("\2\2bc\7t\2\2cd\7g\2\2de\7v\2\2ef\7w\2\2fg\7t\2\2gh\7")
        buf.write("p\2\2h\20\3\2\2\2ij\7r\2\2jk\7t\2\2kl\7k\2\2lm\7p\2\2")
        buf.write("mn\7v\2\2n\22\3\2\2\2op\7n\2\2pq\7g\2\2qr\7p\2\2r\24\3")
        buf.write("\2\2\2st\7?\2\2t\26\3\2\2\2uv\7?\2\2vw\7?\2\2w\30\3\2")
        buf.write("\2\2xy\7*\2\2y\32\3\2\2\2z{\7+\2\2{\34\3\2\2\2|}\7]\2")
        buf.write("\2}\36\3\2\2\2~\177\7_\2\2\177 \3\2\2\2\u0080\u0081\7")
        buf.write(".\2\2\u0081\"\3\2\2\2\u0082\u0083\7<\2\2\u0083$\3\2\2")
        buf.write("\2\u0084\u0085\7-\2\2\u0085&\3\2\2\2\u0086\u0087\7,\2")
        buf.write("\2\u0087(\3\2\2\2\u0088\u0089\7/\2\2\u0089*\3\2\2\2\u008a")
        buf.write("\u008b\7\61\2\2\u008b,\3\2\2\2\u008c\u008d\7@\2\2\u008d")
        buf.write(".\3\2\2\2\u008e\u008f\7>\2\2\u008f\60\3\2\2\2\u0090\u0091")
        buf.write("\7>\2\2\u0091\u0092\7?\2\2\u0092\62\3\2\2\2\u0093\u0094")
        buf.write("\7@\2\2\u0094\u0095\7?\2\2\u0095\64\3\2\2\2\u0096\u0097")
        buf.write("\t\2\2\2\u0097\66\3\2\2\2\u0098\u0099\t\3\2\2\u00998\3")
        buf.write("\2\2\2\u009a\u009d\7)\2\2\u009b\u009e\5\65\33\2\u009c")
        buf.write("\u009e\t\4\2\2\u009d\u009b\3\2\2\2\u009d\u009c\3\2\2\2")
        buf.write("\u009d\u009e\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a0\7")
        buf.write(")\2\2\u00a0:\3\2\2\2\u00a1\u00b7\7\62\2\2\u00a2\u00a6")
        buf.write("\t\5\2\2\u00a3\u00a5\5\67\34\2\u00a4\u00a3\3\2\2\2\u00a5")
        buf.write("\u00a8\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2")
        buf.write("\u00a7\u00b7\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a9\u00ab\t")
        buf.write("\3\2\2\u00aa\u00a9\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00aa")
        buf.write("\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00af\3\2\2\2\u00ae")
        buf.write("\u00aa\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b0\3\2\2\2")
        buf.write("\u00b0\u00b2\7\60\2\2\u00b1\u00b3\t\3\2\2\u00b2\u00b1")
        buf.write("\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4")
        buf.write("\u00b5\3\2\2\2\u00b5\u00b7\3\2\2\2\u00b6\u00a1\3\2\2\2")
        buf.write("\u00b6\u00a2\3\2\2\2\u00b6\u00ae\3\2\2\2\u00b7<\3\2\2")
        buf.write("\2\u00b8\u00bd\5\65\33\2\u00b9\u00bc\5\65\33\2\u00ba\u00bc")
        buf.write("\5\67\34\2\u00bb\u00b9\3\2\2\2\u00bb\u00ba\3\2\2\2\u00bc")
        buf.write("\u00bf\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2")
        buf.write("\u00be>\3\2\2\2\u00bf\u00bd\3\2\2\2\u00c0\u00c6\7$\2\2")
        buf.write("\u00c1\u00c2\7$\2\2\u00c2\u00c5\7$\2\2\u00c3\u00c5\n\6")
        buf.write("\2\2\u00c4\u00c1\3\2\2\2\u00c4\u00c3\3\2\2\2\u00c5\u00c8")
        buf.write("\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7")
        buf.write("\u00c9\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c9\u00ca\7$\2\2")
        buf.write("\u00ca@\3\2\2\2\u00cb\u00cd\7\17\2\2\u00cc\u00cb\3\2\2")
        buf.write("\2\u00cc\u00cd\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00d2")
        buf.write("\7\f\2\2\u00cf\u00d1\t\7\2\2\u00d0\u00cf\3\2\2\2\u00d1")
        buf.write("\u00d4\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2")
        buf.write("\u00d3B\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d5\u00d6\t\b\2")
        buf.write("\2\u00d6\u00d7\3\2\2\2\u00d7\u00d8\b\"\2\2\u00d8D\3\2")
        buf.write("\2\2\u00d9\u00da\7$\2\2\u00da\u00db\7$\2\2\u00db\u00dc")
        buf.write("\7$\2\2\u00dc\u00de\3\2\2\2\u00dd\u00df\13\2\2\2\u00de")
        buf.write("\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e1\3\2\2\2")
        buf.write("\u00e0\u00de\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e3\7")
        buf.write("\"\2\2\u00e3\u00e4\7$\2\2\u00e4\u00e5\7$\2\2\u00e5\u00e6")
        buf.write("\7$\2\2\u00e6\u00e7\7\"\2\2\u00e7\u00e8\3\2\2\2\u00e8")
        buf.write("\u00e9\b#\2\2\u00e9F\3\2\2\2\u00ea\u00ec\7%\2\2\u00eb")
        buf.write("\u00ed\n\t\2\2\u00ec\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2")
        buf.write("\u00ee\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f0\3")
        buf.write("\2\2\2\u00f0\u00f1\b$\2\2\u00f1H\3\2\2\2\21\2\u009d\u00a6")
        buf.write("\u00ac\u00ae\u00b4\u00b6\u00bb\u00bd\u00c4\u00c6\u00cc")
        buf.write("\u00d2\u00e0\u00ee\3\b\2\2")
        return buf.getvalue()


class minipythonLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    DEF = 1
    IF = 2
    ELSE = 3
    WHILE = 4
    FOR = 5
    IN = 6
    RETURN = 7
    PRINT = 8
    LEN = 9
    ASSIGN = 10
    EQUAL = 11
    BLEFT = 12
    BRIGHT = 13
    SQLEFT = 14
    SQRIGHT = 15
    COMMA = 16
    COLON = 17
    SUM = 18
    MUL = 19
    SUB = 20
    DIV = 21
    HIGHER = 22
    LESS = 23
    LESSOREQUAL = 24
    HIGHEROREQUAL = 25
    CHAR = 26
    NUM = 27
    IDENTIFIER = 28
    STRING = 29
    NEWLINE = 30
    WS = 31
    BLOK_COMMENT = 32
    COMMENT = 33

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'def'", "'if'", "'else'", "'while'", "'for'", "'in'", "'return'", 
            "'print'", "'len'", "'='", "'=='", "'('", "')'", "'['", "']'", 
            "','", "':'", "'+'", "'*'", "'-'", "'/'", "'>'", "'<'", "'<='", 
            "'>='" ]

    symbolicNames = [ "<INVALID>",
            "DEF", "IF", "ELSE", "WHILE", "FOR", "IN", "RETURN", "PRINT", 
            "LEN", "ASSIGN", "EQUAL", "BLEFT", "BRIGHT", "SQLEFT", "SQRIGHT", 
            "COMMA", "COLON", "SUM", "MUL", "SUB", "DIV", "HIGHER", "LESS", 
            "LESSOREQUAL", "HIGHEROREQUAL", "CHAR", "NUM", "IDENTIFIER", 
            "STRING", "NEWLINE", "WS", "BLOK_COMMENT", "COMMENT" ]

    ruleNames = [ "DEF", "IF", "ELSE", "WHILE", "FOR", "IN", "RETURN", "PRINT", 
                  "LEN", "ASSIGN", "EQUAL", "BLEFT", "BRIGHT", "SQLEFT", 
                  "SQRIGHT", "COMMA", "COLON", "SUM", "MUL", "SUB", "DIV", 
                  "HIGHER", "LESS", "LESSOREQUAL", "HIGHEROREQUAL", "L", 
                  "N", "CHAR", "NUM", "IDENTIFIER", "STRING", "NEWLINE", 
                  "WS", "BLOK_COMMENT", "COMMENT" ]

    grammarFileName = "minipython.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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


