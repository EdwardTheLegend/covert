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


class Lexer:
    def __init__(self, text):
        self.text = text
        self.tokens = []
        self.current = 0
        self.line = 1
        self.column = 0
