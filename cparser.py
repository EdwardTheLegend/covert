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
    
    def statement(self):        
        # TODO
        next = self.peek()

    def parse(self):
        while self.peek():
            self.ast.append(self.statement())

        return self.ast
