from clexer import TOKENS
from cast import (
    Literal,
    Array,
    Var,
    Set,
    Binary,
    Func,
    Return,
    For,
    While,
    Conditional,
    Struct,
    Instance,
    Call,
    Get,
    Unary,
    Agency,
    Employs,
)


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.ast = []

    def peek(self):
        if self.pos >= len(self.tokens):
            return None
        return self.tokens[self.pos]

    def peekn(self, n):
        if self.pos + n >= len(self.tokens):
            return None
        return self.tokens[self.pos + n]

    def eat(self, type):
        if peek_type := self.peek().type == type:
            self.pos += 1
            return self.tokens[self.pos - 1]

        raise Exception(f"Expected {type}, got {peek_type}")

    def expression(self):
        pass

    def statement(self):
        def agency():
            self.eat(TOKENS.Keyword)
            name = self.eat(TOKENS.Identifier)

            return Agency(name)

        def employs():
            self.eat(TOKENS.Keyword)
            name = self.eat(TOKENS.Identifier)

            return Employs(name)

        def functions():
            self.eat(TOKENS.Keyword)
            name = self.eat(TOKENS.Identifier)
            self.eat("expects")

            params = []
            while self.peek().type == TOKENS.Identifier:
                params.append(self.eat(TOKENS.Identifier))
                if self.peek().type == TOKENS.Comma:
                    self.eat(TOKENS.Comma)
            
            self.eat(TOKENS.LeftBrace)

            body = []
            while self.peek().type != TOKENS.RightBrace:
                body.append(self.statement())

            self.eat(TOKENS.RightBrace)

            return Func(name, params, body)

        def returns():
            self.eat(TOKENS.Keyword)
            value = self.expression()
            return Return(value)

        next = self.peek()
        match next.value:
            case "Agency":
                return agency()
            case "employs":
                return employs()
            case "report":
                return functions()
            case "investigate":
                return returns()
            case _:
                return self.expression()


    def parse(self):
        while self.peek():
            self.ast.append(self.statement())

        return self.ast
