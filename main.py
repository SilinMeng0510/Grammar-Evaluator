import sys
import os
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from MyExprVisitor import MyExprVisitor


def readInputFile(file):
    with open(file) as f:
        contents = f.read()
    return contents


def main(argv):
    path = os.getcwd()
    input = InputStream(readInputFile(os.path.join(path, 'command')))

    lexer = ExprLexer(input)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.prog()
    MyExprVisitor().visitProg(tree)  # Evaluate the expression


if __name__ == '__main__':
    main(sys.argv)
