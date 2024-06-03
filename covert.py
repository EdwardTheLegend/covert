import argparse
from cparser import Parser
from cinterpreter import Interpreter
from clexer import Lexer

parser = argparse.ArgumentParser(prog="vin", description="Vin programming language")
parser.add_argument("file", type=str, help="Vin source code file", required=False)

args = parser.parse_args()

if args.file:
    with open(args.file, "r") as file:
        text = file.read()

    lexer = Lexer(text)
    lexer.parse_tokens()

    parser = Parser(lexer.tokens)
    parser.parse()

    interpreter = Interpreter(parser.ast)
    interpreter.interpret()
else:
    while True:
        try:
            text = input("vin> ")
        except EOFError:
            break

        lexer = Lexer(text)
        lexer.parse_tokens()

        parser = Parser(lexer.tokens)
        parser.parse()

        interpreter = Interpreter(parser.ast)
        interpreter.interpret()
