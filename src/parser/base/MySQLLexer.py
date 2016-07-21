# Generated from C:/pyprojects/hackathon/src/parser\MySQLLexer.g4 by ANTLR 4.5.3
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO




def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2")
        buf.write(u"N\u0226\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4")
        buf.write(u"\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r")
        buf.write(u"\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4")
        buf.write(u"$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(u",\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63")
        buf.write(u"\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\4")
        buf.write(u"9\t9\4:\t:\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA")
        buf.write(u"\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\t")
        buf.write(u"J\4K\tK\4L\tL\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\3\2\3\2\3")
        buf.write(u"\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3")
        buf.write(u"\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write(u"\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write(u"\b\3\t\3\t\3\t\3\t\3\t\5\t\u00d3\n\t\3\n\3\n\3\n\3\n")
        buf.write(u"\5\n\u00d9\n\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3")
        buf.write(u"\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write(u"\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3")
        buf.write(u"\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write(u"\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\5\25\u010d")
        buf.write(u"\n\25\3\26\3\26\3\26\3\26\5\26\u0113\n\26\3\27\3\27\3")
        buf.write(u"\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write(u"\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3")
        buf.write(u"\35\3\35\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write(u"\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#")
        buf.write(u"\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3+\3")
        buf.write(u"+\3,\3,\3-\3-\3-\3.\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60")
        buf.write(u"\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\64\3\64\3")
        buf.write(u"\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\66")
        buf.write(u"\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3")
        buf.write(u"8\38\38\38\38\38\39\39\39\39\39\39\3:\3:\3:\3:\3:\3:")
        buf.write(u"\3;\3;\3;\3;\3<\3<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3=\3>\3")
        buf.write(u">\3>\3?\3?\3?\3?\3@\3@\3@\3@\3A\3A\3A\3A\3A\3A\3A\3B")
        buf.write(u"\3B\3B\3B\3B\3B\3B\3B\3B\3B\3C\3C\3C\3C\3C\3C\3C\3C\3")
        buf.write(u"C\3C\3C\3C\3C\3C\3D\3D\3D\3D\3D\3D\3D\3D\3E\3E\3E\3E")
        buf.write(u"\3E\3F\3F\3F\3F\3F\3F\3G\3G\3G\3H\3H\3H\3I\6I\u01eb\n")
        buf.write(u"I\rI\16I\u01ec\3J\6J\u01f0\nJ\rJ\16J\u01f1\3K\5K\u01f5")
        buf.write(u"\nK\3K\3K\3K\3K\3L\6L\u01fc\nL\rL\16L\u01fd\3L\3L\3M")
        buf.write(u"\3M\3M\3M\3M\5M\u0207\nM\3N\3N\6N\u020b\nN\rN\16N\u020c")
        buf.write(u"\3N\3N\3O\3O\6O\u0213\nO\rO\16O\u0214\3O\3O\3P\3P\6P")
        buf.write(u"\u021b\nP\rP\16P\u021c\3P\3P\3Q\3Q\6Q\u0223\nQ\rQ\16")
        buf.write(u"Q\u0224\2\2R\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write(u"\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)")
        buf.write(u"\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write(u"\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65")
        buf.write(u"i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083C\u0085D")
        buf.write(u"\u0087E\u0089F\u008bG\u008dH\u008fI\u0091J\u0093K\u0095")
        buf.write(u"L\u0097M\u0099N\u009b\2\u009d\2\u009f\2\u00a1\2\3\2\b")
        buf.write(u"\5\2C\\aac|\5\2\13\f\17\17\"\"\3\2bb\3\2))\3\2$$\7\2")
        buf.write(u"&&\62;C\\aac|\u0231\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write(u"\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write(u"\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write(u"\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write(u"\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write(u"\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write(u"\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write(u"\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2")
        buf.write(u"E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2")
        buf.write(u"\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2")
        buf.write(u"\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2")
        buf.write(u"\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3")
        buf.write(u"\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2")
        buf.write(u"u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2")
        buf.write(u"\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write(u"\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2")
        buf.write(u"\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2")
        buf.write(u"\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099")
        buf.write(u"\3\2\2\2\3\u00a3\3\2\2\2\5\u00aa\3\2\2\2\7\u00b1\3\2")
        buf.write(u"\2\2\t\u00b6\3\2\2\2\13\u00bb\3\2\2\2\r\u00c2\3\2\2\2")
        buf.write(u"\17\u00c7\3\2\2\2\21\u00d2\3\2\2\2\23\u00d8\3\2\2\2\25")
        buf.write(u"\u00da\3\2\2\2\27\u00de\3\2\2\2\31\u00e1\3\2\2\2\33\u00e6")
        buf.write(u"\3\2\2\2\35\u00eb\3\2\2\2\37\u00ee\3\2\2\2!\u00f5\3\2")
        buf.write(u"\2\2#\u00f9\3\2\2\2%\u00fd\3\2\2\2\'\u0102\3\2\2\2)\u010c")
        buf.write(u"\3\2\2\2+\u0112\3\2\2\2-\u0114\3\2\2\2/\u011c\3\2\2\2")
        buf.write(u"\61\u0123\3\2\2\2\63\u0125\3\2\2\2\65\u0127\3\2\2\2\67")
        buf.write(u"\u0129\3\2\2\29\u012b\3\2\2\2;\u012d\3\2\2\2=\u012f\3")
        buf.write(u"\2\2\2?\u0136\3\2\2\2A\u0139\3\2\2\2C\u013c\3\2\2\2E")
        buf.write(u"\u0143\3\2\2\2G\u0145\3\2\2\2I\u0147\3\2\2\2K\u0149\3")
        buf.write(u"\2\2\2M\u014b\3\2\2\2O\u014d\3\2\2\2Q\u014f\3\2\2\2S")
        buf.write(u"\u0152\3\2\2\2U\u0154\3\2\2\2W\u0156\3\2\2\2Y\u0158\3")
        buf.write(u"\2\2\2[\u015b\3\2\2\2]\u015f\3\2\2\2_\u0162\3\2\2\2a")
        buf.write(u"\u0165\3\2\2\2c\u0167\3\2\2\2e\u0169\3\2\2\2g\u016b\3")
        buf.write(u"\2\2\2i\u0173\3\2\2\2k\u0179\3\2\2\2m\u017f\3\2\2\2o")
        buf.write(u"\u0184\3\2\2\2q\u018a\3\2\2\2s\u0190\3\2\2\2u\u0196\3")
        buf.write(u"\2\2\2w\u019a\3\2\2\2y\u01a0\3\2\2\2{\u01a6\3\2\2\2}")
        buf.write(u"\u01a9\3\2\2\2\177\u01ad\3\2\2\2\u0081\u01b1\3\2\2\2")
        buf.write(u"\u0083\u01b8\3\2\2\2\u0085\u01c2\3\2\2\2\u0087\u01d0")
        buf.write(u"\3\2\2\2\u0089\u01d8\3\2\2\2\u008b\u01dd\3\2\2\2\u008d")
        buf.write(u"\u01e3\3\2\2\2\u008f\u01e6\3\2\2\2\u0091\u01ea\3\2\2")
        buf.write(u"\2\u0093\u01ef\3\2\2\2\u0095\u01f4\3\2\2\2\u0097\u01fb")
        buf.write(u"\3\2\2\2\u0099\u0201\3\2\2\2\u009b\u0208\3\2\2\2\u009d")
        buf.write(u"\u0210\3\2\2\2\u009f\u0218\3\2\2\2\u00a1\u0222\3\2\2")
        buf.write(u"\2\u00a3\u00a4\7u\2\2\u00a4\u00a5\7g\2\2\u00a5\u00a6")
        buf.write(u"\7n\2\2\u00a6\u00a7\7g\2\2\u00a7\u00a8\7e\2\2\u00a8\u00a9")
        buf.write(u"\7v\2\2\u00a9\4\3\2\2\2\u00aa\u00ab\7k\2\2\u00ab\u00ac")
        buf.write(u"\7p\2\2\u00ac\u00ad\7u\2\2\u00ad\u00ae\7g\2\2\u00ae\u00af")
        buf.write(u"\7t\2\2\u00af\u00b0\7v\2\2\u00b0\6\3\2\2\2\u00b1\u00b2")
        buf.write(u"\7f\2\2\u00b2\u00b3\7g\2\2\u00b3\u00b4\7u\2\2\u00b4\u00b5")
        buf.write(u"\7e\2\2\u00b5\b\3\2\2\2\u00b6\u00b7\7k\2\2\u00b7\u00b8")
        buf.write(u"\7p\2\2\u00b8\u00b9\7v\2\2\u00b9\u00ba\7q\2\2\u00ba\n")
        buf.write(u"\3\2\2\2\u00bb\u00bc\7x\2\2\u00bc\u00bd\7c\2\2\u00bd")
        buf.write(u"\u00be\7n\2\2\u00be\u00bf\7w\2\2\u00bf\u00c0\7g\2\2\u00c0")
        buf.write(u"\u00c1\7u\2\2\u00c1\f\3\2\2\2\u00c2\u00c3\7h\2\2\u00c3")
        buf.write(u"\u00c4\7t\2\2\u00c4\u00c5\7q\2\2\u00c5\u00c6\7o\2\2\u00c6")
        buf.write(u"\16\3\2\2\2\u00c7\u00c8\7y\2\2\u00c8\u00c9\7j\2\2\u00c9")
        buf.write(u"\u00ca\7g\2\2\u00ca\u00cb\7t\2\2\u00cb\u00cc\7g\2\2\u00cc")
        buf.write(u"\20\3\2\2\2\u00cd\u00ce\7c\2\2\u00ce\u00cf\7p\2\2\u00cf")
        buf.write(u"\u00d3\7f\2\2\u00d0\u00d1\7(\2\2\u00d1\u00d3\7(\2\2\u00d2")
        buf.write(u"\u00cd\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d3\22\3\2\2\2\u00d4")
        buf.write(u"\u00d5\7q\2\2\u00d5\u00d9\7t\2\2\u00d6\u00d7\7~\2\2\u00d7")
        buf.write(u"\u00d9\7~\2\2\u00d8\u00d4\3\2\2\2\u00d8\u00d6\3\2\2\2")
        buf.write(u"\u00d9\24\3\2\2\2\u00da\u00db\7z\2\2\u00db\u00dc\7q\2")
        buf.write(u"\2\u00dc\u00dd\7t\2\2\u00dd\26\3\2\2\2\u00de\u00df\7")
        buf.write(u"k\2\2\u00df\u00e0\7u\2\2\u00e0\30\3\2\2\2\u00e1\u00e2")
        buf.write(u"\7p\2\2\u00e2\u00e3\7w\2\2\u00e3\u00e4\7n\2\2\u00e4\u00e5")
        buf.write(u"\7n\2\2\u00e5\32\3\2\2\2\u00e6\u00e7\7n\2\2\u00e7\u00e8")
        buf.write(u"\7k\2\2\u00e8\u00e9\7m\2\2\u00e9\u00ea\7g\2\2\u00ea\34")
        buf.write(u"\3\2\2\2\u00eb\u00ec\7k\2\2\u00ec\u00ed\7p\2\2\u00ed")
        buf.write(u"\36\3\2\2\2\u00ee\u00ef\7g\2\2\u00ef\u00f0\7z\2\2\u00f0")
        buf.write(u"\u00f1\7k\2\2\u00f1\u00f2\7u\2\2\u00f2\u00f3\7v\2\2\u00f3")
        buf.write(u"\u00f4\7u\2\2\u00f4 \3\2\2\2\u00f5\u00f6\7c\2\2\u00f6")
        buf.write(u"\u00f7\7n\2\2\u00f7\u00f8\7n\2\2\u00f8\"\3\2\2\2\u00f9")
        buf.write(u"\u00fa\7c\2\2\u00fa\u00fb\7p\2\2\u00fb\u00fc\7{\2\2\u00fc")
        buf.write(u"$\3\2\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff\7t\2\2\u00ff")
        buf.write(u"\u0100\7w\2\2\u0100\u0101\7g\2\2\u0101&\3\2\2\2\u0102")
        buf.write(u"\u0103\7h\2\2\u0103\u0104\7c\2\2\u0104\u0105\7n\2\2\u0105")
        buf.write(u"\u0106\7u\2\2\u0106\u0107\7g\2\2\u0107(\3\2\2\2\u0108")
        buf.write(u"\u0109\7f\2\2\u0109\u010a\7k\2\2\u010a\u010d\7x\2\2\u010b")
        buf.write(u"\u010d\7\61\2\2\u010c\u0108\3\2\2\2\u010c\u010b\3\2\2")
        buf.write(u"\2\u010d*\3\2\2\2\u010e\u010f\7o\2\2\u010f\u0110\7q\2")
        buf.write(u"\2\u0110\u0113\7f\2\2\u0111\u0113\7\'\2\2\u0112\u010e")
        buf.write(u"\3\2\2\2\u0112\u0111\3\2\2\2\u0113,\3\2\2\2\u0114\u0115")
        buf.write(u"\7d\2\2\u0115\u0116\7g\2\2\u0116\u0117\7v\2\2\u0117\u0118")
        buf.write(u"\7y\2\2\u0118\u0119\7g\2\2\u0119\u011a\7g\2\2\u011a\u011b")
        buf.write(u"\7p\2\2\u011b.\3\2\2\2\u011c\u011d\7t\2\2\u011d\u011e")
        buf.write(u"\7g\2\2\u011e\u011f\7i\2\2\u011f\u0120\7g\2\2\u0120\u0121")
        buf.write(u"\7z\2\2\u0121\u0122\7r\2\2\u0122\60\3\2\2\2\u0123\u0124")
        buf.write(u"\7-\2\2\u0124\62\3\2\2\2\u0125\u0126\7/\2\2\u0126\64")
        buf.write(u"\3\2\2\2\u0127\u0128\7\u0080\2\2\u0128\66\3\2\2\2\u0129")
        buf.write(u"\u012a\7~\2\2\u012a8\3\2\2\2\u012b\u012c\7(\2\2\u012c")
        buf.write(u":\3\2\2\2\u012d\u012e\7`\2\2\u012e<\3\2\2\2\u012f\u0130")
        buf.write(u"\7d\2\2\u0130\u0131\7k\2\2\u0131\u0132\7p\2\2\u0132\u0133")
        buf.write(u"\7c\2\2\u0133\u0134\7t\2\2\u0134\u0135\7{\2\2\u0135>")
        buf.write(u"\3\2\2\2\u0136\u0137\7>\2\2\u0137\u0138\7>\2\2\u0138")
        buf.write(u"@\3\2\2\2\u0139\u013a\7@\2\2\u013a\u013b\7@\2\2\u013b")
        buf.write(u"B\3\2\2\2\u013c\u013d\7g\2\2\u013d\u013e\7u\2\2\u013e")
        buf.write(u"\u013f\7e\2\2\u013f\u0140\7c\2\2\u0140\u0141\7r\2\2\u0141")
        buf.write(u"\u0142\7g\2\2\u0142D\3\2\2\2\u0143\u0144\7,\2\2\u0144")
        buf.write(u"F\3\2\2\2\u0145\u0146\7+\2\2\u0146H\3\2\2\2\u0147\u0148")
        buf.write(u"\7*\2\2\u0148J\3\2\2\2\u0149\u014a\7_\2\2\u014aL\3\2")
        buf.write(u"\2\2\u014b\u014c\7]\2\2\u014cN\3\2\2\2\u014d\u014e\7")
        buf.write(u"<\2\2\u014eP\3\2\2\2\u014f\u0150\7\60\2\2\u0150\u0151")
        buf.write(u"\7,\2\2\u0151R\3\2\2\2\u0152\u0153\7?\2\2\u0153T\3\2")
        buf.write(u"\2\2\u0154\u0155\7>\2\2\u0155V\3\2\2\2\u0156\u0157\7")
        buf.write(u"@\2\2\u0157X\3\2\2\2\u0158\u0159\7#\2\2\u0159\u015a\7")
        buf.write(u"?\2\2\u015aZ\3\2\2\2\u015b\u015c\7p\2\2\u015c\u015d\7")
        buf.write(u"q\2\2\u015d\u015e\7v\2\2\u015e\\\3\2\2\2\u015f\u0160")
        buf.write(u"\7>\2\2\u0160\u0161\7?\2\2\u0161^\3\2\2\2\u0162\u0163")
        buf.write(u"\7@\2\2\u0163\u0164\7?\2\2\u0164`\3\2\2\2\u0165\u0166")
        buf.write(u"\7=\2\2\u0166b\3\2\2\2\u0167\u0168\7.\2\2\u0168d\3\2")
        buf.write(u"\2\2\u0169\u016a\7\60\2\2\u016af\3\2\2\2\u016b\u016c")
        buf.write(u"\7e\2\2\u016c\u016d\7q\2\2\u016d\u016e\7n\2\2\u016e\u016f")
        buf.write(u"\7n\2\2\u016f\u0170\7c\2\2\u0170\u0171\7v\2\2\u0171\u0172")
        buf.write(u"\7g\2\2\u0172h\3\2\2\2\u0173\u0174\7k\2\2\u0174\u0175")
        buf.write(u"\7p\2\2\u0175\u0176\7p\2\2\u0176\u0177\7g\2\2\u0177\u0178")
        buf.write(u"\7t\2\2\u0178j\3\2\2\2\u0179\u017a\7q\2\2\u017a\u017b")
        buf.write(u"\7w\2\2\u017b\u017c\7v\2\2\u017c\u017d\7g\2\2\u017d\u017e")
        buf.write(u"\7t\2\2\u017el\3\2\2\2\u017f\u0180\7l\2\2\u0180\u0181")
        buf.write(u"\7q\2\2\u0181\u0182\7k\2\2\u0182\u0183\7p\2\2\u0183n")
        buf.write(u"\3\2\2\2\u0184\u0185\7e\2\2\u0185\u0186\7t\2\2\u0186")
        buf.write(u"\u0187\7q\2\2\u0187\u0188\7u\2\2\u0188\u0189\7u\2\2\u0189")
        buf.write(u"p\3\2\2\2\u018a\u018b\7w\2\2\u018b\u018c\7u\2\2\u018c")
        buf.write(u"\u018d\7k\2\2\u018d\u018e\7p\2\2\u018e\u018f\7i\2\2\u018f")
        buf.write(u"r\3\2\2\2\u0190\u0191\7k\2\2\u0191\u0192\7p\2\2\u0192")
        buf.write(u"\u0193\7f\2\2\u0193\u0194\7g\2\2\u0194\u0195\7z\2\2\u0195")
        buf.write(u"t\3\2\2\2\u0196\u0197\7m\2\2\u0197\u0198\7g\2\2\u0198")
        buf.write(u"\u0199\7{\2\2\u0199v\3\2\2\2\u019a\u019b\7q\2\2\u019b")
        buf.write(u"\u019c\7t\2\2\u019c\u019d\7f\2\2\u019d\u019e\7g\2\2\u019e")
        buf.write(u"\u019f\7t\2\2\u019fx\3\2\2\2\u01a0\u01a1\7i\2\2\u01a1")
        buf.write(u"\u01a2\7t\2\2\u01a2\u01a3\7q\2\2\u01a3\u01a4\7w\2\2\u01a4")
        buf.write(u"\u01a5\7r\2\2\u01a5z\3\2\2\2\u01a6\u01a7\7d\2\2\u01a7")
        buf.write(u"\u01a8\7{\2\2\u01a8|\3\2\2\2\u01a9\u01aa\7h\2\2\u01aa")
        buf.write(u"\u01ab\7q\2\2\u01ab\u01ac\7t\2\2\u01ac~\3\2\2\2\u01ad")
        buf.write(u"\u01ae\7w\2\2\u01ae\u01af\7u\2\2\u01af\u01b0\7g\2\2\u01b0")
        buf.write(u"\u0080\3\2\2\2\u01b1\u01b2\7k\2\2\u01b2\u01b3\7i\2\2")
        buf.write(u"\u01b3\u01b4\7p\2\2\u01b4\u01b5\7q\2\2\u01b5\u01b6\7")
        buf.write(u"t\2\2\u01b6\u01b7\7g\2\2\u01b7\u0082\3\2\2\2\u01b8\u01b9")
        buf.write(u"\7r\2\2\u01b9\u01ba\7c\2\2\u01ba\u01bb\7t\2\2\u01bb\u01bc")
        buf.write(u"\7v\2\2\u01bc\u01bd\7k\2\2\u01bd\u01be\7v\2\2\u01be\u01bf")
        buf.write(u"\7k\2\2\u01bf\u01c0\7q\2\2\u01c0\u01c1\7p\2\2\u01c1\u0084")
        buf.write(u"\3\2\2\2\u01c2\u01c3\7u\2\2\u01c3\u01c4\7v\2\2\u01c4")
        buf.write(u"\u01c5\7t\2\2\u01c5\u01c6\7c\2\2\u01c6\u01c7\7k\2\2\u01c7")
        buf.write(u"\u01c8\7i\2\2\u01c8\u01c9\7j\2\2\u01c9\u01ca\7v\2\2\u01ca")
        buf.write(u"\u01cb\7a\2\2\u01cb\u01cc\7l\2\2\u01cc\u01cd\7q\2\2\u01cd")
        buf.write(u"\u01ce\7k\2\2\u01ce\u01cf\7p\2\2\u01cf\u0086\3\2\2\2")
        buf.write(u"\u01d0\u01d1\7p\2\2\u01d1\u01d2\7c\2\2\u01d2\u01d3\7")
        buf.write(u"v\2\2\u01d3\u01d4\7w\2\2\u01d4\u01d5\7t\2\2\u01d5\u01d6")
        buf.write(u"\7c\2\2\u01d6\u01d7\7n\2\2\u01d7\u0088\3\2\2\2\u01d8")
        buf.write(u"\u01d9\7n\2\2\u01d9\u01da\7g\2\2\u01da\u01db\7h\2\2\u01db")
        buf.write(u"\u01dc\7v\2\2\u01dc\u008a\3\2\2\2\u01dd\u01de\7t\2\2")
        buf.write(u"\u01de\u01df\7k\2\2\u01df\u01e0\7i\2\2\u01e0\u01e1\7")
        buf.write(u"j\2\2\u01e1\u01e2\7v\2\2\u01e2\u008c\3\2\2\2\u01e3\u01e4")
        buf.write(u"\7q\2\2\u01e4\u01e5\7l\2\2\u01e5\u008e\3\2\2\2\u01e6")
        buf.write(u"\u01e7\7q\2\2\u01e7\u01e8\7p\2\2\u01e8\u0090\3\2\2\2")
        buf.write(u"\u01e9\u01eb\t\2\2\2\u01ea\u01e9\3\2\2\2\u01eb\u01ec")
        buf.write(u"\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ec\u01ed\3\2\2\2\u01ed")
        buf.write(u"\u0092\3\2\2\2\u01ee\u01f0\4\62;\2\u01ef\u01ee\3\2\2")
        buf.write(u"\2\u01f0\u01f1\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f1\u01f2")
        buf.write(u"\3\2\2\2\u01f2\u0094\3\2\2\2\u01f3\u01f5\7\17\2\2\u01f4")
        buf.write(u"\u01f3\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5\u01f6\3\2\2")
        buf.write(u"\2\u01f6\u01f7\7\f\2\2\u01f7\u01f8\3\2\2\2\u01f8\u01f9")
        buf.write(u"\bK\2\2\u01f9\u0096\3\2\2\2\u01fa\u01fc\t\3\2\2\u01fb")
        buf.write(u"\u01fa\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u01fb\3\2\2")
        buf.write(u"\2\u01fd\u01fe\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff\u0200")
        buf.write(u"\bL\2\2\u0200\u0098\3\2\2\2\u0201\u0206\7B\2\2\u0202")
        buf.write(u"\u0207\5\u009bN\2\u0203\u0207\5\u009dO\2\u0204\u0207")
        buf.write(u"\5\u009fP\2\u0205\u0207\5\u00a1Q\2\u0206\u0202\3\2\2")
        buf.write(u"\2\u0206\u0203\3\2\2\2\u0206\u0204\3\2\2\2\u0206\u0205")
        buf.write(u"\3\2\2\2\u0207\u009a\3\2\2\2\u0208\u020a\7b\2\2\u0209")
        buf.write(u"\u020b\n\4\2\2\u020a\u0209\3\2\2\2\u020b\u020c\3\2\2")
        buf.write(u"\2\u020c\u020a\3\2\2\2\u020c\u020d\3\2\2\2\u020d\u020e")
        buf.write(u"\3\2\2\2\u020e\u020f\7b\2\2\u020f\u009c\3\2\2\2\u0210")
        buf.write(u"\u0212\7)\2\2\u0211\u0213\n\5\2\2\u0212\u0211\3\2\2\2")
        buf.write(u"\u0213\u0214\3\2\2\2\u0214\u0212\3\2\2\2\u0214\u0215")
        buf.write(u"\3\2\2\2\u0215\u0216\3\2\2\2\u0216\u0217\7)\2\2\u0217")
        buf.write(u"\u009e\3\2\2\2\u0218\u021a\7$\2\2\u0219\u021b\n\6\2\2")
        buf.write(u"\u021a\u0219\3\2\2\2\u021b\u021c\3\2\2\2\u021c\u021a")
        buf.write(u"\3\2\2\2\u021c\u021d\3\2\2\2\u021d\u021e\3\2\2\2\u021e")
        buf.write(u"\u021f\7$\2\2\u021f\u00a0\3\2\2\2\u0220\u0223\t\7\2\2")
        buf.write(u"\u0221\u0223\5e\63\2\u0222\u0220\3\2\2\2\u0222\u0221")
        buf.write(u"\3\2\2\2\u0223\u0224\3\2\2\2\u0224\u0222\3\2\2\2\u0224")
        buf.write(u"\u0225\3\2\2\2\u0225\u00a2\3\2\2\2\21\2\u00d2\u00d8\u010c")
        buf.write(u"\u0112\u01ec\u01f1\u01f4\u01fd\u0206\u020c\u0214\u021c")
        buf.write(u"\u0222\u0224\3\b\2\2")
        return buf.getvalue()


class MySQLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    SELECT = 1
    INSERT = 2
    DESC = 3
    INTO = 4
    VALUES = 5
    FROM = 6
    WHERE = 7
    AND = 8
    OR = 9
    XOR = 10
    IS = 11
    NULL = 12
    LIKE = 13
    IN = 14
    EXISTS = 15
    ALL = 16
    ANY = 17
    TRUE = 18
    FALSE = 19
    DIVIDE = 20
    MOD = 21
    BETWEEN = 22
    REGEXP = 23
    PLUS = 24
    MINUS = 25
    NEGATION = 26
    VERTBAR = 27
    BITAND = 28
    POWER_OP = 29
    BINARY = 30
    SHIFT_LEFT = 31
    SHIFT_RIGHT = 32
    ESCAPE = 33
    ASTERISK = 34
    RPAREN = 35
    LPAREN = 36
    RBRACK = 37
    LBRACK = 38
    COLON = 39
    ALL_FIELDS = 40
    EQ = 41
    LTH = 42
    GTH = 43
    NOT_EQ = 44
    NOT = 45
    LET = 46
    GET = 47
    SEMI = 48
    COMMA = 49
    DOT = 50
    COLLATE = 51
    INNER = 52
    OUTER = 53
    JOIN = 54
    CROSS = 55
    USING = 56
    INDEX = 57
    KEY = 58
    ORDER = 59
    GROUP = 60
    BY = 61
    FOR = 62
    USE = 63
    IGNORE = 64
    PARTITION = 65
    STRAIGHT_JOIN = 66
    NATURAL = 67
    LEFT = 68
    RIGHT = 69
    OJ = 70
    ON = 71
    ID = 72
    INT = 73
    NEWLINE = 74
    WS = 75
    USER_VAR = 76

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'select'", u"'insert'", u"'desc'", u"'into'", u"'values'", 
            u"'from'", u"'where'", u"'xor'", u"'is'", u"'null'", u"'like'", 
            u"'in'", u"'exists'", u"'all'", u"'any'", u"'true'", u"'false'", 
            u"'between'", u"'regexp'", u"'+'", u"'-'", u"'~'", u"'|'", u"'&'", 
            u"'^'", u"'binary'", u"'<<'", u"'>>'", u"'escape'", u"'*'", 
            u"')'", u"'('", u"']'", u"'['", u"':'", u"'.*'", u"'='", u"'<'", 
            u"'>'", u"'!='", u"'not'", u"'<='", u"'>='", u"';'", u"','", 
            u"'.'", u"'collate'", u"'inner'", u"'outer'", u"'join'", u"'cross'", 
            u"'using'", u"'index'", u"'key'", u"'order'", u"'group'", u"'by'", 
            u"'for'", u"'use'", u"'ignore'", u"'partition'", u"'straight_join'", 
            u"'natural'", u"'left'", u"'right'", u"'oj'", u"'on'" ]

    symbolicNames = [ u"<INVALID>",
            u"SELECT", u"INSERT", u"DESC", u"INTO", u"VALUES", u"FROM", 
            u"WHERE", u"AND", u"OR", u"XOR", u"IS", u"NULL", u"LIKE", u"IN", 
            u"EXISTS", u"ALL", u"ANY", u"TRUE", u"FALSE", u"DIVIDE", u"MOD", 
            u"BETWEEN", u"REGEXP", u"PLUS", u"MINUS", u"NEGATION", u"VERTBAR", 
            u"BITAND", u"POWER_OP", u"BINARY", u"SHIFT_LEFT", u"SHIFT_RIGHT", 
            u"ESCAPE", u"ASTERISK", u"RPAREN", u"LPAREN", u"RBRACK", u"LBRACK", 
            u"COLON", u"ALL_FIELDS", u"EQ", u"LTH", u"GTH", u"NOT_EQ", u"NOT", 
            u"LET", u"GET", u"SEMI", u"COMMA", u"DOT", u"COLLATE", u"INNER", 
            u"OUTER", u"JOIN", u"CROSS", u"USING", u"INDEX", u"KEY", u"ORDER", 
            u"GROUP", u"BY", u"FOR", u"USE", u"IGNORE", u"PARTITION", u"STRAIGHT_JOIN", 
            u"NATURAL", u"LEFT", u"RIGHT", u"OJ", u"ON", u"ID", u"INT", 
            u"NEWLINE", u"WS", u"USER_VAR" ]

    ruleNames = [ u"SELECT", u"INSERT", u"DESC", u"INTO", u"VALUES", u"FROM", 
                  u"WHERE", u"AND", u"OR", u"XOR", u"IS", u"NULL", u"LIKE", 
                  u"IN", u"EXISTS", u"ALL", u"ANY", u"TRUE", u"FALSE", u"DIVIDE", 
                  u"MOD", u"BETWEEN", u"REGEXP", u"PLUS", u"MINUS", u"NEGATION", 
                  u"VERTBAR", u"BITAND", u"POWER_OP", u"BINARY", u"SHIFT_LEFT", 
                  u"SHIFT_RIGHT", u"ESCAPE", u"ASTERISK", u"RPAREN", u"LPAREN", 
                  u"RBRACK", u"LBRACK", u"COLON", u"ALL_FIELDS", u"EQ", 
                  u"LTH", u"GTH", u"NOT_EQ", u"NOT", u"LET", u"GET", u"SEMI", 
                  u"COMMA", u"DOT", u"COLLATE", u"INNER", u"OUTER", u"JOIN", 
                  u"CROSS", u"USING", u"INDEX", u"KEY", u"ORDER", u"GROUP", 
                  u"BY", u"FOR", u"USE", u"IGNORE", u"PARTITION", u"STRAIGHT_JOIN", 
                  u"NATURAL", u"LEFT", u"RIGHT", u"OJ", u"ON", u"ID", u"INT", 
                  u"NEWLINE", u"WS", u"USER_VAR", u"USER_VAR_SUBFIX1", u"USER_VAR_SUBFIX2", 
                  u"USER_VAR_SUBFIX3", u"USER_VAR_SUBFIX4" ]

    grammarFileName = u"MySQLLexer.g4"

    def __init__(self, input=None):
        super(MySQLLexer, self).__init__(input)
        self.checkVersion("4.5.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


