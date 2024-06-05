class TOKENS:
    LeftParen = "LeftParen"
    RightParen = "RightParen"
    LeftBrace = "LeftBrace"
    RightBrace = "RightBrace"
    LeftBracket = "LeftBracket"
    RightBracket = "RightBracket"
    Period = "Period"
    Comma = "Comma"
    Colon = "Colon"
    Keyword = "Keyword"
    Identifier = "Identifier"
    String = "String"
    Number = "Number"
    Boolean = "Boolean"
    Or = "Or"
    Not = "Not"
    And = "And"
    Equiv = "Equiv"
    NotEquiv = "NotEquiv"
    Gt = "Gt"
    Gte = "Gte"
    Lt = "Lt"
    Lte = "Lte"
    Plus = "Plus"
    Minus = "Minus"
    Asterisk = "Asterisk"
    Slash = "Slash"
    EOF = "EOF"

    chars = {
        "(": LeftParen,
        ")": RightParen,
        "{": LeftBrace,
        "}": RightBrace,
        "[": LeftBracket,
        "]": RightBracket,
        ".": Period,
        ",": Comma,
        ":": Colon,
        ">": Gt,
        ">=": Gte,
        "<": Lt,
        "<=": Lte,
        "+": Plus,
        "-": Minus,
        "*": Asterisk,
        "/": Slash,
    }


KEYWORDS = [
    "Agency",
    "suspect",  # variables
    "possibly",
    "employs",  # imports
    "agent",
    "expects",
    "report",  # functions
    "stakeout",
    "surveillance",
    "until",  # loops
    "investigate",
    "then",
    "fallback",  # conditionals
]


class Token:
    def __init__(self, type, value, content, line, column):
        self.type = type
        self.value = value
        self.content = content
        self.line = line
        self.column = column

    def __str__(self):
        return self.value


class Lexer:
    def __init__(self, text):
        self.text = text
        self.tokens = []
        self.current = 0
        self.line = 1
        self.column = 0

    def peek(self):
        if self.current >= len(self.text):
            return None
        return self.text[self.current]

    def peekn(self, n):
        if self.current + n >= len(self.text):
            return None
        return self.text[self.current + n]

    def advance(self):
        if self.current >= len(self.text):
            return None
        self.current += 1
        self.column += 1
        return self.text[self.current - 1]

    def match(self, char):
        if self.peek() == char:
            return self.advance()
        return False

    def match_word(self, word):
        for i in range(len(word)):
            if self.peekn(i) != word[i]:
                return False

        for _ in range(len(word)):
            self.advance()
        return True

    def start_identifier(self, char):
        identifier = char
        column = self.column
        while self.peek().isalnum() or self.peek() == "_":
            identifier += self.advance()

        if identifier in KEYWORDS:
            self.tokens.append(Token(TOKENS.Keyword, identifier, identifier, self.line, column))
        elif identifier == "true" or identifier == "false":
            self.tokens.append(Token(TOKENS.Boolean, identifier, identifier == "true", self.line, column))
        else:
            self.tokens.append(Token(TOKENS.Identifier, identifier, identifier, self.line, column))

    def scan_token(self):
        char = self.advance()

        match char:
            case "(" | ")" | "{" | "}" | "[" | "]" | "." | "," | ":" | "+" | "-" | "*" | "/":
                self.tokens.append(Token(TOKENS.chars[char], char, char, self.line, self.column))
            case "<" | ">":
                if self.match("="):
                    self.tokens.append(Token(TOKENS.chars[char + "="], char + "=", char + "=", self.line, self.column))
                else:
                    self.tokens.append(Token(TOKENS.chars[char], char, char, self.line, self.column))
            case "'" | '"':
                string = ""
                while self.peek() != char:
                    string += self.advance()
                    if not self.peek():
                        raise Exception(f"Unterminated string at line {self.line}")

                self.advance()  # closing quote
                self.tokens.append(Token(TOKENS.String, string, string, self.line, self.column))
            case "o":
                if self.match_word("r "):
                    self.tokens.append(Token(TOKENS.Or, "or", "or", self.line, self.column))
                else:
                    self.start_identifier(char)
            case "a":
                if self.match_word("nd "):
                    self.tokens.append(Token(TOKENS.And, "and", "and", self.line, self.column))
                else:
                    self.start_identifier(char)
            case "n":
                if self.match_word("ot "):
                    self.tokens.append(Token(TOKENS.Not, "not", "not", self.line, self.column))
                else:
                    self.start_identifier(char)
            case "?":  # comments
                while self.peek() != "\n":
                    self.advance()
            case " " | "\t" | "\r":
                pass
            case "\n":
                self.line += 1
                self.column = 0
            case _:
                if char.isdigit():
                    number = char
                    while self.peek().isdigit() or (self.peek() == "." and self.peekn(1).isdigit()):
                        number += self.advance()

                    self.tokens.append(Token(TOKENS.Number, number, float(number), self.line, self.column))
                elif char.isalpha() or char == "_":
                    self.start_identifier(char)
                else:
                    raise Exception(f"Invalid character '{char}' at line {self.line}")

    def scan_tokens(self):
        while self.peek():
            self.scan_token()

        self.tokens.append(Token(TOKENS.EOF, None, None, self.line, self.column))

        return self.tokens
